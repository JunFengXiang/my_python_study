# Lecture 11 OCR 与视觉核验记录

- 原书：Numerical Linear Algebra，Lecture 11 “Least Squares Problems”。
- 原书页码：77--85。
- 目标 PDF 页码：92--100。
- 核验方式：使用 pdftotext -layout 生成候选文本，并将目标 PDF 第 92--100 页以 150 dpi 渲染，逐页比对公式、Vandermonde 矩阵、投影图、算法步骤、帽号和习题函数。对 OCR 无法可靠恢复的上下标、共轭转置、近似号和不等式，以原页视觉结果为准。

## 重点纠正的 OCR 风险

1. 式 (11.1) 的残差是 $r=b-Ax\in\mathbb C^m$；式 (11.2) 的条件为 $A\in\mathbb C^{m\times n}$、$m\ge n$、$b\in\mathbb C^m$，目标是最小化 $\|b-Ax\|_2$。
2. 例 11.1 的多项式次数是 $m-1$，Vandermonde 系统是方阵；例 11.2 的多项式次数是 $n-1$ 且 $n<m$，式 (11.7) 是长方形系统，右侧使用近似号而不是等号。
3. 图 11.1 是 11 个方波数据点的 10 次插值多项式，端点附近有明显振荡；图 11.2 是相同数据的 7 次最小二乘拟合。图中文字和曲线均回看原页，未根据 OCR 重画。
4. 定理 11.1 的维数条件为 $m\ge n$；四个等价表述依次涉及 $r\perp\operatorname{range}(A)$、$A^*r=0$、$A^*Ax=A^*b$ 和 $Pb=Ax$。其中 $P\in\mathbb C^{m\times m}$ 是到 $\operatorname{range}(A)$ 的正交投影。
5. 证明中使用勾股关系
   $\|b-z\|_2^2=\|b-y\|_2^2+\|y-z\|_2^2>\|b-y\|_2^2$；由 $x^*A^*Ax=\|Ax\|_2^2$ 说明 $A^*A$ 奇异当且仅当 $A$ 秩亏。
6. 伪逆公式为 $A^+=(A^*A)^{-1}A^*\in\mathbb C^{n\times m}$，并总结为 $x=A^+b$、$y=Pb$。OCR 容易丢失上标加号和共轭转置。
7. 算法 11.1 使用 Cholesky 分解 $A^*A=R^*R$，先解 $R^*w=A^*b$，再解 $Rx=w$；式 (11.14) 的运算量是 $mn^2+\frac13n^3$ flops。
8. QR 路线使用约化分解 $A=\widehat Q\widehat R$，投影为 $P=\widehat Q\widehat Q^*$，并解 $\widehat R x=\widehat Q^*b$。式 (11.18) 是 $2mn^2-\frac23n^3$ flops，不能把 $\widehat Q,\widehat R$ 的帽号或右侧共轭转置删掉。
9. SVD 路线使用 $A=\widehat U\widehat\Sigma V^*$、$P=\widehat U\widehat U^*$，先解对角系统 $\widehat\Sigma w=\widehat U^*b$，再令 $x=Vw$。式 (11.22) 的典型估计是 $2mn^2+11n^3$ flops。
10. 习题 11.1 的分块矩阵为 $A=[A_1;A_2]$，其中 $A_1$ 是非奇异的 $n\times n$ 矩阵、$A_2$ 是 $(m-n)\times n$ 矩阵。习题 11.2 使用 $f(x)=x^{-1}$、$e^x$、$\sin x$ 和 Gamma 函数 $\Gamma(x)$；OCR 容易把 $x^{-1}$ 和 Gamma 函数识别成乱码。习题 11.3 的尺寸为 $m=50,n=12$，右端为 $\cos(4t)$，比较正规方程、mgs、house、qr、左除和 SVD 六种方法。

## 图形资产

- assets/figure-11-1.png：从目标 PDF 第 94 页（原书第 79 页）裁切，保留 10 次插值曲线和 11 个叉号数据点。
- assets/figure-11-2.png：从目标 PDF 第 95 页（原书第 80 页）裁切，保留 7 次最小二乘曲线和数据点。
- assets/figure-11-3.png：从目标 PDF 第 96 页（原书第 81 页）裁切，保留 $\operatorname{range}(A)$、$b$、$r=b-Ax$ 和 $y=Ax=Pb$ 等图中文字。

本讲三幅图均可从扫描页可靠裁切，因此没有调用 Matplotlib 重绘。若后续讲次出现无法可靠提取的图，绘图脚本只放在 /tmp 等临时目录，工作区只保存最终 PNG/SVG。

## 译文验收范围

- 已覆盖 Lecture 11 导言、最小二乘定义、两个多项式拟合例子、式 (11.1)--(11.22)、定理及证明、正规方程/QR/SVD 三种算法、算法比较和习题 11.1--11.3。
- 已从读者视角补充了残差、最近点、正规方程与三条算法路线之间的衔接，但没有擅自补写习题答案。
- latex/l11.tex 已独立 XeLaTeX 编译两遍并渲染检查 9 页；三幅图的裁切边界和最终页面布局已逐页检查。
