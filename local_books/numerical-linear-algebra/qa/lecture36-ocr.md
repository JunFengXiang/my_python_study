# 第 36 讲 OCR、插图与版面核验记录

## 范围

- 原书页：276–284。
- 目标 PDF 页：291–299。
- 处理对象：第 36 讲“Lanczos 迭代”。
- 中文正文：translation/textbook.md。
- 独立 LaTeX：translation/latex/l36.tex。
- 最终插图：
  - translation/assets/figure-36-lanczos-polynomial.png
  - translation/assets/figure-36-ritz-convergence.png
  - translation/assets/figure-36-ghost-eigenvalues.png

## 处理方法

1. 使用 pdftotext 提取候选文本，并对目标 PDF 页 291–299 的 9 个源页逐页渲染、逐页核对正文、公式、算法框、图示和习题。
2. OCR 对 Hermitian、Hessenberg、三对角矩阵、$\alpha_n$、$\beta_n$、$q_{n-1}$、$\widetilde T_n$、$\mathcal P^n$ 和特征值重数有明显混淆；所有下标、矩阵维数、转置、范数和 Chebyshev 点的端点间距均回看原页核对。
3. 图 36.1、36.2、36.3 均从高分辨率源页裁切为最终 PNG，去除页眉和原文英文图注；中文图注在 Markdown/LaTeX 中重写。三幅图均可直接从源页提取，本讲没有需要用 Matplotlib 重绘的图；裁切辅助只在 /tmp 中进行，工作区不保存绘图脚本。
4. l36.tex 使用 XeLaTeX 编译两遍，输出到 /tmp/l36-build/l36.pdf；最终 PDF 共 8 页，日志没有 Error、Undefined、Overfull、Underfull、Warning 或 Missing character。最终渲染页 1–8 已回看，重点检查三幅插图、算法 36.1、定理 36.1、式（36.4）–（36.10）和习题分页。

## 重点 OCR 与数学核对

- 核对 Arnoldi 在实对称情形下的化简：$H_n$ 同时为对称矩阵和 Hessenberg 矩阵，因此为三对角矩阵；相应递推由多项变为三项。
- 核对
  \[
  h_{ij}=q_i^TAq_j,
  \qquad h_{ij}=q_j^TA^Tq_i,
  \]
  以及 $\alpha_n=h_{nn}$、$\beta_n=h_{n+1,n}=h_{n,n+1}$ 和三对角矩阵 $T_n$ 的记号。
- 算法 36.1 的直接写法核对为
  \[
  v=Aq_n,\quad \alpha_n=q_n^Tv,\quad
  v\leftarrow v-\beta_{n-1}q_{n-1}-\alpha_nq_n,
  \quad \beta_n=\lVert v\rVert.
  \]
  原书算法框在第一行给出“为提高稳定性也可使用 $Aq_n-\beta_{n-1}q_{n-1}$”的括号说明；若采用这一稳定写法，后续更新只能再减去 $\alpha_nq_n$，不能再次减去 $\beta_{n-1}q_{n-1}$。译稿在 Markdown、LaTeX 和本记录中明确展开这一点，以避免机械照排造成重复减法。
- 核对定理 36.1：$K_n=Q_nR_n$、$T_n=Q_n^TAQ_n$、$AQ_n=Q_{n+1}\widetilde T_n$，以及
  \[
  Aq_n=\beta_{n-1}q_{n-1}+\alpha_nq_n+\beta_nq_{n+1}.
  \]
  原书式（36.8）将“达到最小值”排在公式末尾；译稿保留其原书表达，不擅自添加未在原页显示的下标。
- 核对 Chebyshev 点
  \[
  x_j=\cos\theta_j,\qquad
  \theta_j=\frac{(j-\tfrac12)\pi}{m},\qquad 1\leq j\leq m,
  \]
  以及内部间距 $O(m^{-1})$、端点附近间距 $O(m^{-2})$ 和平衡电荷密度 $(1-x^2)^{-1/2}$。
- 例 36.1 核对
  \[
  A=\operatorname{diag}(0,.01,.02,\ldots,1.99,2,2.5,3.0),
  \]
  其维数为 $203\times203$；第 9 步最大三个 Ritz 值约为 $1.93,2.48,2.999962$，第 20 步约为 $1.9906,2.499999999987,3.00000000000000$。
- 核对舍入误差部分：图 36.3 中 3.0 的额外 Ritz 值约在第 30、60、90 步出现，2.5 的额外副本约在第 40、80 步出现；这些“幽灵”特征值不代表矩阵中真实的特征值重数增加。
- 习题 36.1–36.4 全部保留。习题 36.3 的对角元原页为 $a_{ii}=\sqrt{i}$；该处 OCR 容易误读为其他函数，已按源页纠正。

## 插图核验

- 图 36.1 保留第 9 步 Lanczos 多项式、Ritz 值根、横坐标 $0,2,2.5,3$ 及 $[0,2]\cup\{2.5\}\cup\{3.0\}$ 的语义；中文图注说明多项式在谱上很小以及离群值附近的根。
- 图 36.2 保留前 20 步 Ritz 值的逐步散点/连线、横坐标 $n$、纵坐标特征值以及 $[0,2]$、$2.5$、$3.0$ 的收敛结构；连线在译稿图注中注明仅用于追踪变化。
- 图 36.3 保留延续到 120 步的 Ritz 值轨迹、图中重数标记和纵轴特征值；最终裁切包含完整的“step number n”横轴标识，中文图注解释幽灵特征值现象。

## 结论

第 36 讲已完成中文翻译、读者视角文字整理、公式/算法重建、3 幅插图保留，以及 LaTeX/Markdown 双版本同步。下一待处理范围为第 37–40 讲及附录、注释、参考文献和索引。
