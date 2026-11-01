from pathlib import Path
import csv
import math
path = Path(__file__).parent / "data"/"nodes.csv"
nodes = []
queries_nodes = []
with path.open(encoding = "utf-8",newline="")as file:#newline = ""让文件读取保留原来的换行字符，再交给csv按CSV的规则解析
    reader = csv.DictReader(file)#把file这个csv文件的第一行当作列
    for row in reader:
        x = float(row['x'])
        y = float(row["y"])
        nodes.append({"x":x,"y":y})#j将每一个节点（x，y）作为元素
        print(x,y,type(x))

print(nodes)

x0 = nodes[0]["x"]
y0 = nodes[0]["y"]

x1 = nodes[1]["x"]
y1 = nodes[1]["y"]

print(f"第一个节点:({x0},{y0})")
print(f"第二个节点:({x1},{y1})")

def linear_interpolate(x0,y0,x1,y1,x):
    if x0 == x1:
        raise ValueError("两个节点的横坐标不能相同")

    k = (y1-y0)/(x1-x0)
    y_pred = y0+k*(x-x0)
    return y_pred

result = linear_interpolate(x0,y0,x1,y1,0.5)
print(result)
print(linear_interpolate(1, 2, 3, 4, 2))


query_path = Path(__file__).parent/"data"/"queries.csv"
with query_path.open(encoding = "utf-8",newline="")as file:
    reader = csv.DictReader(file)
    for row in reader:
        x = float(row['x'])
        y_reference = float(row['y_reference'])
        queries_nodes.append({"x":x,"y":y_reference})


        y_pred = linear_interpolate(x0,y0,x1,y1,x)
        loss = abs(y_pred - y_reference)

        print(f"x={x},预测值={y_pred},参考值 = {y_reference},误差 = {loss}")
