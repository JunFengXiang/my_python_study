# 第 34 讲 OCR、插图与版面核验记录

## 范围

- 原书页：257–265。
- 目标 PDF 页：272–280。
- 处理对象：第 34 讲“Arnoldi 方法如何定位特征值”。
- 中文正文：translation/textbook.md。
- 独立 LaTeX：translation/latex/l34.tex。
- 最终插图：
  - translation/assets/figure-34-least-squares.png
  - translation/assets/figure-34-eigenvalues.png
  - translation/assets/figure-34-lemniscates.png
  - translation/assets/figure-34-convergence.png

## 处理方法

1. 使用 pdftotext 提取候选文本，并对目标 PDF 页 272–280 的 9 个源页逐页渲染、逐页核对正文、公式、证明、图示和习题。
2. OCR 对 $p^n$、$\mathcal P^n$、$\lambda^{(n)}$、$\widetilde\lambda$、$H_n$、$\widetilde H_n$ 和 $a_{k,k+1}$ 等记号有明显混淆；所有上下标、共轭、范数和伪谱条件均回看原页核对。
3. 图 34.1、34.2、34.3、34.4 均从 300 dpi 源页裁切为最终 PNG，裁切时去除页眉和原文英文图注；中文图注在 Markdown/LaTeX 中重写。裁切辅助只在 /tmp 中进行，工作区不保存绘图脚本。
4. l34.tex 使用 XeLaTeX 编译两遍，输出到 /tmp/l34.pdf；最终 PDF 共 9 页，日志无 Undefined、Error、Overfull、Underfull、Warning 或 Missing character。最终渲染页 1–9 已回看，重点检查了四幅插图、定理证明和习题分页。

## 重点 OCR 修正

- 核对 Arnoldi 估计/Ritz 值是 $H_n$ 的特征值，并明确 $n\ll m$ 时通常只能寻找谱边缘的极端特征值。
- 非正规性段落保留“特征向量远不正交会导致特征值病态”和“非模态扰动可能被大幅放大”的警告；条件数核对为 $10^4$。
- 核对式（34.1）–（34.2）：
  \[
  x=c_0b+c_1Ab+\cdots+c_{n-1}A^{n-1}b=q(A)b.
  \]
- 核对 $\mathcal P^n$ 是次数为 $n$ 的首一多项式空间，式（34.3）为最小化 $\lVert p^n(A)b\rVert$，不能把上标误当作幂次。
- 定理 34.1 的证明按源页重建：$p(A)b=A^nb-Q_ny$、最小二乘正交条件 $Q_n^*p^n(A)b=0$、分块 Hessenberg 结构，以及由 Cayley–Hamilton 定理得到的特征多项式结论。
- 核对定理 34.2 的三种不变性：$A\mapsto A+\sigma I$ 时 Ritz 值平移，$A\mapsto\sigma A$ 时 Ritz 值缩放，酉相似变换并同步变换 $b$ 时 Ritz 值不变。
- 核对 Arnoldi 纽结线定义
  \[
  \{z\in\mathbb C:|p(z)|=C\},\qquad
  C=\frac{\lVert p^n(A)b\rVert}{\lVert b\rVert}.
  \]
- 图示例核对为 $m=100$、元素来自标准差 $m^{-1/2}$ 的实正态分布、将 $a_{11}$ 改为 1.5、离群特征值约 $\lambda\approx1.4852$；图 34.3 的步骤为 $n=5,6,7,8$。
- 核对几何收敛式（34.6）为
  \[
  |\lambda^{(n)}-\lambda|\approx(2/3)^n,
  \]
  以及候选多项式 $p(z)=z^{n-1}(z-\widetilde\lambda)$ 和
  \[
  |p(\lambda)|\approx(3/2)^n|\widetilde\lambda-\lambda|.
  \]
- 习题 34.1 的 Horner 公式核对为首一多项式的
  \[
  p(z)=c_0+z(c_1+z(c_2+\cdots+z(c_{n-1}+z)\cdots)).
  \]
  习题 34.3 的双对角矩阵核对为 $a_{k,k+1}=a_{k,k}=k^{-1/2}$、$N=64$，并保留 $\widetilde H_n$ 的矩形伪谱条件。

## 插图核验

- 图 34.1 保留 $A^nb$、$p^n(A)b$、$Q_ny$、正交残差和 Krylov 子空间 $\mathcal K_n$ 的几何关系。
- 图 34.2 保留单位圆、单位圆盘中的特征值散点以及右侧离群特征值。
- 图 34.3 保留 $n=5,6,7,8$ 四个面板、矩阵特征值小点、Ritz 值大点以及纽结线分支吞入离群值后收缩的过程。
- 图 34.4 保留误差曲线、参考线 $(2/3)^n$、对数纵轴和迭代次数横轴；中文图注明确说明实线与虚线含义。

## 结论

第 34 讲已完成中文翻译、读者视角文字整理、公式/证明重建、4 组插图保留，以及 LaTeX/Markdown 双版本同步。下一待处理范围为第 35–40 讲及附录、注释、参考文献和索引。
