# 当前任务入口｜2026-11-12

北京时间 2026-11-12；原日历 Day 17，仅用于日期定位。阶段：数值代数与数值分析；稳定 ID：LA03-qr-solve / NA03-orthonormal-coordinates。依据 [main 最新指南](https://github.com/JunFengXiang/my_python_study/blob/main/docs/LEARNING_GUIDE.md)记录的 11 月 11 日用户调整，两科同步、每天合计最多 120 分钟；本次不修改任何提醒或 schedule。

## 进度依据与本次边界

[11 月 11—12 日学习总结](https://github.com/JunFengXiang/my_python_study/blob/main/daily/11_11/README.md)已记录：本人完成 2×2 QR 手算、填写核对代码和真实输出，讨论约化/完整 Q；数值分析已做最佳常数和函数内积练习。最后换基系数经助手纠正，尚需独立复核。3×2 QR 只有口头判断，未标为本人代码完成。
[第三章作业](https://github.com/JunFengXiang/my_python_study/blob/main/numerical/numerical_analysis/ch03_approximation/README.md)是已准备的助手参考材料，不代表本人完成整章。

本轮核心已可收尾，实际耗时未知。**先扣除今天已用时间；若已学满，今天只记录停点，下面留到下一次学习，不另加 120 分钟。** 新任务均为安排，未声明本人已运行或通过。

## 一个目标：独立用正交坐标计算，并还原检查

1. **数值代数（最多 60 分钟）：QR 求解。** 精读 [Trefethen 第 7 讲](https://github.com/JunFengXiang/my_python_study/blob/main/local_books/numerical-linear-algebra/textbook.md#lecture-7)的定理 7.2 与式 (7.13)：满列秩、R 正对角时约化 QR 唯一；Q 某列与 R 对应行同时变号不改变 QR。复用下述文件矩阵及本人已有 Q，计算 R=QᵀA、Qᵀb，自己写两步回代求解 Rx=Qᵀb，再检查 Ax−b。参考分配：读 10、手算/编码 35、验证 15 分钟。
2. **数值分析（最多 60 分钟）：换基复核。** 在 [-1,1]、权重 1 上，对 f(x)=2−3x 和 q₀=1/√2、q₁=√(3/2)x，自行用积分内积求两个系数，再展开还原 f；不要抄上轮纠正后的答案。精读 [数值分析 §3.1.3 连续函数空间与范数](https://github.com/JunFengXiang/my_python_study/blob/main/local_books/numerical-analysis/verified/sections/3.1.md)，结合上轮笔记写清平方积分 J 与 L² 范数 √J 的区别。参考分配：读/回顾 10、独立手算 35、核验/记录 15 分钟。
3. **验收与记录包含在上述时间内。** QR 保存真实 Qᵀb、R、解向量及 max(abs(Ax−b))，目标不超过 1e-12；函数展开的常数项与 x 系数须分别还原为 2、−3。各用一句话解释“QR 为什么允许同时变号”和“标准正交基系数如何检验”。附代码、真实输出或手算，以及两科各自耗时、卡点、是否依赖完整答案。没有运行就写待验证。

## 输入与输出

- 已入库输入：[daily/11_11/data/matrix.csv](https://github.com/JunFengXiang/my_python_study/blob/main/daily/11_11/data/matrix.csv)，无表头、两行两列，内容为 `1,3` / `1,1`，即 A=[[1,3],[1,1]]。来源为自拟确定性教学示例，不含随机过程。该文件在 main；本学习分支未复制学生材料，请从链接确认本机已有输入，不假设切换分支后自动存在。
- 新右端项版本 qr-solve-v1：请首次手动保存下列内容到 `data/linear_algebra/qr-solve-v1/rhs.csv`，之后从文件读，跳过表头。单列 b、两行值；自拟教学向量，无 seed。**本次仅提供内容，CSV 尚未创建或提交；若本机已有同名文件，先核对，不覆盖。**

```csv
b
5
1
```

- 数值分析为明确给定的解析函数手算，无采样 CSV；参考由展开恒等式与解析积分核验，不虚构程序结果。
- 拟新增自己的程序 `numerical/qr_solve.py`（若已有同名程序先复用），真实运行时才保存 `results/qr-solve-v1/<本次运行标识>/output.txt`。两科解释与耗时记在该结果目录的 `notes.md`；这些输出目前均未生成。保留原 `daily/11_11/qr.py` 和原输出。

**唯一进阶：**核心提前通过，再将函数改为 1+2x，独立算新基坐标并展开核对，仍计入本科 60 分钟。
**30 分钟保底：**代数 15 分钟只完成 Qᵀb 与回代手算；分析 15 分钟只复核 2−3x 的两个系数并展开。未做代码验证明确保留。卡住约 20 分钟先检查中间量，再请求分层提示。

## 同步与历史

本次只维护本任务文件，使用现有学习分支 `study/mac-data-analysis-batch02` / [草稿 PR #3](https://github.com/JunFengXiang/my_python_study/pull/3)。PR #1 已合并，不重开。写前核对 main 为 `efd0d51`、学习分支为 `a903225`；两者存在未合并差异，PR 报告冲突，不自动合并或改写学生答案。本次为纯文档，未重跑学生程序或全仓测试，无新增 CI 通过声明。
真实经验已见 [main 学习日志](https://github.com/JunFengXiang/my_python_study/blob/main/docs/LEARNING_LOG.md)，本次不重复追加。

以下内容原样保留作历史索引，其中“当前/今天/待完成”只表示当时状态，不覆盖上方安排。

---

# 当前任务入口｜2026-11-11
今天执行[LA02投影与NA02函数逼近](tasks/LA02-NA02-projection-approximation.md)，数值代数与数值分析各约60分钟，总计120分钟。输入、阅读、验收、保底与进阶均在新卡。
依据[main最新学习指南](https://github.com/JunFengXiang/my_python_study/blob/main/docs/LEARNING_GUIDE.md)的11月11日调整；本分支旧指南与旧逐日表只作历史，不能覆盖新安排。
五节点样条已在指导下完成，实际证据见[11月10日记录](https://github.com/JunFengXiang/my_python_study/blob/main/daily/11_10/README.md)；本人独立理解另验。新任务仅材料准备，不是已完成。
学习分支保留历史与未合并差异，不自动合并main；本次不重复追加经验。
历史索引：[样条](tasks/NA01-natural-spline.md)、[SVD](tasks/LA01-svd-reconstruction.md)。下方原矩阵卡原样保留，其中“当前/待完成/今天”均为历史语境。

---

# 当前任务：11月2日完成三节点矩阵求解与插值对照

2026-11-02，日历 **Day 7/50**；稳定任务ID **NP05-matrix-interpolation**；MacBook CPU，最多120分钟。**状态：待完成，不是完成记录。**

## 从今天的实际成果接续

11月1日已在指导下完成 NumPy 读取、数组形状与切片、三节点选取、99个查询点的Lagrange批量预测及终端误差统计；详见[今日笔记](../daily/11_01/学习知识点.md)和[实际输出](../daily/11_01/run_output.txt)。最大绝对误差0.014187438922776963，平均0.008734737850859027。

本人按步骤编写并提供了部分运行输出；助手复跑与不变量检查通过。这些证据不等于已经独立掌握所有NumPy操作。通用Lagrange、Newton、绘图、函数封装和逐点CSV导出仍待完成。

用户明确将三节点线性方程组求解移到11月2日。本任务替换旧逐日表的广播大练习，不叠加为额外负担。

## 唯一核心目标

将同一个三点插值多项式写成 `p(x)=a0+a1*x+a2*x**2`，从三个节点列出3×3线性方程组，用 `np.linalg.solve` 求系数，再对99个查询点计算并与Lagrange对照。

## 现有输入

- [nodes.csv](../daily/11_01/data/nodes.csv)：100个 `exp(x)` 候选节点，取原下标0、50、99；中间横坐标是50/99，不是0.5。
- [queries.csv](../daily/11_01/data/queries.csv)：99个查询及对应参考值；参考列只用于评估。
- [已有程序](../daily/11_01/interolation.py)：沿用本人实际文件和公式。输入不覆盖；不混用备用的x²三节点文件。
- 本人拟新增 `numerical/interpolation_matrix.py`（已有本地等价文件可沿用），从仓库内上述CSV读取，不依赖工作目录或Notebook旧变量。拟输出 `results/11_02/matrix_comparison.csv`，列为x,y_lagrange,y_matrix,y_reference,implementation_gap,abs_error；99行，输出目前待生成。先完成终端核对，导出遇阻可记录卡点，不追加时长。
- 输入来源：exp01-100-v1，exp(x)在[0,1]上的无噪声教学数据；候选节点x_i=i/99，查询q_i=(i+0.5)/99，无随机数。参考值由math.exp生成，来源说明见[原manifest](../daily/10_31/data/manifest.json)。不得把100个候选节点全部传入三系数系统。

## 精读与接口提示
只读[数据分析4.6](../local_books/python-data-analysis/chapters/04.md)开头的矩阵乘法、二维乘一维示例（不读求逆/QR示例）；以及[NumPy solve官方文档](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)的Parameters、Returns、Raises。
今日约定A为(3,3)，b与系数为(3,)，查询设计矩阵Q为(99,3)。按未知量顺序a0,a1,a2，自己从三个方程组织A；用solve求解，不先算逆矩阵。接口建议 `fit_quadratic(node_xs, node_ys)` 返回三个系数，`predict_quadratic(coeffs, query_xs)` 返回(99,)。
提示：先写出一个节点对应的一行，再复制这一规律；卡住20分钟先核对A的一行与手写方程，检查右端是否误用了查询参考值。

## 建议的120分钟

1. **25分钟：回顾、精读与预测。** 写出三个方程，说明系数矩阵每一行及未知量顺序，预测矩阵和向量的shape。
2. **65分钟：本人编码。** 构造系数矩阵和右端向量，用 `solve` 求系数；通过多项式表达式或查询矩阵与系数的 `@` 运算批量预测。
3. **20分钟：验证。** 检查节点再现；在同一查询网格比较两个实现；分别报告实现一致性误差与相对参考值的误差。
4. **10分钟：记录。** 记录代码、实际输出、用时及是否借助完整答案。进阶从提前完成的余量里取，不增加预算。

验收：三个节点再现误差及两种实现预测的最大差异针对本组小数据应不超过1e-12；形状和输入对应清楚。若失败先打印中间量，不修改输入参考值来迎合结果。能解释相同节点确定同一个二次多项式，而两种表达形式不同。

**最少证据：**代码或commit，A/b/系数/Q的shape、节点残差、两个实现最大差异、相对参考的最大误差；两句解释“为什么两种方法应一致”“为什么一致不代表与exp(x)完全相同”。

**15—30分钟保底：**读三个节点，独立构造A与b，完成solve并输出节点残差；99点预测下次接着做。

**今日唯一进阶：**同时交换A与b的前两行再求解，检查系数是否保持一致，解释为何只换A不换b会改变问题。

## Trefethen：后续入口（今日不叠加）

用户自学到SVD，学校讲到第22讲。教材[目录](../local_books/numerical-linear-algebra/INDEX.md)确认：第4–5讲是SVD，第22讲是高斯消去法的稳定性。

矩阵求解桥接通过后，下一次可开始一个小矩阵的SVD重构与秩一近似，按需补 `@`、转置和范数，不等待pandas或整套Python。该桥接实验依据第4–5讲，不冒称原书原题。后续选[第4讲习题4.3](../local_books/numerical-linear-algebra/textbook.md#lecture-4)的单位圆到椭圆程序，明确标注为原题的Python改写。新实验的矩阵CSV在开始时单独准备并注明来源，今天尚未创建。

之后按“QR与最小二乘 → 条件数、残差与解误差 → 消去、选主元与稳定性”衔接第7、11、12–14、20–22讲；四个主题单元不等于承诺四天掌握全部理论。

## 收尾规则与历史

本次自动执行按用户当前明确边界：仅学习分支与草稿PR，不自动合并main。PR #1已于11月1日合并；当前main为f518d5d700588187d445c555e67600bf36e3f0f6，旧学习分支无领先提交。本批新建study/mac-data-analysis-batch02承接main；保留旧分支和本人笔记中的历史收尾约定，不改写学生内容。实际输出和本人解释分别记录，未完成内容保持待办。

11月2日复核：助手Python 3.12.14 / NumPy 2.3.5复跑原interolation.py，终端输出与已提交run_output.txt逐字一致；预测/参考/查询/误差均为(99,)且有限，权重和最大偏差2.22e-16。此为既有批量程序验证，不是矩阵练习已完成。仓库Actions仍无运行记录，未跑全仓测试。

- [11月2日补充前的任务卡](https://github.com/JunFengXiang/my_python_study/blob/f518d5d700588187d445c555e67600bf36e3f0f6/docs/TASKS.md)
- [11月1日原任务卡](https://github.com/JunFengXiang/my_python_study/blob/004d2b492ef123c3c3b46d175454cba2f1ed94d9/docs/TASKS.md)
- [50天逐日计划](DAILY_PLAN.md)保持原周期与结项日期；广播、其他插值方法按实际缺口补齐。
