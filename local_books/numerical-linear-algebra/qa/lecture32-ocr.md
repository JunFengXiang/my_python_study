# 第 32 讲 OCR、插图与版面核验记录

## 范围

- 原书页：243–249。
- 目标 PDF 页：258–264。
- 处理对象：第 32 讲“迭代法概述”。
- 中文正文：translation/textbook.md。
- 独立 LaTeX：translation/latex/l32.tex。
- 最终插图：
  - translation/assets/figure-32-black-box.png
  - translation/assets/figure-32-krylov-table.png
  - translation/assets/figure-32-convergence.png
  - translation/assets/figure-32-exponents.png

## 处理方法

1. 使用 pdftotext 提取候选文本，并对目标 PDF 页 258–264 的 7 个源页逐页渲染、逐页核对正文、公式、表格、图示和习题。
2. 对 $m$、$\nu$、Krylov 序列、$A^*$、Hessenberg 以及复杂度指数等容易受 OCR 影响的内容，结合源页版式重新核对；不能只依据纯文本提取结果。
3. 黑盒图和 Krylov 分类表从源页高分辨率裁切；两幅曲线图按源页视觉结构保留为最终 PNG。所有辅助裁切与重绘脚本只在 /tmp 中使用，工作区不保存绘图脚本。
4. l32.tex 使用 XeLaTeX 编译两遍，输出到 /tmp/l32.pdf；最终 PDF 共 6 页，日志无 Undefined、Error、Overfull、Underfull、Warning 或 Missing character。最终渲染页 1–6 已回看，重点检查了四幅图片、复杂度指数、分块矩阵和 Strassen 公式。

## 重点 OCR 修正

- 核对历史规模表为 1950 年 $m=20$、1965 年 $m=200$、1980 年 $m=2000$、1995 年 $m=20000$，并保留 Wilkinson、Forsythe–Moler、UNPACK、LAPACK 标记。
- 核对硬件增长与问题规模的数量级关系：维数增加 $10^3$ 倍、硬件加速约 $10^9=(10^3)^3$，以及迭代法希望把典型复杂度从 $O(m^3)$ 降至 $O(m^2)$ 或更低。
- 核对稀疏例子的参数为 $m=10^5$、每行 $\nu=10$ 个非零条目；黑盒只需计算 $x\mapsto Ax$，稀疏矩阵–向量乘法为 $O(\nu m)$。
- 核对 Krylov 序列为 $b,Ab,A^2b,A^3b,\ldots$，表格按 $Ax=b$ / $Ax=\lambda x$ 与 $A=A^*$ / $A\ne A^*$ 分类，并保留 CG、Lanczos、GMRES、CGN、BCG 和 Arnoldi。
- 核对 Hermitian 约化矩阵为三对角形式，非 Hermitian 约化矩阵为 Hessenberg 形式；没有把 Arnoldi 误写成只适用于 Hermitian 矩阵。
- 核对理想迭代复杂度为 $O(1)\times O(m)=O(m)$，而常见改进为 $O(m^3)\to O(m^2)$；图 32.1 的残差下限为机器精度量级。
- 核对直接法历史指数：Strassen 给出 $\log_2(7)\approx2.81$，Coppersmith–Winograd 约为 2.376；图 32.2 的说明保留“理论指数低但常数很大、实际不实用”的限定。
- 核对习题 32.1 中误差随 $h$ 线性缩小、两位有效数字耗时 1 分钟的条件；习题 32.2 的七个 Strassen 乘积 $P_1,\ldots,P_7$ 及四个输出组合均按源页重建，未沿用 OCR 中可能错位的上下标。

## 插图核验

- 黑盒图保留输入 $x$、BLACK BOX 和输出 $Ax$ 的方向关系。
- Krylov 分类表保留两列 $Ax=b$、$Ax=\lambda x$，两行 $A=A^*$、$A\ne A^*$，并核对各单元格中的算法名称。
- 图 32.1 保留 direct/iterative 两条收敛示意线、残差对数尺度、机器精度水平和 $O(m^3)$ 工作量标记；中文图注解释了“先收敛”和“完成直接法后才下降”的含义。
- 图 32.2 保留复杂度指数随年份下降的阶梯曲线、指数纵轴和 year 横轴；中文图注明确说明它表示已知最好指数而不是实际运行时间。

## 结论

第 32 讲已完成中文翻译、读者视角文字整理、公式/表格重建、4 组插图保留，以及 LaTeX/Markdown 双版本同步。下一待处理范围为第 33–40 讲及附录、注释、参考文献和索引。
