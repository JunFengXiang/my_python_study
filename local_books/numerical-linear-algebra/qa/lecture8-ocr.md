# Lecture 8 OCR 与视觉核验记录

- 原书：`Numerical Linear Algebra`，Lecture 8 “Gram--Schmidt Orthogonalization”。
- 原书页码：56--62。
- 目标 PDF 页码：71--77。
- 核验方式：使用 `pdftotext -layout` 生成候选文本，并将目标 PDF 第 71--77 页以 150 dpi 渲染，逐页对照公式、循环顺序、上三角矩阵结构和几何图。对 OCR 无法恢复的矩阵与上下标，以原页视觉结果为准。

## 重点纠正的 OCR 风险

1. 原页条件为 $m\ge n$；OCR 多处把不等式和维数上标识别错。译文统一保留 $A\in\mathbb C^{m\times n}$、$m\ge n$。
2. 式 (8.1) 是
   `q_j=P_ja_j/\|P_ja_j\|_2`，其中 $P_j$ 投影到 $q_1,\ldots,q_{j-1}$ 的正交补，不能把 $P_j$ 误读成标量或下标丢失。
3. 式 (8.2)--(8.3) 的矩阵为 `\widehat Q_{j-1}=[q_1\ \cdots\ q_{j-1}]` 与 `P_j=I-\widehat Q_{j-1}\widehat Q_{j-1}^*`，共轭转置和帽号均已回看原页确认。
4. 式 (8.5)--(8.7) 是一串秩 $m-1$ 的投影，顺序为从 $P_{\perp q_1}$ 开始逐次作用；译文保留中间量 $v_j^{(1)},v_j^{(2)},\ldots$，避免 OCR 把它们识别成普通的 $v_j$。
5. 算法 8.1 的循环顺序与算法 7.1 不同：先初始化全部 $v_i=a_i$，再对 $i=1,\ldots,n$ 计算 $r_{ii}$、$q_i$，并立即更新所有 $j>i$ 的 $v_j$。这是本讲的核心，不能按经典 Gram--Schmidt 的循环顺序改写。
6. 定理 8.1 与式 (8.8)、(8.9) 的主项是 `\sim 2mn^2` flops；OCR 对波浪号和指数有误读，译文保留渐近含义及双重求和。
7. 式 (8.10) 为 `A R_1R_2\cdots R_n=\widehat Q`，且乘积等于 `\widehat R^{-1}`。不能误写成左乘，也不能把帽号删去。
8. 习题 8.2 的 MATLAB 函数名为 `mgs(A)`；题目要求约化 QR，译文保留 $Q\in\mathbb C^{m\times n}$ 和 $R\in\mathbb C^{n\times n}$。

## 图形资产

- `assets/figure-8-operation-count.png`：从目标 PDF 第 75 页（原书第 60 页）裁剪，保留逐层收缩的 $m\times(n-i)$ 矩形几何图。
- `assets/figure-8-triangular-orthogonalization.png`：从目标 PDF 第 76 页（原书第 61 页）裁剪，保留 $R_1$、$R_2$、$R_3$ 及右乘结构图。图中英文说明是原图的一部分，中文正文和图注补充其含义。

本讲的图均可从扫描页可靠裁剪，因此没有调用 Matplotlib 重绘。若后续讲次确实无法提取，绘图脚本只放在 `/tmp` 等临时目录，工作区只保存最终 PNG/SVG。

## 译文验收范围

- 已覆盖 Lecture 8 正文、式 (8.1)--(8.10)、定理 8.1、算法 8.1、两幅图和习题 8.1--8.3。
- 已从读者视角解释经典与修改后 Gram--Schmidt 的计算顺序差异、稳定性动机、运算量来源和三角正交化解释，但没有擅自补写习题答案。
- LaTeX 已独立 XeLaTeX 编译两遍并渲染检查 6 页；还需在全书统一检查阶段再次回归公式编号、图片路径和术语一致性。
