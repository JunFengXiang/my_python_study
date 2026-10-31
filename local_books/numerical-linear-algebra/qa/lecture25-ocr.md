# 第 25 讲 OCR 与视觉核验记录

- 原书讲次：Lecture 25，Overview of Eigenvalue Algorithms
- 中文标题：特征值算法概述
- 原书页码：190–195
- 目标 PDF 页码：205–210
- 交付文件：`textbook.md`、`latex/l25.tex`

## 核验流程

1. 使用 `pdftotext` 提取目标 PDF 第 205–210 页作为候选文本。
2. 对 6 个源页逐页渲染并回看，核对特征多项式、伴随矩阵、Schur 变换、
   两阶段约化示意和三道习题。
3. 源页没有可独立提取的位图插图；两组“满矩阵 → Hessenberg/三对角矩阵
   → 三角/对角矩阵”的示意图用 LaTeX 矩阵重建，并在 Markdown 中保留
   对应的矩阵结构。
4. 使用 XeLaTeX 编译 `l25.tex` 两遍，渲染最终 5 页并逐页检查。

## 重点 OCR 与数学核验

- 幂迭代序列核对为
  \[
  x/\|x\|,\quad Ax/\|Ax\|,\quad A^2x/\|A^2x\|,\quad
  A^3x/\|A^3x\|,\ldots
  \]
  并明确其收敛目标是绝对值最大的特征值对应的特征向量。
- 多项式 (25.1) 核对为
  \(p(z)=z^m+a_{m-1}z^{m-1}+\cdots+a_1z+a_0\)。
- 公式 (25.2) 补回 OCR 中容易漏掉的整体因子
  \(p(z)=(-1)^m\det(\cdots)\)，并核对最后一个对角条目为
  \(-z-a_{m-1}\)。
- 伴随矩阵 (25.3) 的次对角线 1 和最后一列
  \(-a_0,-a_1,\ldots,-a_{m-1}\) 均按源页复核；左特征向量恢复为
  \((1,z,z^2,\ldots,z^{m-1})\)。
- 定理 25.1 采用 \(m\ge5\)，而不是 OCR 容易产生的严格不等式；
  结论保留“有理数、四则运算和根式不能表达任意高次多项式根”的含义。
- Schur 迭代核对为
  \(Q_j^*\cdots Q_2^*Q_1^*AQ_1Q_2\cdots Q_j\to T\)；
  Hermitian 情形的极限同时为三角矩阵和 Hermitian 矩阵，因而是对角矩阵。
- 两阶段复杂度核对为：第一阶段 \(O(m^3)\)；一般矩阵第二阶段通常
  \(O(m)\) 次迭代、每步 \(O(m^2)\)，总量 \(O(m^3)\)；若不先 Hessenberg
  约化则可能达到 \(O(m^4)\) 或更高。Hermitian 且只求特征值时，第二阶段
  每步为 \(O(m)\)，总量为 \(O(m^2)\)。
- 习题 25.2 的收敛关系核对为
  \(e_{k+1}\le C(e_k)^\alpha\)，提示恢复为
  \(f_k=C^{1/(\alpha-1)}e_k\)。Markdown 与 LaTeX 均将
  \(O(\log\varepsilon_{\mathrm{machine}})\) 按正的工作量写成
  \(O(|\log\varepsilon_{\mathrm{machine}}|)\)。
- 习题 25.3 的三个结构按源页逐项重排：
  (a) 上三角，(b) 中心条目为 0 且两侧有次对角线非零项，(c) 第二、
  第三行均只保留第三列非零项；题目要求保留三种可达性分类。

## 插图处理

源页没有需要独立保存的位图插图。两组算法流程图不是可靠的独立图像，
因此在 `latex/l25.tex` 与 `textbook.md` 中用矩阵示意
重建；工作区没有新增 Matplotlib 或其他绘图脚本。

## 编译与视觉结果

- `latex/l25.tex`：从 `translation/latex` 目录执行 XeLaTeX 两遍通过。
- 最终输出：`/tmp/l25.pdf`，共 5 页。
- 最终渲染页 `page-1.png` 至 `page-5.png` 已逐页回看；公式 (25.1)–(25.4)、
  伴随矩阵、两组阶段示意和习题矩阵均未越界。
- 最终日志未出现 `Undefined`、`Error`、`Overfull`、`Underfull`、`Warning`
  或 `Missing character`。
