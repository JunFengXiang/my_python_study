# 数值课程 × Python/NumPy：统一实践入口

更新：2026-10-29。当前每天两小时的实践统一在 my_python_study，路线见[学习指南](../docs/LEARNING_GUIDE.md)，唯一待完成核心练习见[任务卡](../docs/TASKS.md)，本人实际输出与解释记入[学习记录](../docs/LEARNING_LOG.md)。

## 本目录的边界

这里承接数值线性代数、数值分析的学习型小实验：用课程问题练数组、函数、测试、表格和绘图，不额外开启第二条课程编程计划。先自己实现可手算的小例子，再比较参考实现，不能只调用一个函数或复制旧程序就记为掌握。

本次仅新增统一入口并更新路线和任务；**尚未整体复制旧代码，也没有代写新的算法答案。** 不创建空目录或批量脚手架。实际开始相关题目时再按需要创建：

```text
numerical/
  README.md             # 本入口（已建立）
  linear_algebra/       # 以下为计划路径，用到时再建
  numerical_analysis/
```

每个主题起步只需要一个 .py 文件，较长时再拆计算与绘图。不要命名 numpy.py、pandas.py 或 matplotlib.py。结果与临时文件沿用仓库的忽略规则；需要长期保留的小型输出注明生成命令。新增依赖应明确记录，不能假定已有环境可直接运行。

## 现有数值仓库的资料入口

来源仓库：[JunFengXiang/numerical-computing-lab](https://github.com/JunFengXiang/numerical-computing-lab)。2026-10-29读取其README时登记了以下入口；本文没有重新执行或重新验收这些程序，也不把README中的示例结果算作本人的完成证据。

| 课程题材 | 旧资料/代码入口 | 融入Python学习的方式 |
|---|---|---|
| 矩阵与向量、列视角 | [01-matvec/lab.py](https://github.com/JunFengXiang/numerical-computing-lab/blob/main/linear-algebra/01-matvec/lab.py) | 数组形状、索引、矩阵乘法、与循环结果核对 |
| 正交、内积、投影 | [02-orthogonal/lab.py](https://github.com/JunFengXiang/numerical-computing-lab/blob/main/linear-algebra/02-orthogonal/lab.py) | 转置/共轭、向量运算、残差与正交性检查 |
| 两节点插值 | [插值实验说明](https://github.com/JunFengXiang/numerical-computing-lab/blob/main/numerical-analysis/code/ch02_interpolation/lagrange/README.md) | 函数、广播、节点验证、参考值与误差 |
| 数值线性代数后续课件 | [课程目录](https://github.com/JunFengXiang/numerical-computing-lab/blob/main/linear-algebra/README.md)及项目中已上传课件 | 按实际课内进度选范数、QR/SVD、最小二乘、条件数、消元与选主元 |
| 数值分析教材与章节 | [数值分析入口](https://github.com/JunFengXiang/numerical-computing-lab/blob/main/numerical-analysis/README.md) | 按章节选插值、求根、数值积分、差分、ODE及误差分析 |

旧仓库资料不等于此处都已上传；每次使用实际读取对应文件。教材转录需对照原页或校注，不能凭目录编造章节页码。不重复上传整本教材。

## 一次融合实验怎样验收

同一任务只回答一个主要问题，记录：课程来源与必要公式；输入、shape、dtype与参数；本人实现；手算/参考实现或数学恒等式检查；实际输出与误差定义；一句观察及其适用条件。已知解测试中也要区分残差和解误差；浮点结果按问题尺度选择容差，不机械要求完全相等。

数值实验产生的真实小表继续用于pandas的读写、清洗、合并、分组，Matplotlib画误差/收敛/重构曲线。尚未计算的结果只能标为预期或教学模拟，不能写成真实实验。复杂QR/SVD或多种积分、求根算法不要挤在同一个两小时任务里。

已有代码需要引入本仓库时，先读源文件和依赖，保留来源/历史路径，按文件进行非破坏式复制或独立重写并检查；不删除旧文件，不以迁移本身代替学习验收。

## 旧仓库何时重新成为实验主仓库

当前停止给 numerical-computing-lab 安排独立日更、重复作业和重复进度；其原文件与Git历史不动，未执行GitHub的归档操作。

以后获得授权且具备可用的真实AI4水处理数据，再在那里开展字段/单位/时间戳与缺失异常检查、数值和统计基线、模型比较、误差评价及可复现实验。届时从本仓库迁入经过验证的小函数，带上来源commit与测试，而不是搬运全部学习草稿。

现在不假设已有真实工厂数据，不上传公司原始数据或图纸，不启动控制、加药、RL或硬件接入。教学模拟数据不能用于宣称真实工程效果。
