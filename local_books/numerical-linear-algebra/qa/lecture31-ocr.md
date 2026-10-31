# 第 31 讲 OCR、插图与版面核验记录

## 范围

- 原书页：234–240。
- 目标 PDF 页：249–255。
- 处理对象：第 31 讲“奇异值分解的计算”。
- 中文正文：translation/textbook.md。
- 独立 LaTeX：translation/latex/l31.tex。
- 最终插图：
  - translation/assets/figure-31-two-phases.png
  - translation/assets/figure-31-golub-kahan.png
  - translation/assets/figure-31-lhc.png
  - translation/assets/figure-31-three-step.png
  - translation/assets/figure-31-operation-count.png

## 处理方法

1. 使用 pdftotext 提取候选文本，并对目标 PDF 页 249–255 的 7 个源页逐页渲染、逐页核对正文、公式、矩阵、图示和习题。
2. 公式、分块矩阵和双对角矩阵优先根据源页版式重建，不把 OCR 的星号、上下标或矩阵列数直接视为可信结果。
3. 5 组示意图均从 300 dpi 源页裁取为最终 PNG；裁切和辅助检查只在 /tmp 中进行，工作区不保存绘图脚本。
4. l31.tex 使用 XeLaTeX 编译两遍，输出到 /tmp/l31.pdf；最终 PDF 共 8 页，日志无 Undefined、Error、Overfull、Underfull、Warning 或 Missing character。最终渲染页 1–8 已回看。

## 重点 OCR 修正

- 明确 SVD 的尺寸条件为 $m\ge n$，并保持 $A=U\Sigma V^*$、$\Sigma$ 为 $m\times n$ 矩形对角矩阵。
- 核对 $A^*A=V\Sigma^*\Sigma V^*$、扰动界和后向稳定关系 (31.1)，并保留由 $A^*A$ 导致的条件数平方化解释。
- 重建 Hermitian 增广矩阵
  \[
  H=\begin{bmatrix}0&A^*\\A&0\end{bmatrix}
  \]
  及分块特征值关系 (31.3)，避免 OCR 将 $A^*$、$-U$ 和两个 $\Sigma$ 块混淆。
- 两阶段复杂度核为第一阶段 $O(mn^2)$，第二阶段在机器精度视为常数时为 $O(n^2)$；保留超线性迭代项 $O(n\log|\log\varepsilon_{\mathrm{machine}}|)$。
- Golub–Kahan 双对角化核对为左侧 $n$ 个反射、右侧 $n-2$ 个反射，以及
  \[
  \mathord{\sim}4mn^2-\frac43n^3
  \]
  的运算量式 (31.4)。
- LHC 双对角化核对先做 $A=QR$，再对 $R$ 做 $B=U^*RV$，并保留
  \[
  \mathord{\sim}2mn^2+2n^3
  \]
  的式 (31.5) 和交叉条件 $m>\frac53n$。
- 三步双对角化核对中途 QR 的剩余矩阵长宽比 $(m-k)/(n-k)$，最优插入点为 2，以及式 (31.6)
  \[
  \mathord{\sim}4mn^2-\frac43n^3-\frac23(m-n)^3.
  \]
- 习题 31.5 的双对角矩阵按主对角线 $x_m,\ldots,x_{m-(n-1)}$ 和超对角线 $y_{n-1},\ldots,y_1$ 重建；每个变量是相应自由度的 $\chi^2$ 样本的正平方根。

## 插图核验

- 两阶段流程图保留稠密矩阵 $A$、双对角矩阵 $B$、对角矩阵 $\Sigma$ 及 Phase 1/Phase 2 标记。
- Golub–Kahan 图保留 $6\times4$ 矩阵的两对左右反射、零结构、$U_1^*$、$V_1$、$U_2^*$、$V_2$ 标记。
- LHC 图保留 $A\to Q^*A\to U^*Q^*AV$ 的矩阵结构示意。
- 三步双对角化图保留中途 QR 的虚线方框和四个矩阵状态。
- 图 31.1 保留三条运算量曲线、纵轴 flops/$n^3$、横轴 $m/n$、$5/3$ 与 2 的刻度和原图标签；中文图注在 LaTeX 与 Markdown 中单独重写。

## 结论

第 31 讲已完成中文翻译、读者视角文字整理、公式和矩阵重建、5 组插图保留，以及 LaTeX/Markdown 双版本同步。下一待处理范围为第 32–40 讲及附录、注释、参考文献和索引。

