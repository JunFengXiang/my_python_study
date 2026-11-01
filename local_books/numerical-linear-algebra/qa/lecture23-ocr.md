# 第 23 讲 OCR 与视觉核验记录

- 原书讲次：Lecture 23，Cholesky Factorization
- 原书页码：172–178
- 目标 PDF 页码：187–193
- 中文标题：Cholesky 分解
- 交付文件：textbook.md、latex/l23.tex

## 核验流程

1. 用 pdftotext 提取目标 PDF 第 187–193 页作为候选文本。
2. 对 7 个源页逐页渲染并回看，核对 Hermitian 正定定义、块矩阵分解、算法、运算量、稳定性定理和 MATLAB 习题。
3. 第 176 页的三维层叠运算量示意图从 300 dpi 源页裁切为最终 PNG；没有使用未经核验的 OCR 图，也没有把绘图脚本放入工作区。
4. 使用 XeLaTeX 编译 l23.tex 两遍，并渲染最终 6 页逐页检查。

## 重点 OCR 与数学核验

- Hermitian 条件核对为 \(a_{ij}=\overline{a_{ji}}\)、\(A=A^*\)，正定条件为对所有非零 \(x\) 有 \(x^*Ax>0\)。
- 块消元公式 (23.1) 核对为右下角 Schur 补 \(K-ww^*\)，一般步使用 \(K-ww^*/a_{11}\)。
- Cholesky 分解核对为 \(A=R^*R\)，且 \(R\) 为上三角、\(r_{jj}>0\)；没有把平方根或伴随符号抄成普通转置。
- 算法 23.1 保留了先更新 \(R_{j,j:m}\)、再将 \(R_{k,k:m}\) 除以 \(\sqrt{R_{kk}}\) 的顺序。
- 运算量求和核对为约 \(\frac13m^3\) flops，几何图的四面体体积为 \(\frac16m^3\)，每个单位立方体对应两次浮点运算。
- 定理 23.2 核对为 \(\widetilde R^*\widetilde R=A+\delta A\) 和相对向后误差 \(O(\varepsilon_{\mathrm{machine}})\)；同时保留病态时因子本身可能不接近的说明。
- 定理 23.3 核对为 \((A+\Delta A)\widetilde x=b\) 及相对扰动 \(O(\varepsilon_{\mathrm{machine}})\)。
- 习题 23.1–23.3 全部保留，MATLAB 会话中的矩阵构造、反斜杠、特征值和耗时数值均按源页核对。

## 插图处理

原书的三维层叠线稿已从目标 PDF 第 191 页的 300 dpi 渲染结果裁切为 assets/figure-23-operation-count.png。正文图注说明其几何含义；没有新增 Matplotlib 重绘脚本。

## 编译与视觉结果

- l23.tex：从 latex 目录执行 XeLaTeX 两遍通过。
- 最终输出：6 页。
- 最终 6 页均已逐页回看；矩阵、平方根、算法伪代码、运算量图、稳定性公式和 MATLAB 代码均未越界。
