# 第 24 讲 OCR 与视觉核验记录

- 原书讲次：Lecture 24，Eigenvalue Problems
- 原书页码：181–189
- 目标 PDF 页码：196–204
- 中文标题：特征值问题
- 交付文件：textbook.md、latex/l24.tex

## 核验流程

1. 用 pdftotext 提取目标 PDF 第 196–204 页作为候选文本。
2. 对 9 个源页逐页渲染并回看，核对特征值分解、特征多项式、重数、相似变换、Schur 分解和习题矩阵。
3. 本讲没有独立位图插图；所有矩阵、块矩阵和公式均在 LaTeX/Markdown 中重排。
4. 使用 XeLaTeX 编译 l24.tex 两遍，并渲染最终 9 页逐页检查。

## 重点 OCR 与数学核验

- 统一恢复 \(\lambda\) 为特征值、\(\Lambda\) 为对角特征值矩阵，避免 OCR 将两者混成同一个字符。
- 公式 (24.2)–(24.4) 核对为 \(A=X\Lambda X^{-1}\)、\(AX=X\Lambda\) 和 \(X^{-1}b=\Lambda(X^{-1}x)\)。
- 几何重数核对为 \(\dim\mathcal{N}(A-\lambda I)\)；代数重数由 \(p_A(z)\) 中根的重数定义。
- 定理 24.4 的块矩阵核对为 \(B=V^*AV=\begin{bmatrix}\lambda I&C\\0&D\end{bmatrix}\)，并保留 \((z-\lambda)^n\) 因子。
- 缺陷矩阵例子核对为对角矩阵 \(A=2I\) 与含两个超对角 1 的三阶 Jordan 块 \(B\)。
- 行列式/迹公式 (24.8) 的乘积和求和均按代数重数计；酉对角化和 Schur 分解的伴随符号均按源页复核。
- Schur 证明核对为 \(U^*AU=\begin{bmatrix}\lambda&B\\0&C\end{bmatrix}\)、\(C=VTV^*\)，以及 \(Q=U\operatorname{diag}(1,V)\)。
- Gerschgorin 习题矩阵核对为 \(\begin{bmatrix}8&1&0\\1&4&\varepsilon\\0&\varepsilon&1\end{bmatrix}\)，并保留 \(|\varepsilon|<1\) 和 \(|\lambda_3-1|\le\varepsilon^2\)。
- 习题 24.1–24.4 全部保留，包括 \(e^{tA}\)、谱半径和谱 abscissa 的极限问题。

## 插图处理

源页没有独立插图。本讲的矩阵图示全部由 LaTeX 矩阵环境重建；工作区没有新增绘图脚本或临时脚本。

## 编译与视觉结果

- l24.tex：从 latex 目录执行 XeLaTeX 两遍通过。
- 最终输出：9 页。
- 最终 9 页均已逐页回看；块矩阵、Jordan 例子、Schur 证明、Gerschgorin 习题和公式编号均未越界。
