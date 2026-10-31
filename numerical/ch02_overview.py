"""Chapter 2 reference experiment; running this is NOT independent implementation.

Prepare once, then read the saved CSV files in a separate run:
    python numerical/ch02_overview.py prepare
    python numerical/ch02_overview.py run

Lagrange/Newton use library references; write your own versions in a separate file.
Chapter source: JunFengXiang/numerical-computing-lab,
numerical-analysis/book/verified/sections/2.2.3.md through 2.8.1.md.
API references: https://docs.scipy.org/doc/scipy/reference/interpolate.html
"""

import argparse
import csv
import hashlib
import json
import math
import platform
from datetime import datetime, timezone
from pathlib import Path


def write_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def prepare(folder):
    """Only this preparation step knows the analytic teaching functions."""
    paths = [folder / name for name in ("nodes.csv", "queries.csv", "manifest.json")]
    if any(path.exists() for path in paths):
        raise FileExistsError("Input already exists; keep it or use a new --data-dir.")
    cases = [
        ("square3", 0.0, 1.0, 3, lambda x: x*x, lambda x: 2*x, "x**2", "2*x"),
        ("sin5", 0.0, 1.0, 5, math.sin, math.cos, "sin(x), x in radians", "cos(x)"),
        ("runge11", -1.0, 1.0, 11, lambda x: 1/(1+25*x*x),
         lambda x: -50*x/(1+25*x*x)**2, "1/(1+25*x**2)", "-50*x/(1+25*x**2)**2"),
    ]
    nodes, queries, descriptions = [], [], []
    for case, left, right, count, function, derivative, formula, dformula in cases:
        for i in range(count):
            x = left + (right-left)*i/(count-1)
            nodes.append(dict(case_id=case, x=x, y=function(x), dy=derivative(x)))
        for i in range(401):
            x = left + (right-left)*i/400
            queries.append(dict(case_id=case, x=x, y_reference=function(x)))
        descriptions.append(dict(case_id=case, function=formula, derivative=dformula,
                                 interval=[left, right], nodes=count, queries=401))
    folder.mkdir(parents=True, exist_ok=True)
    write_csv(paths[0], ["case_id", "x", "y", "dy"], nodes)
    write_csv(paths[1], ["case_id", "x", "y_reference"], queries)
    paths[2].write_text(json.dumps(dict(
        version="ch02-v1", source="synthetic teaching data; not field measurements",
        reference="Python binary64 math/arithmetic; not exact decimal function values",
        seed=None, random_sampling=False, cases=descriptions,
    ), ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"Prepared {len(nodes)} nodes and {len(queries)} queries in {folder}")


def read_rows(path, fields):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if not set(fields).issubset(reader.fieldnames or []):
            raise ValueError(f"Missing columns in {path}: expected {fields}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"Empty input: {path}")
    return rows


def aitken(x, y, target):
    """Reference recurrence, textbook (2.3.1); not the independent-work target."""
    p = list(y)
    for k in range(len(x)-1):
        for j in range(k+1, len(x)):
            p[j] = p[k] + (p[j]-p[k])*(target-x[k])/(x[j]-x[k])
    return p[-1]


def neville(x, y, target):
    """Alternative recurrence, textbook (2.3.2)."""
    p = list(y)
    for width in range(1, len(x)):
        for i in range(len(x)-width):
            j = i + width
            p[i] = ((x[j]-target)*p[i] + (target-x[i])*p[i+1])/(x[j]-x[i])
    return p[0]


def equal_grid_formula(np, x, y, queries, backward=False):
    """Full-degree Newton forward/backward difference formula, section 2.5.2."""
    h = x[1]-x[0]
    if not np.allclose(np.diff(x), h, rtol=1e-10, atol=0):
        raise ValueError("Forward/backward formulas require equally spaced nodes.")
    index = -1 if backward else 0
    t = (queries-x[index])/h
    values = np.full_like(queries, y[index])
    factor = np.ones_like(queries)
    differences = y.copy()
    for order in range(1, len(x)):
        differences = np.diff(differences)
        shift = order-1 if backward else 1-order
        factor *= (t+shift)/order
        values += factor*differences[index]
    return values


def methods(np, x, y, dy):
    from scipy.interpolate import (
        BarycentricInterpolator, CubicHermiteSpline, CubicSpline, KroghInterpolator,
    )
    # Barycentric weights use a fixed RNG; there is no random data generation.
    polynomial = BarycentricInterpolator(x, y, rng=0)
    newton_ref = KroghInterpolator(x, y)
    hermite = KroghInterpolator(np.repeat(x, 2), np.column_stack((y, dy)).ravel())
    piecewise_hermite = CubicHermiteSpline(x, y, dy, extrapolate=False)
    natural = CubicSpline(x, y, bc_type="natural", extrapolate=False)
    clamped = CubicSpline(x, y, bc_type=((1, dy[0]), (1, dy[-1])), extrapolate=False)
    endpoints = np.array([0, len(x)-1])
    three = np.array([0, len(x)//2, len(x)-1])
    all_nodes = np.arange(len(x))
    specs = [
        ("linear_2nodes", BarycentricInterpolator(x[endpoints], y[endpoints], rng=0), endpoints, "values_only"),
        ("quadratic_3nodes", BarycentricInterpolator(x[three], y[three], rng=0), three, "values_only"),
        ("lagrange", polynomial, all_nodes, "values_only"),
        ("aitken", lambda q: np.array([aitken(x, y, t) for t in q]), all_nodes, "values_only"),
        ("neville", lambda q: np.array([neville(x, y, t) for t in q]), all_nodes, "values_only"),
        ("newton_reference", newton_ref, all_nodes, "values_only"),
        ("newton_forward", lambda q: equal_grid_formula(np, x, y, q), all_nodes, "values_only"),
        ("newton_backward", lambda q: equal_grid_formula(np, x, y, q, True), all_nodes, "values_only"),
        ("hermite_global", hermite, all_nodes, "all_node_first_derivatives"),
        ("piecewise_linear", lambda q: np.interp(q, x, y), all_nodes, "values_only"),
        ("piecewise_hermite", piecewise_hermite, all_nodes, "all_node_first_derivatives"),
        ("spline_natural", natural, all_nodes, "zero_endpoint_second_derivatives"),
        ("spline_given_slopes", clamped, all_nodes, "given_endpoint_first_derivatives"),
    ]
    checks = {
        "global_hermite_derivatives": float(np.max(np.abs(hermite.derivative(x)-dy))),
        "piecewise_hermite_derivatives": float(np.max(np.abs(piecewise_hermite(x, 1)-dy))),
        "natural_second_derivatives": float(np.max(np.abs(natural(x[endpoints], 2)))),
        "given_endpoint_slopes": float(np.max(np.abs(clamped(x[endpoints], 1)-dy[endpoints]))),
    }
    return specs, checks


def plot_case(np, out, case, x, y, queries, truth, predictions):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    chosen = ["lagrange", "hermite_global", "piecewise_linear", "piecewise_hermite",
              "spline_natural", "spline_given_slopes"]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)
    axes[0].plot(queries, truth, color="black", linewidth=2.4, label="reference")
    axes[0].scatter(x, y, color="black", s=22, zorder=10, label="nodes")
    for name in chosen:
        axes[0].plot(queries, predictions[name], linewidth=1.3, label=name)
        error = np.abs(predictions[name]-truth)
        axes[1].plot(queries, np.ma.masked_equal(error, 0), linewidth=1.3, label=name)
    axes[0].set(xlabel="x (radians for sin)", ylabel="value", title=f"{case}: interpolants")
    axes[1].set(xlabel="x", ylabel="absolute error", yscale="log",
                title="401-point grid error; exact zeros omitted")
    for ax in axes:
        ax.grid(alpha=.2)
    axes[0].legend(fontsize=7)
    fig.savefig(out / f"{case}.png", dpi=150)
    plt.close(fig)


def run(folder, out, no_plot):
    import numpy as np
    import scipy
    nodes = read_rows(folder / "nodes.csv", ["case_id", "x", "y", "dy"])
    queries = read_rows(folder / "queries.csv", ["case_id", "x", "y_reference"])
    cases = sorted({row["case_id"] for row in nodes})
    if {row["case_id"] for row in queries} != set(cases):
        raise ValueError("Node/query case IDs do not match.")
    prepared = []
    for case in cases:
        node_rows = [row for row in nodes if row["case_id"] == case]
        query_rows = [row for row in queries if row["case_id"] == case]
        x, y, dy = np.array([[float(row[k]) for k in ("x", "y", "dy")]
                            for row in node_rows]).T
        q, truth = np.array([[float(row[k]) for k in ("x", "y_reference")]
                             for row in query_rows]).T
        if len(x) < 3 or not np.all(np.isfinite(np.concatenate((x, y, dy, q, truth)))):
            raise ValueError(f"{case}: need at least three finite nodes and finite queries.")
        if not np.all(np.diff(x) > 0):
            raise ValueError(f"{case}: nodes must be strictly increasing and distinct.")
        if q.min() < x[0] or q.max() > x[-1]:
            raise ValueError(f"{case}: this experiment does not use extrapolation.")
        prepared.append((case, x, y, dy, q, truth))
    out.mkdir(parents=True, exist_ok=False)
    summary, point_rows, check_rows = [], [], []
    for case, x, y, dy, q, truth in prepared:
        specs, checks = methods(np, x, y, dy)
        predictions = {}
        for name, function, indices, extra in specs:
            predicted = np.asarray(function(q), dtype=float)
            if predicted.shape != q.shape or not np.all(np.isfinite(predicted)):
                raise ValueError(f"Invalid predictions: {case}/{name}")
            predictions[name] = predicted
            errors = np.abs(predicted-truth)
            node_error = float(np.max(np.abs(function(x[indices])-y[indices])))
            if node_error > 1e-7:
                raise ArithmeticError(f"Node reproduction failed: {case}/{name}: {node_error}")
            summary.append(dict(case_id=case, method=name, used_nodes=len(indices),
                                extra_information=extra, query_count=len(q),
                                max_grid_abs_error=float(errors.max()),
                                mean_grid_abs_error=float(errors.mean()),
                                max_used_node_error=node_error, status="ok"))
            point_rows.extend(dict(case_id=case, method=name, x=float(t),
                                   y_pred=float(p), y_reference=float(r), abs_error=float(e))
                              for t, p, r, e in zip(q, predicted, truth, errors))
        family = ["aitken", "neville", "newton_reference", "newton_forward", "newton_backward"]
        checks["same_polynomial_max_gap"] = max(float(np.max(np.abs(
            predictions[name]-predictions["lagrange"]))) for name in family)
        for name, error in checks.items():
            tolerance = 1e-6 if "global_hermite" in name else 1e-8
            check_rows.append(dict(case_id=case, check=name, error=error,
                                   tolerance=tolerance, passed=error <= tolerance))
            if error > tolerance:
                raise ArithmeticError(f"Check failed: {case}/{name}: {error}")
        if not no_plot:
            plot_case(np, out, case, x, y, q, truth, predictions)
    write_csv(out / "summary.csv", list(summary[0]), summary)
    write_csv(out / "predictions.csv", list(point_rows[0]), point_rows)
    write_csv(out / "checks.csv", list(check_rows[0]), check_rows)
    hashes = {name: hashlib.sha256((folder/name).read_bytes()).hexdigest()
              for name in ("nodes.csv", "queries.csv")}
    (out / "run.json").write_text(json.dumps(dict(
        author="assistant reference demonstration; not student completion",
        data_dir=str(folder.resolve()), input_sha256=hashes, python=platform.python_version(),
        numpy=np.__version__, scipy=scipy.__version__, dtype="float64",
        error_scope="maximum/mean on saved query grid, not a continuous sup norm",
        note="Hermite uses additional derivatives; low-degree baselines use fewer nodes.",
    ), indent=2)+"\n", encoding="utf-8")
    for row in summary:
        print(f"{row['case_id']:9s} {row['method']:24s} {row['max_grid_abs_error']:.6e}")
    print(f"Saved outputs to {out}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["prepare", "run"])
    parser.add_argument("--data-dir", type=Path, default=Path("data/interpolation/ch02-v1"))
    parser.add_argument("--out", type=Path)
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()
    if args.action == "prepare":
        prepare(args.data_dir)
    else:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        run(args.data_dir, args.out or Path("results/ch02-overview")/timestamp, args.no_plot)


if __name__ == "__main__":
    main()
