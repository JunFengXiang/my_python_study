# Lecture 39 OCR / translation QA

- 源页：目标 PDF 318–327；原书页 303–312。
- 源文本：/tmp/trefethen-l39.txt；视觉核对使用 /tmp/trefethen-l39-hi/page-319.png 至 /tmp/trefethen-l39-hi/page-327.png。
- 输出：latex/l39.tex、累计 textbook.md、assets/figure-39-1-classification.png、assets/figure-39-2-bcg-gmres.png。

## OCR 与公式核对

1. 源 OCR 将 $A^*A$、$A^*b$、$(A^*A)^{n-1}A^*b$ 等伴随与幂次严重混淆；已根据源页 304 逐项恢复为式（39.1）和式（39.2）。
2. 源 OCR 将残量记号识别成 r.、7. 等；已统一为 $r_n=b-Ax_n$，并保留式（39.3）的最小残量结论。
3. 源 OCR 将条件数 $\kappa$ 识别为 is，并丢失分式结构；已恢复式（39.4）
   $\lVert r_n\rVert_2/\lVert r_0\rVert_2\le 2((\kappa-1)/(\kappa+1))^n$，以及 $O(\kappa)$ 与 $O(\sqrt\kappa)$ 的对比。
4. 循环矩阵恢复为源页 305 的上移一位、左下角为 1 的矩阵，公式编号为（39.5）；习题 39.1 的引用已同步为（39.5）。
5. 源 OCR 将 $V^{-*}$、$T^*$、$(V^*)^{-1}$ 等记号损坏；已按源页 305–306 恢复 $A=VTV^{-1}$、$W=V^{-*}$ 及双正交关系（39.6）。
6. 源 OCR 将 $V_n,W_n$ 的列矩阵和 $\delta_{ij}$ 识别为字母/数字噪声；已恢复式（39.7）以及
   $W_n^*V_n=V_n^*W_n=I_n$。
7. 源页 307 的三项递推已逐字符核对：$Av_n=\gamma_{n-1}v_{n-1}+\alpha_nv_n+\beta_nv_{n+1}$ 为式（39.11），而伴随递推使用
   $\overline\beta_{n-1}$、$\overline\alpha_n$、$\overline\gamma_n$，为式（39.12）；没有把复共轭横线误删。
8. 源 OCR 将 Krylov 子空间指数、$A^*$ 和内积符号混淆；已恢复式（39.13）、GMRES 正交条件（39.14）和 BCG 正交条件（39.15）。
9. 算法 39.1 已与源页 309 的框线内容逐行核对：$\alpha_n$ 的分母为 $q_{n-1}^*Ap_{n-1}$，影子残量更新为
   $s_n=s_{n-1}-\alpha_nA^*q_{n-1}$，并保留 $p_n,q_n$ 两条递推。
10. 习题 39.5 的规模、特征值区域和环域均按源页 312 核对为 $10^4$、$10^5$、$10^6$、$10^7$，以及
    $-10\le\operatorname{Re}(\lambda)\le10$、$-1\le\operatorname{Im}(\lambda)\le1$、$1\le|\lambda|\le2$。

## 插图处理

- 图 39.1：源页 318 中的分类图从高分辨率页面裁出，保留原英文节点和省略号；中文图注解释其含义。
- 图 39.2：源页 322 中的 GMRES/BCG 对数残量图从高分辨率页面裁出，保留坐标轴、曲线和 BCG/GMRES 标注；中文图注与正文说明随机符号、$\tau=0.01$ 和奇偶步效应。
- 裁图临时文件和任何可能的重绘脚本均位于 /tmp/trefethen-l39*；linear-algebra/translation/ 不包含绘图脚本。

## LaTeX 构建与视觉检查

- 使用 XeLaTeX 独立编译 latex/l39.tex，输出 /tmp/l39-build/l39.pdf。
- pdfinfo：9 页，A4。
- 最终编译日志无 Warning、Overfull、Underfull、Error、Missing character 或 Undefined。
- 使用 pdftoppm -png -r 120 渲染 /tmp/l39-render/page-1.png 至 page-9.png，逐页目视检查：
  - 公式（39.1）–（39.15）编号连续且与源书对应；
  - 无编号的辅助公式不再出现 LaTeX 自动编号；
  - 两幅图完整、清晰，图注未被截断；
  - 算法框、习题和页面底部没有溢出或遮挡。

## 文件卫生

- 工作区未新增 .py、.ipynb 或 .m 绘图脚本。
- 本讲完成后继续保留第 40 讲、附录、注释、参考文献和索引待处理状态。
