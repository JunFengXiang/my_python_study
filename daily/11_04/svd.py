from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

path = Path(__file__).parent/"data"/"matrix.csv"

A = np.loadtxt(path, delimiter = ",",skiprows = 1)

print("矩阵 A:")
print(A)
print("A的形状：", A.shape)

U, s , Vt = np.linalg.svd(A)
print("U:")
print(U)
print("奇异值 s:")
print(s)
print("Vt:")
print(Vt)
print("三个对象的形状：",U.shape, s.shape,Vt.shape)


Sigma = np.diag(s)
print("Sigma:")

print(Sigma)

A_rebuilt = U @Sigma @Vt

print(A_rebuilt)

print("最大元素误差：")
print(np.abs(A_rebuilt - A).max())

#下面考虑秩1近似

sigma1 = s[0]
u1 = U[:, 0]#代入第1列
v1t = Vt[0, :]

A_rank1 = sigma1 * np.outer(u1 , v1t)

print("秩一近似矩阵：")
print(A_rank1)
print("秩一近似的最大元素误差：")
print(np.abs(A_rank1 - A).max())

#画图
theta = np.linspace(0, 2 * np.pi, 100)

circle = np.array([
    np.cos(theta),
    np.sin(theta)
])

print("圆上点的数组形状：", circle.shape)

ellipse = A @ circle
print("变换后的形状：", ellipse.shape)

plt.plot(circle[0, :], circle[1, :], label="Unit circle")
plt.plot(ellipse[0, :], ellipse[1, :], label="A @ circle")

plt.axis("equal")
plt.legend()
plt.grid(True)

plt.savefig(Path(__file__).parent / "svd_geometry.png", dpi=150)
plt.show()