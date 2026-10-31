from pathlib import Path
import csv
path = Path(__file__).parent/"data"/"nodes.csv"
xs = []
ys = []

with path.open(encoding = "utf-8",newline = "") as file:
    reader = csv.DictReader(file)

    for row in reader:
        xs.append(float(row["x"]))
        ys.append(float(row["y"]))
print("节点数量: ", len(xs))
print("第一个节点:",(xs[0],ys[0]))
print("最后一个节点:",(xs[-1],ys[-1]))

x0, y0 = xs[0], ys[0]
x1, y1 = xs[-1], ys[-1]

x = 0.5

#利用这两点做lagrange插值
L0 = (x - x1)/(x0-x1)
L1 = (x-x0)/(x1-x0)
y_pred = y0*L0+y1*L1

print("两个权重：", L0, L1)
print("预测值：", y_pred)


x0, y0 = xs[0], ys[0]
x1, y1 = xs[50], ys[50]
x2, y2 = xs[-1], ys[-1]

L0 = ((x-x1)*(x-x2))/((x1-x0)*(x2-x0))
L1 = ((x-x0)*(x-x2))/((x0-x1)*(x2-x1))
L2 = ((x-x1)*(x-x0))/((x0-x2)*(x1-x2))

y_pred2 = y0*L0+y1*L1+y2*L2
print("三个权重：",L0, L1, L2)
print("预测值：",y_pred2)

#循环格式

n = int(input("请输入节点个数："))
if not 2 <= n <= len(xs):
    raise ValueError(f"节点个数应该在 2 到{len(xs)} 之间")

node_xs = []
node_ys = []

for i in range(n):
    index = round(i * (len(xs)-1)/(n-1))
    node_xs.append(xs[index])
    node_ys.append(ys[index])

print("选中的横坐标：",node_xs)
print("选中的函数值：",node_ys)
