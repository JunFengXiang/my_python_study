# Lecture 15 OCR 与视觉核验记录

- 原书：Numerical Linear Algebra，Lecture 15 “More on Stability”。
- 原书页码：108--113。
- 目标 PDF 页码：123--128。
- 核验方式：使用 pdftotext -layout 生成候选文本，并将目标 PDF 第 123--128 页以 150 dpi 渲染，逐页比对浮点运算符、减法后向稳定推导、例 15.1--15.4、特征多项式反例、定理 15.1、式 (15.1)--(15.2) 和习题。OCR 无法可靠恢复的波浪号、共轭转置、平方根阶和 $10^{-14}$ 扰动，以原页视觉结果为准。

## 重点纠正的 OCR 风险

1. 减法算法是 $\widetilde f(x_1,x_2)=\operatorname{fl}(x_1)\ominus\operatorname{fl}(x_2)$；先对两个输入舍入，再执行浮点减法。由三次舍入误差得到 $\widetilde f(x)=\widetilde x_1-\widetilde x_2$，且两个输入分别只有 $O(\varepsilon_{\mathrm{machine}})$ 的相对扰动。
2. 展开乘积时，$\epsilon_4,\epsilon_5$ 满足 $|\epsilon_4|,|\epsilon_5|\le2\varepsilon_{\mathrm{machine}}+O(\varepsilon_{\mathrm{machine}}^2)$，不能把二阶项误删成改变阶数的结论。
3. 例 15.1 的内积使用逐项 $\otimes$ 与累加 $\oplus$；例 15.2 的外积 $\widetilde A$ 一般不再恰好秩一，因此算法稳定但不后向稳定；例 15.3 的 $x+1$ 在 $x\approx0$ 时只有绝对误差控制，后向相对扰动会失控。
4. 例 15.4 取 $x=\pi/2-\delta$、$0<\delta\ll1$，此时 $f'(x)=\cos x\approx\delta$，后向误差为 $O(\varepsilon_{\mathrm{machine}}/\delta)$，所以不能是 $O(\varepsilon_{\mathrm{machine}})$。
5. 特征多项式求特征值的算法是“先求特征多项式系数，再求根”；它既后向不稳定也不稳定。$A=I$ 时 $p(x)=x^2-2x+1$，$O(\varepsilon_{\mathrm{machine}})$ 的系数误差会造成 $O(\sqrt{\varepsilon_{\mathrm{machine}}})$ 的根误差；$\varepsilon_{\mathrm{machine}}=10^{-16}$ 时约损失 8 位数字。源页建议用 $\operatorname{diag}(1+10^{-14},1)$ 的扰动矩阵做实验，以避免整数系数被精确表示掩盖现象。
6. 定理 15.1 的结论是后向稳定算法的相对误差 $O(\kappa(x)\varepsilon_{\mathrm{machine}})$；证明由后向稳定性和第 12 讲相对条件数定义组合得到，式 (15.2) 中保留 $\kappa(x)+o(1)$。
7. 习题 15.1 的 (c) 是数据 $x\in\mathbb C\setminus\{0\}$、解 1、计算 $x\oslash x$；(e)、(f) 比较从左到右和从右到左求和 $e$ 的级数；(g) 在 $[3,4]$ 中搜索最小浮点数 $x$，满足 $s(x)\otimes s(x')<0$。
8. 习题 15.2 讨论完整显式 SVD $A=U\Sigma V^*$，明确 $U,V$ 不是反射器乘积的隐式表示；要求分别解释后向稳定为何不可能，以及标准 SVD 算法的稳定性含义。

## 图形资产

- 本讲原书页 108--113 没有插图或需要保留的图形资产，因此未新增 assets 文件。
- 本讲没有调用 Matplotlib；若后续讲次出现无法可靠提取的图，绘图脚本只放在 /tmp 等临时目录，工作区只保存最终 PNG/SVG。

## 译文验收范围

- 已覆盖 Lecture 15 导言、浮点四则运算稳定性、减法后向稳定证明、例 15.1--15.4、特征多项式不稳定算法、定理 15.1、后向误差分析和习题 15.1--15.2。
- 已从读者视角补充了“稳定但不后向稳定”的差别，以及条件数如何把后向误差转化为前向准确度，但保留原书例子、证明和习题，不擅自补写答案。
- latex/l15.tex 已独立 XeLaTeX 编译两遍，并渲染检查 6 页；无插图，公式、矩阵反例、定理证明和习题页面已逐页检查。
