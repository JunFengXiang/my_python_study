# 第 33 讲 OCR、公式与版面核验记录

## 范围

- 原书页：250–256。
- 目标 PDF 页：265–271。
- 处理对象：第 33 讲“Arnoldi 迭代”。
- 中文正文：translation/textbook.md。
- 独立 LaTeX：translation/latex/l33.tex。
- 独立位图：无；原书中的表格、算法框和矩阵关系已在两个版本中重构。

## 处理方法

1. 使用 pdftotext 提取候选文本，并对目标 PDF 页 265–271 的 7 个源页逐页渲染、逐页核对正文、公式、表格、算法框和习题。
2. OCR 中的 $q_1$、$q_n$、$q_{n+1}$、$\widetilde H_n$、$H_n$、$Q_n^*$ 和 $K_n$ 经常被识别为错误字符或缺失上下标；所有这些记号均按原页版式逐式核对。
3. 原书无需要作为独立文件保存的图片；四算法对照表、同时迭代/Arnoldi 对照表、Arnoldi 算法框以及 Hessenberg 矩阵结构均以可编译 LaTeX 表格/矩阵和 Markdown 表格/缩进算法重建。
4. l33.tex 使用 XeLaTeX 编译两遍，输出到 /tmp/l33.pdf；最终 PDF 共 6 页，日志无 Undefined、Error、Overfull、Underfull、Warning 或 Missing character。最终渲染页 1–6 已回看，重点检查了算法框、矩阵维数、公式编号和习题分页。

## 重点 OCR 修正

- 核对 Arnoldi 与 Gram–Schmidt 的类比：Householder 通过正交操作将矩阵三角化，Gram–Schmidt 通过三角操作正交化；Hessenberg 约化的对应方法为两侧 Householder 与 Arnoldi。
- 核对基本设定为 $A\in\mathbb C^{m\times m}$、$n<m$、$\lVert\cdot\rVert=\lVert\cdot\rVert_2$，以及启动向量 $b$ 在特征值问题中通常随机、在方程组问题中作为右端或初始残差。
- 逐式核对
  \[
  Q_n=[q_1,\ldots,q_n],\qquad
  AQ_n=Q_{n+1}\widetilde H_n,
  \]
  以及
  \[
  Aq_n=h_{1n}q_1+\cdots+h_{nn}q_n+h_{n+1,n}q_{n+1}.
  \]
- 算法 33.1 按原页重建为 $q_1=b/\lVert b\rVert$、$v=Aq_n$、$h_{jn}=q_j^*v$、$v\leftarrow v-h_{jn}q_j$、$h_{n+1,n}=\lVert v\rVert$ 和 $q_{n+1}=v/h_{n+1,n}$，没有把 $q_j^*$ 误写成 $q_j$。
- 核对 Krylov 子空间和矩阵为
  \[
  \mathcal K_n=\operatorname{span}\{b,Ab,\ldots,A^{n-1}b\},\qquad
  K_n=[b,Ab,\ldots,A^{n-1}b],
  \]
  以及约化 QR 分解 $K_n=Q_nR_n$；保留“显式形成 $K_n$ 通常不稳定”的解释。
- 核对投影矩阵由删除 $\widetilde H_n$ 最后一行得到的 $H_n$ 给出，并保留 $H_n=Q_n^*AQ_n$、Rayleigh–Ritz 解释以及 Ritz 值定义
  \[
  \{\theta_j\}=\{\text{$H_n$ 的特征值}\}.
  \]
- 核对定理 33.1 的三条结论分别为（33.11）$K_n=Q_nR_n$、（33.12）$H_n=Q_n^*AQ_n$、（33.13）$AQ_n=Q_{n+1}\widetilde H_n$。
- 补回 OCR 漏掉的原书第 256 页说明：$h_{n+1,n}=0$ 称为 breakdown，但通常是良性的；并保留习题 33.3 关于最小多项式次数与启动向量依赖性的三问。

## 结论

第 33 讲已完成中文翻译、读者视角文字整理、公式/表格/算法框重建，以及 LaTeX/Markdown 双版本同步。下一待处理范围为第 34–40 讲及附录、注释、参考文献和索引。
