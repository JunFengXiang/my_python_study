# Lecture 40 OCR / translation QA

- 源页：目标 PDF 328–335；原书页 313–320。
- 目标 PDF 第 335 页已视觉核对为空白尾页；正文与习题位于第 328–334 页。
- 源文本：/tmp/trefethen-l40.txt；视觉核对使用 /tmp/trefethen-l40-hi/page-328.png 至 /tmp/trefethen-l40-hi/page-335.png。
- 输出：latex/l40.tex、累计 textbook.md、assets/figure-40-1-preconditioned-cg.png。

## OCR 与公式核对

1. 式（40.1）–（40.3）逐页核对为 $Ax=b$、$M^{-1}Ax=M^{-1}b$ 和 $My=c$；没有把预处理操作误写成显式形成 $M^{-1}$。
2. 源 OCR 将 $\lVert M^{-1}A-I\rVert_2$ 的减号和范数下标破坏；已恢复“特征值接近 1 且范数小”的强条件，并保留“接近正规且特征值聚集”的经验法则。
3. 左、右预处理的关系按源页 314 恢复为 $AM^{-1}y=b$、$x=M^{-1}y$；只在 Hermitian 正定情形下采用保持对称性的变换。
4. 式（40.4）已按源页 314 恢复为
   $\bigl[C^{-1}AC^{-*}\bigr]C^*x=C^{-1}b$，并显式说明 $C^{-*}=(C^*)^{-1}$。
5. 源页 315 的例子中，矩阵对角元核对为 $a_{ii}=0.5+\sqrt{i}$，近邻和第 100 条副对角线的元素为 1；右端项为全 1 向量。没有沿用 OCR 中的乱码。
6. 对角预处理器核对为 $M=\operatorname{diag}(A)$，$m_{ii}=0.5+\sqrt{i}$，并取 $C=M^{1/2}$；图注核对为习题 36.3 的矩阵加 $0.5I$。
7. 粗网格预处理器式（40.5）保留了三个算子按“传递到细网格—粗网格算子—传递到粗网格”组合的顺序，并恢复复合符号 $\circ$。
8. 预处理器概览逐项覆盖源页 316–318：Jacobi、IC/ILU、粗网格、局部近似、块预处理器与区域分解、低阶离散、常系数或对称近似、多项算子分裂、ADI、经典迭代一步、周期/卷积近似、不稳定直接方法和多项式预处理器。
9. 周期/卷积部分核对为 Toeplitz 条件 $a_{ij}=a_{i-j}$、循环矩阵
   $m_{ij}=m_{(i-j)\bmod m}$ 和 $O(m\log m)$ 快速 Fourier 变换复杂度。
10. 特征值预处理器覆盖 polynomial acceleration、shift-and-invert Arnoldi、有理 Krylov、Davidson 和 Jacobi–Davidson，并恢复 $\operatorname{eig}(r(A))=\{r(\lambda_j)\}$ 的内容。
11. 习题 40.1 的条件为 $\lVert I-M^{-1}N\rVert_2\le 1/2$，问题中的“20 步、六个数量级”和 CGN 小问均保留；习题 40.2 的 Hermitian 正定与非 Hermitian 对比也逐句核对。

## 插图处理

- 图 40.1：从源页 315 的高分辨率页面裁出收敛曲线，保留坐标、两条曲线、曲线标注和对数刻度；中文图注补充矩阵构造、$0.5I$ 和迭代效果。
- 临时裁图文件位于 /tmp/trefethen-l40*；linear-algebra/translation/ 只保留最终 PNG，不保留裁图或绘图脚本。

## LaTeX 构建与视觉检查

- 使用 XeLaTeX 独立编译 latex/l40.tex，输出 /tmp/l40-build/l40.pdf。
- pdfinfo：7 页，A4。
- 第二次及最终编译日志无 Warning、Overfull、Underfull、Error、Missing character 或 Undefined。
- 使用 pdftoppm -png -r 120 渲染 /tmp/l40-render/page-1.png 至 page-7.png，逐页目视检查：
  - 式（40.1）–（40.5）编号和伴随/逆矩阵记号正确；
  - 图 40.1 完整、清晰，图注未截断；
  - 预处理器概览、结语和两道习题均出现，页面底部无溢出或遮挡。

## 文件卫生

- 工作区未新增 .py、.ipynb 或 .m 绘图脚本。
- Lecture 40 完成后，附录、注释、参考文献和索引仍待从原书后续页纳入。
