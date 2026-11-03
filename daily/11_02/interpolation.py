from pathlib import Path
import numpy as np

path = Path(__file__).parent / "data" / "nodes.csv"
data = np.loadtxt(path, delimiter=",", skiprows=1)

nodes = data[[0, 50, -1]]#第1行，第51行 最后一行
x0, x1, x2 = nodes[:, 0]
b = nodes[:, 1]

A = np.array([
    [1, x0, x0**2],
    [1, x1, x1**2],
    [1, x2, x2**2]
])

print("系数矩阵 A：")
print(A)
print("右端向量 b：", b)
print("形状：", A.shape, b.shape)

coeffs = np.linalg.solve(A,b)

print(coeffs)

node_pred = A @ coeffs
print("三个节点的预测值:",node_pred)
print("三个节点的已知数据:",b)
print("最大节点误差: ",np.abs(node_pred-b).max())


query_path = path.parent/"queries.csv"
query_data = np.loadtxt(query_path,delimiter= ",",skiprows = 1)
query_xs = query_data[:, 0]
y_reference = query_data[:,1]
Q = np.column_stack([
    np.ones_like(query_xs),
    query_xs,
    query_xs**2
])

y_pred = Q @ coeffs
print("查询矩阵形状:",Q.shape)
print("预测值形状",y_pred.shape)
print("前三个预测值:",y_pred[:3])

# 使用相同节点和查询点，比较矩阵法与Lagrange形式。
y0, y1, y2 = b
L0 = ((query_xs - x1) * (query_xs - x2)) / ((x0 - x1) * (x0 - x2))
L1 = ((query_xs - x0) * (query_xs - x2)) / ((x1 - x0) * (x1 - x2))
L2 = ((query_xs - x0) * (query_xs - x1)) / ((x2 - x0) * (x2 - x1))
y_lagrange = y0 * L0 + y1 * L1 + y2 * L2

method_difference = np.abs(y_pred - y_lagrange)
abs_error = np.abs(y_pred - y_reference)

print("比较的查询点数量：", len(query_xs))
print("两种方法的最大绝对差：", method_difference.max())
print("两种方法在1e-12容差内一致：",
      np.allclose(y_pred, y_lagrange, rtol=0, atol=1e-12))
print("矩阵法相对参考值的最大绝对误差：", abs_error.max())
print("矩阵法相对参考值的平均绝对误差：", abs_error.mean())

# 保存每个查询点的两种预测，便于逐项核对。
comparison = np.column_stack([
    query_xs, y_pred, y_lagrange, method_difference, y_reference, abs_error
])
output_path = Path(__file__).parent / "comparison.csv"
np.savetxt(
    output_path, comparison, delimiter=",", fmt="%.17g", comments="",
    header="x,y_matrix,y_lagrange,method_abs_diff,y_reference,abs_error_matrix"
)
print("逐点对照已保存：", output_path.name)
