name = "zhangsan"
age = 22
city = "beijing"
hobby = "数据分析"
temperature = 36.5
info = f'''{'='*30}
        个人信息卡片
{'='*30}
姓名: {name}
年龄: {age}岁
城市: {city}
爱好: {hobby}
体温: {temperature}
{'='*30}
'''
#f"""……"""三引号支持多行格式化字符串
#如果"""改成'''唯一的区别是：如果字符串内容里包含双引号就用三单引号包裹，包含单引号就用三双引 号包裹，避免转义。没有引号冲突时随便选哪个都行。
#
print(info)

#2、圆的面积和周长计算
radius = 5.0
pi = 3.1415926
area = pi*radius**2
circumference = 2*pi*radius
print(f"半径为{radius}的圆:")
print(f"面积 = {area:.2f}")
print(f"周长 = {circumference:.2f}")
print()

#3、温度转换
celsius = 25
fahrenheit = celsius*9/5+32
print(f"{celsius}°C = {fahrenheit}°F")
#option+shift+8 = °

#4、反向转换
f = 98.6
c = (f-32)*5/9
print(f"{f}°F = {c}°C")

#字符串拼接练习
name = "Python"
version = 3.12
#方法1:+拼接
print("我正在学习"+name+"版本"+str(version))

#方法2: %格式化
print("我正在学习%s版本%.2f"%(name,version))

#方法3:f - string
print(f"我正在学习{name}版本{version}")
print()