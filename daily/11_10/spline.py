"""教材第 24 题（2）：自然三次样条。

助手仅准备导入、输入路径和步骤提示；读取与核心计算由学习者逐步填写。
"""

from pathlib import Path

import numpy as np

import matplotlib.pyplot as plt


path = Path(__file__).parent / "data" / "nodes.csv"

# 第一步：用 np.loadtxt 读取 CSV 的数值部分，命名为 data。
# 提取第 0 列为 x、第 1 列为 y，打印数据和三个数组的形状。

# 第二步：由相邻节点计算 h 和 k，并与手算结果对照。

# 后续：组装 A、rhs → 求 M → 计算 b、c、d → 分段求值、绘图、检查。

data = np.loadtxt(path, delimiter = ",",skiprows = 1)

x,y = data[:,0],data[:,1]
print("x:",x)
print("y:",y)
print("data.shape:",data.shape," x.shape:",x.shape," y.shape:",y.shape)


#考虑用切片一次计算所有区间
h = x[1:] - x[:-1]

k = (y[1:]-y[:-1])/h
print("h:", h)
print("k:", k)
print("h.shape:", h.shape, "k.shape:", k.shape)
A = np.array([
    [2 * (h[0] + h[1]), h[1], 0],
    [h[1], 2 * (h[1] + h[2]), h[2]],
    [0, h[2], 2 * (h[2] + h[3])]
])


rhs = 6*(np.array(k[1:]-k[:-1]))

print("A:")
print(A)
print("rhs:", rhs)
print("A.shape:", A.shape, "rhs.shape:", rhs.shape)


#求解A@M_inner = rhs
M_inner = np.linalg.solve(A,rhs)
print("内部节点的二阶导数:", M_inner)

M = np.zeros(len(x))
M[1:-1] = M_inner
b = k - h * (2 * M[:-1] + M[1:]) / 6

c = M[:-1]/2
d = (M[1:]-M[:-1])/(6*h)

print("b:", b)
print("c:", c)
print("d:", d)

x_query = 0.275
i = 0                   # 位于第 0 段：[0.25, 0.30]
t = x_query - x[i]

s_value = y[i] + b[i] * t + c[i] * t**2 + d[i] * t**3

print("查询点:", x_query)
print("样条值:", s_value)


#画图
plt.figure(figsize=(7, 4))

for i in range(len(h)):
    # 在第 i 段内取 100 个查询点
    xs = np.linspace(x[i], x[i + 1], 100)
    t = xs - x[i]

    # 与刚才单点求值的公式相同
    ys = y[i] + b[i] * t + c[i] * t**2 + d[i] * t**3

    plt.plot(xs, ys, label=f"segment {i}")

# 标出教材给定的五个节点
plt.scatter(x, y, color="black", zorder=3, label="nodes")

plt.xlabel("x")
plt.ylabel("S(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(Path(__file__).parent / "spline.png", dpi=150)
plt.show()