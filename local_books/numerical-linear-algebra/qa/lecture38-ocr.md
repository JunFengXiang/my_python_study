# 第 38 讲 OCR、插图与版面核验记录

## 范围

- 原书页：293–302。
- 目标 PDF 页：308–317。
- 处理对象：第 38 讲“共轭梯度法”。
- 中文正文：translation/textbook.md。
- 独立 LaTeX：translation/latex/l38.tex。
- 最终插图：
  - translation/assets/figure-38-cg-convergence.png

## 处理方法

1. 使用 pdftotext 提取候选文本，并对目标 PDF 页 308–317 的 10 个源页逐页渲染、逐页核对正文、公式、算法框、图示和习题。
2. OCR 对 $x_\ast$、$\mathcal K_n$、$e_n$、$A$-范数、转置、$\alpha_n$、$\beta_n$、$\kappa$、$\lambda_{\min/\max}$ 和 Chebyshev 上界有明显混淆；所有下标、分母、矩阵正定条件和不等式方向均回看原页核对。
3. 图 38.1 从目标 PDF 第 316 页（原书第 301 页）高分辨率裁切为最终 PNG，保留坐标轴、对数刻度、四条 $\tau$ 曲线和曲线标签，去除英文图注；中文图注在 Markdown/LaTeX 中重写。裁切只在 /tmp 中进行，工作区不保存绘图脚本。
4. l38.tex 使用 XeLaTeX 编译两遍，输出到 /tmp/l38-build/l38.pdf；最终 PDF 共 10 页，日志没有 Error、Undefined、Overfull、Underfull、Warning 或 Missing character。最终渲染页 1–10 已回看，重点检查算法 38.1、定理 38.1–38.5、图 38.1、式（38.1）–（38.11）和习题分页。

## 重点 OCR 与数学核对

- 核对 Krylov 子空间
  \[
  \mathcal K_n=\operatorname{span}\{b,Ab,\ldots,A^{n-1}b\}
  \]
  以及残量 $r_n=b-Ax_n$。
- 核对 $A$ 正定的条件：$x^TAx>0$ 对所有非零 $x$ 成立；$A$-范数为
  \[
  \lVert x\rVert_A=\sqrt{x^TAx}.
  \]
- 算法 38.1 核对为
  \[
  \alpha_n=\frac{r_{n-1}^Tr_{n-1}}{p_{n-1}^TAp_{n-1}},\quad
  x_n=x_{n-1}+\alpha_np_{n-1},\quad
  r_n=r_{n-1}-\alpha_nAp_{n-1},
  \]
  \[
  \beta_n=\frac{r_n^Tr_n}{r_{n-1}^Tr_{n-1}},\qquad
  p_n=r_n+\beta_np_{n-1}.
  \]
  图示源页中 $A p_{n-1}$ 虽在算法说明中出现两次，但每步只需进行一次矩阵–向量乘法。
- 定理 38.1 核对四个相同子空间、残量正交
  $r_n^Tr_j=0$（$j<n$）和 $A$-共轭关系
  $p_n^TAp_j=0$（$j<n$）。证明中涉及的替换分母和 $\beta_n$ 等式均回看原页，未按 OCR 断行猜测。
- 定理 38.2 核对唯一最小性、单调性
  \[
  \lVert e_n\rVert_A\leq\lVert e_{n-1}\rVert_A
  \]
  以及精确算术下至多 $m$ 步收敛；同时保留原书关于浮点算术中该保证失效的说明。
- 核对二次函数
  \[
  \varphi(x)=\frac12x^TAx-x^Tb
  \]
  以及
  \[
  \lVert e_n\rVert_A^2=2\varphi(x_n)+\text{constant}.
  \]
  译稿明确说明未知常数不影响最小点，帮助读者理解 CG 与优化的对应关系。
- 核对 CG 多项式逼近问题（38.8）和定理 38.3 的谱界（38.9），其中 $\mathcal P_n$ 表示满足 $p(0)=1$ 且次数不超过 $n$ 的多项式集合。
- 定理 38.4 的多项式核对为
  \[
  p(x)=\prod_{j=1}^{n}\left(1-\frac{x}{\lambda_j}\right),
  \]
  对 $n$ 个不同特征值同时为零。
- 定理 38.5 的条件数核对为
  $\kappa=\lambda_{\max}/\lambda_{\min}$，误差界（38.10）保留两层不等式；证明中的缩放平移 Chebyshev 多项式、自变量 $\gamma=(\kappa+1)/(\kappa-1)$、式（38.11）和根
  \[
  z=\frac{\sqrt\kappa+1}{\sqrt\kappa-1}
  \]
  均按源页复核。
- 例 38.1 的阈值参数原页为希腊字母 $\tau$，OCR 容易读成拉丁字母或数字；译稿统一使用 $\tau$。四组非零元数、条件数、迭代步数、浮点运算量和 $\tau=0.2$ 时最低特征值为负的结论均已核对。
- 习题 38.1–38.6 全部保留；习题 38.6 的右端项核对为 $b=(1,1,\ldots,1)^T$，四条曲线分别包括 CG 计算残量、CG 实际残量、最速下降残量和定理 38.5 的估计。

## 插图核验

- 图 38.1 保留纵轴 $\lVert r_n\rVert$ 的对数刻度、横轴 $n$、曲线标签 $\tau=0.01,0.05,0.1,0.2$、曲线走势和原图的极限平台/不收敛行为。
- LaTeX 中使用本地 PNG 并配中文图注；Markdown 中使用同一最终 PNG 的绝对路径，避免依赖外部图片。
- 最终插图为源页裁切，不是 AI 生图或近似重绘；工作区内没有本讲的 Python、Matplotlib 或其他绘图脚本。

## 结论

第 38 讲已完成中文翻译、读者视角文字整理、公式/算法重建、图 38.1 保留，以及 LaTeX/Markdown 双版本同步。下一待处理范围为第 39–40 讲及附录、注释、参考文献和索引。
