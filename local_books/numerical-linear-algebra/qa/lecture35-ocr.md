# 第 35 讲 OCR、插图与版面核验记录

## 范围

- 原书页：266–275。
- 目标 PDF 页：281–290。
- 处理对象：第 35 讲“GMRES”。
- 中文正文：translation/textbook.md。
- 独立 LaTeX：translation/latex/l35.tex。
- 最终插图：
  - translation/assets/figure-35-gmres-least-squares.png
  - translation/assets/figure-35-eigenvalues.png
  - translation/assets/figure-35-convergence-good.png
  - translation/assets/figure-35-eigenvalues-bad.png
  - translation/assets/figure-35-convergence-bad.png

## 处理方法

1. 使用 pdftotext 提取候选文本，并对目标 PDF 页 281–290 的 10 个源页逐页渲染、逐页核对正文、公式、算法框、图示和习题。
2. OCR 对 $\mathcal K_n$、$\widetilde H_n$、$\mathcal P_n$、$p_n(A)b$、共轭转置、范数下标和复数对角元有明显混淆；所有上下标、矩阵维数、归一化条件和不等式均回看原页核对。
3. 图 35.1、35.2、35.3、35.4、35.5 均从高分辨率源页裁切为最终 PNG，去除页眉和原文英文图注；中文图注在 Markdown/LaTeX 中重写。裁切辅助只在 /tmp 中进行，工作区不保存绘图脚本；本讲没有需要重绘的图。
4. l35.tex 使用 XeLaTeX 编译两遍，输出到 /tmp/l35-build/l35.pdf；最终 PDF 共 10 页，日志没有 Error、Undefined、Overfull、Underfull、Warning 或 Missing character。最终渲染页 1–10 已回看，重点检查五幅插图、定理 35.1 的校注、式（35.13）–（35.16）和习题分页。

## 重点 OCR 与数学核对

- 核对 GMRES 的定义：$x_n\in\mathcal K_n$，并最小化 $r_n=b-Ax_n$ 的二范数；直接对 $AK_n$ 做 QR 分解的方案数值不稳定且构造了不需要的 $R$ 因子。
- 核对式（35.1）–（35.6）：
  \[
  AK_n=[Ab,A^2b,\ldots,A^nb],\qquad
  \left\lVert\widetilde H_ny-\lVert b\rVert e_1\right\rVert=\min.
  \]
  \widetilde H_n 为 $(n+1)\times n$ 的 Hessenberg 矩阵，且 $Q_{n+1}^*b=\lVert b\rVert e_1$。
- 算法 35.1 核对为 $q_1=b/\lVert b\rVert$，每步执行 Arnoldi、求解内部最小二乘问题并设置 $x_n=Q_ny$；内部 QR 求解为 $O(n^2)$，利用更新可降为每步 $O(n)$。
- 核对式（35.7）–（35.10）：$\mathcal P_n$ 是次数不超过 $n$ 且满足 $p(0)=1$ 的多项式空间；$x_n=q_n(A)b$，$r_n=p_n(A)b$，GMRES 最小化 $\lVert p_n(A)b\rVert$。
- 定理 35.1 的尺度不变性核对为 $A\mapsto\sigma A$、$b\mapsto\sigma b$ 时 $r_n\mapsto\sigma r_n$。
- 定理 35.1 的酉相似变换：原书页 269 印作残量变为 $\{U^*r_n\}$，但同页变换为 $A\mapsto UAU^*$、$b\mapsto Ub$。由
  \[
  Ub-(UAU^*)(Ux_n)=U(b-Ax_n)=Ur_n
  \]
  可知应为 $\{Ur_n\}$；LaTeX/Markdown 均保留校注并采用按定义校正后的公式。
- 核对式（35.11）–（35.13）：GMRES 残量单调不增，精确算术下至多 $m$ 步收敛，且
  \[
  \frac{\lVert r_n\rVert}{\lVert b\rVert}
  \leq\inf_{p_n\in\mathcal P_n}\lVert p_n(A)\rVert.
  \]
- 核对式（35.14）–（35.16）：$\lVert p\rVert_S=\sup_{z\in S}|p(z)|$；若 $A=V\Lambda V^{-1}$ 可对角化，则谱上的多项式界带有 $\kappa(V)$ 因子。
- 例 35.1 核对 $m=200$、均值 2、标准差 $0.5/\sqrt{200}$、谱圆盘中心 $z=2$、半径 $1/2$、收敛速率约 $4^{-n}$、$\kappa(A)\approx2.03$、$\kappa(V)\approx141$、十步约六位精度及 $m=2000$ 时的运算量比较。
- 例 35.2 核对 $A'=A+D$，其中
  \[
  d_k=(-2+2\sin\theta_k)+\mathrm{i}\cos\theta_k,\qquad
  \theta_k=k\pi/(m-1),\quad 0\leq k\leq m-1.
  \]
  原书此处没有独立公式编号，译稿没有新增编号；同时核对 $\kappa(A)\approx4.32$、$\kappa(V)\approx54.0$ 以及“谱的位置而非大小造成困难”的结论。
- 习题 35.1–35.6 全部保留；特别核对 Richardson 迭代、Givens QR 更新、任意初值和 GMRES$(k)$ 重启描述。

## 插图核验

- 图 35.1 保留 $b$、$AQ_ny$、$r_n=p_n(A)b$、虚线 $A\mathcal K_n$、直角投影关系和坐标轴。
- 图 35.2 保留以 $z=2$ 为中心、半径 $1/2$ 的虚线圆及圆盘内的特征值散点。
- 图 35.3 保留 $\lVert r_n\rVert/\lVert b\rVert$ 的对数纵轴、迭代次数 $n$、散点、虚线参考率 $4^{-n}$。
- 图 35.4 保留弯向原点一侧的半圆形特征值云和坐标轴。
- 图 35.5 保留停滞收敛散点、对数纵轴和迭代次数横轴；图注说明应寻找更好的预条件器。

## 结论

第 35 讲已完成中文翻译、读者视角文字整理、公式/算法重建、5 幅插图保留，以及 LaTeX/Markdown 双版本同步。下一待处理范围为第 36–40 讲及附录、注释、参考文献和索引。
