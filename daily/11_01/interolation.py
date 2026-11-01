from pathlib import Path
import numpy as np
import csv
path = Path(__file__).parent/"data"/"nodes.csv"

data = np.loadtxt(path, delimiter = ",", skiprows = 1)#loadtxt把文件中的数值读成numpy数组 delimiter是分隔符，skiprows=1跳过第一行的表头x,y


print("数组形状:",data.shape)
print("元素类型:",data.dtype)

print("前三行:")
print(data[:3])

xs = data[:,0]
ys = data[:,1]
print("横坐标的形状：",xs.shape)
print("函数值的形状：",ys.shape)
print("前三个横坐标：",xs[:3])
print("前三个函数值：",ys[:3])

indices = [0,50,-1]

node_xs = xs[indices]
node_ys = ys[indices]

print("选中的横坐标：", node_xs)
print("对应的函数值：",node_ys)
print("节点数组形状：", node_xs.shape)

query_path = Path(__file__).parent/"data"/"queries.csv"
query_data = np.loadtxt(query_path,delimiter=",",skiprows = 1)
query_xs = query_data[:,0]
y_reference = query_data[:,1]


print("查询数据的形状：",query_data.shape)
print("查询横坐标的形状：", query_xs.shape)
print("前三个查询点：", query_xs[:3])
print("前三个参考值：", y_reference[:3])

#下面用三个节点进行预测
x0,x1,x2 = node_xs
L0 = ((x1 - query_xs)*(x2 - query_xs))/((x1 - x0)*(x2-x0))

print("L0的形状：",L0.shape)
print("前三个L0值：",L0[:3])
L1 = ((x0-query_xs)*(x2-query_xs))/((x0-x1)*(x2-x1))
L2 = ((x1-query_xs)*(x0-query_xs))/((x1-x2)*(x0-x2))

y0, y1, y2 = node_ys

y_pred = y0 * L0 + y1 * L1 + y2 * L2

print("前三个查询点的权重和：", (L0 + L1 + L2)[:3])
print("预测值形状：", y_pred.shape)
print("前三个预测值：", y_pred[:3])


abs_error = np.abs(y_pred - y_reference)

print("前三个绝对误差：", abs_error[:3])
print("最大绝对误差：", abs_error.max())
print("平均绝对误差：", abs_error.mean())