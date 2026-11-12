"""复核第3章作业中的数值结果；Python 3.11+，依赖 NumPy。"""

from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from numpy.polynomial import chebyshev, legendre


def integrate(function, left: float, right: float, order: int = 128) -> float:
    nodes, weights = legendre.leggauss(order)
    x = (right - left) * nodes / 2 + (right + left) / 2
    return float((right - left) / 2 * (weights @ function(x)))


def solve_exact(matrix, rhs):
    """小型法方程使用 Fraction 高斯消元，避免高次幂基的舍入误差。"""
    n = len(rhs)
    rows = [[F(v) for v in row] + [F(rhs[i])] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        divisor = rows[k][k]
        rows[k] = [v / divisor for v in rows[k]]
        for i in range(n):
            if i != k:
                factor = rows[i][k]
                rows[i] = [v - factor * w for v, w in zip(rows[i], rows[k])]
    return [row[-1] for row in rows]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="保存完整验算结果")
    args = parser.parse_args()
    checks = []
    result = {}

    def check(name, condition):
        passed = bool(condition)
        checks.append({"name": name, "passed": passed})
        if not passed:
            raise AssertionError(name)

    # 第7题：三点交错，并检查残差导数只有一个内部零点。
    k = math.e - 1
    xi = math.log(k)
    error = (1 + k * xi - k) / 2
    intercept = 1 - error
    points = np.array([0.0, xi, 1.0])
    r7 = np.exp(points) - k * points - intercept
    check("q7_alternation", np.allclose(r7, [error, -error, error], atol=2e-15, rtol=0))
    check("q7_interior_stationary_point", 0 < xi < 1 and abs(math.exp(xi) - k) < 1e-14)
    result["q7"] = {"slope": k, "intercept": intercept, "xi": xi, "uniform_error": error}

    # 第9题：Chebyshev 残差恒等式和五点交错。
    grid = np.linspace(0, 1, 1001)
    f9 = lambda x: x**4 + 3 * x**3 - 1
    p9 = lambda x: 5 * x**3 - 5 / 4 * x**2 + x / 4 - 129 / 128
    e9 = lambda x: chebyshev.chebval(2 * x - 1, [0, 0, 0, 0, 1]) / 128
    check("q9_residual_identity", np.max(np.abs(f9(grid) - p9(grid) - e9(grid))) < 3e-15)
    extrema = (1 + np.cos(np.arange(5) * math.pi / 4)) / 2
    check("q9_alternation", np.allclose(f9(extrema) - p9(extrema), (-1.0) ** np.arange(5) / 128, atol=3e-15, rtol=0))
    result["q9"] = {"ascending_power_coefficients": [-129 / 128, 1 / 4, -5 / 4, 5], "uniform_error": 1 / 128}

    # 第13题：直接积分检查正交性及误差恒等式。
    a = 24 * (4 - math.pi) / math.pi**3
    b = 8 * (math.pi - 3) / math.pi**2
    r13 = lambda x: np.sin(x) - a * x - b
    moments13 = [integrate(lambda x, j=j: r13(x) * x**j, 0, math.pi / 2) for j in [0, 1]]
    j13 = integrate(lambda x: r13(x) ** 2, 0, math.pi / 2)
    check("q13_orthogonality", max(map(abs, moments13)) < 2e-14)
    check("q13_squared_error", abs(j13 - (math.pi / 4 - a - b)) < 2e-14)
    result["q13"] = {"a": a, "b": b, "squared_error": j13, "L2_error": math.sqrt(j13)}

    # 第17题：用精确分数解两组 Gram 系统，再直接数值积分残差。
    for label, powers in [("q17_phi1", [0, 1]), ("q17_phi2", [100, 101])]:
        gram = [[F(1, i + j + 1) for j in powers] for i in powers]
        rhs = [F(1, i + 3) for i in powers]
        coefficients = solve_exact(gram, rhs)
        check(label + "_exact_normal_equations", all(sum(gram[i][j] * coefficients[j] for j in range(2)) == rhs[i] for i in range(2)))
        squared = F(1, 5) - sum(c * v for c, v in zip(coefficients, rhs))
        residual = lambda x: x**2 - sum(float(c) * x**p for c, p in zip(coefficients, powers))
        integral = integrate(lambda x: residual(x) ** 2, 0, 1, 256)
        check(label + "_independent_integral", abs(integral - float(squared)) < 3e-13)
        result[label] = {"powers": powers, "coefficients_exact": list(map(str, coefficients)), "squared_error_exact": str(squared), "squared_error": float(squared), "L2_error": math.sqrt(float(squared))}
    check("q17_phi1_is_better", result["q17_phi1"]["squared_error"] < result["q17_phi2"]["squared_error"])

    # 第18题：abs 在0处不可导，将积分拆在 [0,1] 再利用偶性。
    powers18 = [0, 2, 4]
    gram18 = [[F(2, i + j + 1) for j in powers18] for i in powers18]
    rhs18 = [F(2, i + 2) for i in powers18]
    c18 = solve_exact(gram18, rhs18)
    check("q18_exact_coefficients", c18 == [F(15, 128), F(105, 64), F(-105, 128)])
    j18 = F(2, 3) - sum(c * v for c, v in zip(c18, rhs18))
    r18 = lambda x: x - sum(float(c) * x**p for c, p in zip(c18, powers18))
    check("q18_exact_squared_error", j18 == F(1, 384))
    check("q18_independent_integral", abs(2 * integrate(lambda x: r18(x) ** 2, 0, 1) - float(j18)) < 1e-14)
    result["q18"] = {"coefficients_exact": list(map(str, c18)), "squared_error_exact": str(j18), "squared_error": float(j18)}

    # 第20题：128/256点积分独立验证解析 Legendre 系数和残差平方。
    c20 = np.array([0, 12 / math.pi**2, 0, 168 * (math.pi**2 - 10) / math.pi**4])
    f20 = lambda x: np.sin(math.pi * x / 2)
    r20 = lambda x: f20(x) - legendre.legval(x, c20)
    for order in [128, 256]:
        numerical = [(2 * j + 1) / 2 * integrate(lambda x, j=j: f20(x) * legendre.legval(x, [0] * j + [1]), -1, 1, order) for j in range(4)]
        check(f"q20_legendre_coefficients_{order}", np.max(np.abs(c20 - numerical)) < 2e-13)
        check(f"q20_residual_orthogonality_{order}", max(abs(integrate(lambda x, j=j: r20(x) * x**j, -1, 1, order)) for j in range(4)) < 2e-14)
    j20_direct = integrate(lambda x: r20(x) ** 2, -1, 1, 256)
    j20_projection = 1 - 2 / 3 * c20[1] ** 2 - 2 / 7 * c20[3] ** 2
    check("q20_squared_error", abs(j20_direct - j20_projection) < 2e-14)
    result["q20"] = {"legendre_coefficients": c20.tolist(), "ascending_power_coefficients": legendre.leg2poly(c20).tolist(), "squared_error": j20_direct, "L2_error_textbook_convention": math.sqrt(j20_direct), "RMSE_interval_normalized": math.sqrt(j20_direct / 2)}

    # 第23题：用原始设计矩阵的 lstsq，交叉检查手写法方程。
    t = np.array([0, 0.9, 1.9, 3.0, 3.9, 5.0])
    distance = np.array([0, 10, 30, 50, 80, 110.0])
    design = np.column_stack([np.ones_like(t), t, t**2])
    expected_gram = [[6, 14.7, 53.63], [14.7, 53.63, 218.907], [53.63, 218.907, 951.0323]]
    check("q23_normal_matrix", np.allclose(design.T @ design, expected_gram, atol=2e-12, rtol=0))
    check("q23_normal_rhs", np.allclose(design.T @ distance, [280, 1078, 4533.2], atol=2e-12, rtol=0))
    for name, matrix in [("q23_quadratic", design), ("q23_fixed_origin", design[:, 1:])]:
        coeffs, _, rank, _ = np.linalg.lstsq(matrix, distance, rcond=None)
        residual = matrix @ coeffs - distance
        check(name + "_full_rank", rank == matrix.shape[1])
        check(name + "_orthogonality", np.max(np.abs(matrix.T @ residual)) < 5e-10)
        squared = float(residual @ residual)
        result[name] = {"coefficients": coeffs.tolist(), "predictions": (matrix @ coeffs).tolist(), "residuals_fit_minus_observed": residual.tolist(), "sum_squared_error": squared, "RMSE": math.sqrt(squared / len(t))}

    # 选做例3.2：精确内积求系数，直接积分验证原书误差问题。
    d0 = (math.sqrt(2) + math.asinh(1)) / 2
    d1 = (2 * math.sqrt(2) - 1) / 3
    c32 = np.array([4 * d0 - 6 * d1, -6 * d0 + 12 * d1])
    r32 = lambda x: np.sqrt(1 + x**2) - c32[0] - c32[1] * x
    j32 = integrate(lambda x: r32(x) ** 2, 0, 1)
    check("example32_orthogonality", max(abs(integrate(lambda x, j=j: r32(x) * x**j, 0, 1)) for j in range(2)) < 1e-14)
    check("example32_projection_identity", abs(j32 - (4 / 3 - c32 @ [d0, d1])) < 2e-14)
    rounded_j32 = integrate(lambda x: (np.sqrt(1 + x**2) - 0.934 - 0.426 * x) ** 2, 0, 1)
    result["example3_2"] = {"coefficients": c32.tolist(), "squared_error": j32, "L2_error": math.sqrt(j32), "printed_rounded_coefficients_squared_error": rounded_j32, "printed_squared_error": 0.0026}

    # 选做例3.3：验证缩放 Chebyshev 残差及交错点。
    x33 = np.array([-1.0, -0.5, 0.5, 1.0])
    r33 = (2 * x33**3 + x33**2 + 2 * x33 - 1) - (x33**2 + 3.5 * x33 - 1)
    check("example33_alternation", np.array_equal(r33, [-0.5, 0.5, -0.5, 0.5]))
    result["example3_3"] = {"ascending_power_coefficients": [-1, 3.5, 1], "uniform_error": 0.5}

    # 选做例3.4：解析 Legendre 系数与数值积分交叉复核。
    e = math.e
    c34 = np.array([(e - 1 / e) / 2, 3 / e, 5 / 2 * (e - 7 / e), 7 / 2 * (37 / e - 5 * e)])
    c34_quad = [(2 * j + 1) / 2 * integrate(lambda x, j=j: np.exp(x) * legendre.legval(x, [0] * j + [1]), -1, 1) for j in range(4)]
    check("example34_coefficients", np.max(np.abs(c34 - c34_quad)) < 3e-13)
    j34 = integrate(lambda x: (np.exp(x) - legendre.legval(x, c34)) ** 2, -1, 1)
    check("example34_squared_error", abs(j34 - 2.22888704227389e-5) < 1e-16)
    result["example3_4"] = {"legendre_coefficients": c34.tolist(), "ascending_power_coefficients": legendre.leg2poly(c34).tolist(), "squared_error": j34, "L2_error": math.sqrt(j34)}

    # 选做例3.5：以表3.3原数据重建加权系统，检出书中数值错误。
    x35 = np.arange(1.0, 6.0)
    y35 = np.array([4, 4.5, 6, 8, 8.5])
    weights35 = np.array([2.0, 1, 3, 1, 1])
    a35 = np.column_stack([np.ones_like(x35), x35])
    aw35 = a35 * np.sqrt(weights35)[:, None]
    c35 = np.linalg.lstsq(aw35, y35 * np.sqrt(weights35), rcond=None)[0]
    gram35 = a35.T @ (weights35[:, None] * a35)
    rhs35 = a35.T @ (weights35 * y35)
    check("example35_source_data_sums", np.array_equal(gram35, [[8, 22], [22, 74]]) and np.array_equal(rhs35, [47, 145.5]))
    check("example35_exact_solution", np.allclose(c35, [277 / 108, 65 / 54], atol=3e-14, rtol=0))
    res35 = a35 @ c35 - y35
    j35 = float(weights35 @ res35**2)
    check("example35_weighted_orthogonality", np.max(np.abs(a35.T @ (weights35 * res35))) < 2e-13)
    check("example35_squared_error", abs(j35 - 22 / 27) < 5e-15)
    printed_normal_residual = gram35 @ [2.77, 1.13] - rhs35
    check("example35_printed_numbers_do_not_solve_system", np.max(np.abs(printed_normal_residual)) > 0.9)
    result["example3_5"] = {"coefficients_exact": ["277/108", "65/54"], "coefficients": c35.tolist(), "weighted_sum_squared_error": j35, "printed_coefficients_normal_residual": printed_normal_residual.tolist()}

    payload = {"status": "passed", "python": platform.python_version(), "numpy": np.__version__, "checks_passed": len(checks), "checks": checks, "results": result}
    for name, values in result.items():
        print(name + ": " + json.dumps(values, ensure_ascii=False))
    print(f"PASS: {len(checks)} checks")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
