# 第 26 讲 OCR 与视觉核验记录

- 原书讲次：Lecture 26，Reduction to Hessenberg and Tridiagonal Form
- 中文标题：化为 Hessenberg 型与三对角型
- 原书页码：196–201
- 目标 PDF 页码：211–216
- 交付文件：`textbook.md`、`latex/l26.tex`

## 核验流程

1. 使用 `pdftotext` 提取目标 PDF 第 211–216 页作为候选文本。
2. 将 6 个源页逐页渲染并回看，核对坏主意/好主意的 Householder 矩阵示意、
   算法 26.1、Hessenberg 与三对角约化的运算量、稳定性定理和三道习题。
3. 源页中的矩阵零结构属于算法示意，不作为独立位图提取；在 LaTeX 与
   Markdown 中用矩阵环境重建。两幅三维运算量示意图无法可靠独立提取，
   用 Matplotlib 重绘为 `assets/figure-26-operation-left.png` 和
   `assets/figure-26-operation-right.png`。绘图脚本仅存于 `/tmp`，未放入
   工作区。
4. 使用 XeLaTeX 编译 `l26.tex` 两遍，渲染最终 6 页并逐页检查。

## 重点 OCR 与数学核验

- “坏主意”核对为先左乘 $Q_1^*$、再右乘 $Q_1$；右乘会破坏此前引入的零，
  不能把有限过程误写成精确求出全部特征值。
- “好主意”核对为 $Q_1^*$ 保持第一行不变，只对第 $2,\ldots,m$ 行形成
  线性组合；右乘 $Q_1$ 保持第一列不变，只对第 $2,\ldots,m$ 列形成线性组合。
  第二步 $Q_2$ 保持第一、第二行和第一、第二列不变。
- Hessenberg 相似变换核对为
  \(Q_{m-2}^*\cdots Q_2^*Q_1^*AQ_1Q_2\cdots Q_{m-2}=H\)，且 $H$ 的
  第一条次对角线以下全部为零；该显示式本身未强行添加原书没有的公式编号。
- 算法 26.1 的循环范围核对为 $k=1,\ldots,m-2$，并保留
  \(x=A_{k+1:m,k}\)、\(v_k=\operatorname{sign}(x_1)\|x\|_2e_1+x\)、
  归一化以及左右两次子矩阵更新；明确说明不显式构造 $Q$，而是保存反射向量。
- 运算量核对为：左更新的元素体积趋于 $\frac13m^3$，约
  $\frac43m^3$ flops；右更新的元素体积趋于 $\frac12m^3$，约 $2m^3$
  flops；总 Hessenberg 约化为公式 (26.1) 的
  \(\frac{10}{3}m^3\) flops。
- Hermitian 情形核对为 Hermitian Hessenberg 矩阵必为三对角矩阵；利用稀疏性
  后右侧成本为 $\frac43m^3$、合计 $\frac83m^3$，再利用 Hermitian 结构
  得到公式 (26.2) 的 $\frac43m^3$ flops。
- 稳定性定理核对为存在
  \(\delta A\in\mathbb{C}^{m\times m}\)，满足
  \(\widetilde Q\widetilde H\widetilde Q^*=A+\delta A\) 以及
  \(\|\delta A\|/\|A\|=O(\varepsilon_{\mathrm{machine}})\)，对应公式 (26.3)。
- 习题 26.1 的 2-范数 $\epsilon$-伪谱四个等价条件逐项核对：扰动后的特征值、
  近似特征向量、最小奇异值和预解算子范数；$\sigma_m$ 明确为最小奇异值，
  特征值处预解算子范数按约定取无穷大。
- 习题 26.2 的矩阵规格核对为 $32\times32$，主对角线为 $-1$，第一、第二
  条超对角线为 1；伪谱参数为 $10^{-1},10^{-2},\ldots,10^{-8}$，半对数图
  区间为 $0\le t\le50$。
- 习题 26.3 的 Bauer–Fike 条件核对为 $A=V\Lambda V^{-1}$，圆盘半径为
  $\kappa(V)\|\delta A\|_2$；正规矩阵的结论保留为公式 (26.4)。

## 插图处理

- 坏主意/好主意中的矩阵零结构已用 LaTeX/Markdown 矩阵重排，保留粗体条目
  所表达的“本步发生改变的区域”。
- 原页两幅阶梯状三维运算量图未作为独立位图可靠提取，已用 Matplotlib
  重绘并保存最终 PNG；重绘脚本只在 `/tmp/trefethen_l26_figures.py`，
  工作区内没有 `.py` 或 `.ipynb` 绘图脚本。

## 编译与视觉结果

- `latex/l26.tex`：从 `translation/latex` 目录执行 XeLaTeX 两遍通过。
- 最终输出：`/tmp/l26.pdf`，共 6 页。
- 最终渲染页 `page-1.png` 至 `page-6.png` 已逐页回看；矩阵示意、两幅重绘
  图、算法、公式 (26.1)–(26.4) 与习题均未越界。
- 最终日志未出现 `Undefined`、`Error`、`Overfull`、`Underfull`、`Warning`
  或 `Missing character`。
