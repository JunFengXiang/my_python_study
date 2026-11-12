"""第 7 讲 QR 分解：把手算结果写成 NumPy 运算。

助手准备输入文件、导入、读取与步骤提示。
学习者填写 Q、R 和矩阵乘法核对；暂不调用 np.linalg.qr。
"""

from pathlib import Path

import numpy as np


path = Path(__file__).parent / "data" / "matrix.csv"
A = np.loadtxt(path, delimiter=",")
print("A:")
print(A)

# 1. 用 np.array 和 np.sqrt 写出刚才手算的 Q。
#    q1、q2 是 Q 的两列；两个向量都要归一化。

# 2. 根据 R = Q^T A，用 NumPy 的转置和矩阵乘法计算 R。

# 3. 打印 Q、R、Q.T @ Q 和 Q @ R，解释后两个结果。
#    实际结果运行后再记录，不能把手算值当作程序输出。
Q = 1/np.sqrt(2)*(np.array([[1,1],[1,-1]]))
print(Q)
R = Q.T @ A
print(Q.T @ Q)
print(Q @ R)
