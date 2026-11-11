# 2026-11-11｜LA02-projection + NA02-approximation
## 当前依据
以 main b5cca1c 的11月11日学习指南、TASKS与日志为准：数值代数、数值分析每天各约60分钟，Python按需支持。本卡只落实今天两科输入与验收；不修改提醒时间或schedule。
11月10日五节点样条在指导下完成，代码、输出及助手核验见[实际记录](https://github.com/JunFengXiang/my_python_study/blob/main/daily/11_10/README.md)。S(0.275)=0.524143679608773是已保存输出；独立解释待验收，不再重布置三节点题。本次读源码和输出，未重跑学生代码。当天新增两科任务尚未完成。

## 一个连接目标：看清近似结果取决于怎样衡量误差
### 数值代数60分钟：向直线正交投影
- 10分钟读[Trefethen第6讲](https://github.com/JunFengXiang/my_python_study/blob/main/local_books/numerical-linear-algebra/textbook.md#lecture-6)“正交投影算子”和式(6.8)—(6.10)。
- 35分钟先手算v到span(a)的投影p与残差r，再本人从[data/linear_algebra/projection-v1/vectors.csv](../../data/linear_algebra/projection-v1/vectors.csv)读取并以NumPy核对。CSV列a,v，行表示向量分量，a=(1,0,1)，v=(1,2,3)。自拟确定性教学数据projection-v1，无seed、无物理单位、非教材原题。建议 numerical/projection.py；核心自己组织，不提供完整实现。
- 15分钟检查a/v/p/r形状(3,)，P形状(3,3)；a与r内积、P@P-P、P.T-P的最大绝对残差≤1e-12，rtol=0。记录p+r=v，并解释正交投影为什么通常不是正交矩阵。

### 数值分析60分钟：同一函数的两种误差
- 10分钟回顾已写样条中M为何5项、c为何4项；10分钟读[3.1.1的式(3.1.2)—(3.1.3)](https://github.com/JunFengXiang/my_python_study/blob/main/local_books/numerical-analysis/verified/sections/3.1.md#311-问题的提出)。
- 30分钟手算自拟练习：在[0,1]上，用常数c=0、1/3、1/2近似f(x)=x²；逐一计算最大绝对误差E∞与平方积分J=积分(x²-c)²dx，再写E2=sqrt(J)。本题是解析手算，无网格/随机数，不冒充教材例题。比较两个度量各自选哪个常数，不必今天证明一般最佳逼近定理。
- 10分钟独立检查端点与内部可能极值、积分非负；解释J和E2为何不是同一个数。数学参考来自明确函数与解析积分，不用样条未知母函数制造真解误差。

## 输出、保底、进阶
拟保存 results/projection-v1/run_output.txt 与 results/approximation-v1/notes.md；只有实际运行/手算后才产生。两科分别交代码或列式、真实输出、耗时、是否依赖示例及一句解释。提前完成可收尾，总预算120分钟；已在别处学过的时间从相应60分钟扣除。
保底30分钟：两科各15分钟，代数只手算p与a·r，分析只算c=0的两种误差；标部分完成，不挤掉另一科。
唯一进阶（从余量取）：将a换成2a，预测并检查投影是否改变，不增加新数据文件或另一主题。
卡住20分钟先检查向量形状或展开一个积分，保留另一科时间。

## 同步边界与历史
仅教学输入与任务说明；学生核心代码未代写。main已有11月10日验证经验，本次不重复追加LEARNING_LOG。PR #3学习分支落后main，历史旧卡不是当前进度；此卡明确使用main最新依据，不复制学生答案。未自动合并、未运行全仓测试，无CI通过声明。
[旧样条卡](NA01-natural-spline.md)仅作历史；[当前主线](https://github.com/JunFengXiang/my_python_study/blob/main/docs/DAILY_PLAN.md)。
