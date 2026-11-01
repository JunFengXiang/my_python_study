# 第 27 讲 OCR 与视觉核验记录

- 原书讲次：Lecture 27，Rayleigh Quotient, Inverse Iteration
- 中文标题：Rayleigh 商与逆迭代
- 原书页码：202–210
- 目标 PDF 页码：217–225
- 交付文件：`textbook.md`、`latex/l27.tex`

## 核验流程

1. 使用 `pdftotext` 提取目标 PDF 第 217–225 页作为候选文本。
2. 对 9 个源页逐页渲染并回看，核对实对称矩阵限制、Rayleigh 商、幂迭代、
   逆迭代、Rayleigh 商迭代、三次收敛证明、例 27.1、运算量和习题。
3. 图 27.1 的单位球面网格图与 Rayleigh 商迭代闭环图从 300 dpi 源页裁切，
   保存到 `assets/figure-27-rayleigh-sphere.png` 和
   `assets/figure-27-rayleigh-cycle.png`；本讲不需要新增绘图脚本。
4. 使用 XeLaTeX 编译 `l27.tex` 两遍，渲染最终 8 页并逐页检查。

## 重点 OCR 与数学核验

- 本讲的范围核对为后续四讲暂限于实对称矩阵：
  $A=A^T\in\mathbb{R}^{m\times m}$、$x^*=x^T$、$\|x\|=\sqrt{x^Tx}$；
  特征值为实数，特征向量 $q_1,\ldots,q_m$ 标准正交。
- Rayleigh 商公式 (27.1) 核对为 $r(x)=x^TAx/(x^Tx)$；梯度公式 (27.2)
  核对为 $\nabla r(x)=2(Ax-r(x)x)/(x^Tx)$，没有把分母误读成 $x^TAx$。
- 图 27.1 与二阶精度结论核对为
  $r(x)-r(q_j)=O(\|x-q_j\|^2)$；特征向量展开后的加权平均权重是
  $a_j^2$，因此 $|a_j/a_J|\le\epsilon$ 时误差为 $O(\epsilon^2)$。
- 幂迭代 (27.4) 的归一化倍数 $c_k$、比值
  $(\lambda_j/\lambda_1)^k$ 和定理 27.1 的假设
  $|\lambda_1|>|\lambda_2|\ge\cdots\ge|\lambda_m|\ge0$ 均按源页复核；
  特征向量误差的比值幂为 $k$，Rayleigh 商误差的比值幂为 $2k$。
- 逆迭代核对为解线性系统
  $(A-\mu I)w=v^{(k-1)}$，而不是显式计算逆矩阵；定理 27.2 的收敛比为
  $|\mu-\lambda_J|/|\mu-\lambda_K|$，并保留 $q_J^Tv^{(0)}\ne0$。
- Rayleigh 商迭代算法 27.3 核对为用上一轮的
  $\lambda^{(k-1)}$ 构造 $(A-\lambda^{(k-1)}I)$；三次收敛公式 (27.6)–(27.7)
  的误差指数分别为 3，未被 OCR 误识成平方或一次幂。
- 例 27.1 的矩阵核对为
  $\begin{bmatrix}2&1&1\\1&3&1\\1&1&4\end{bmatrix}$，初值为
  $(1,1,1)^T/\sqrt3$；三次迭代值为
  $5$、$5.2131\ldots$、$5.214319743184\ldots$，目标特征值为
  $5.214319743377$。
- 运算量核对为：满矩阵下幂迭代 $O(m^2)$；逆迭代预先 LU/QR 后为 $O(m^2)$；
  Rayleigh 商迭代因每步矩阵改变，不能直接低于每步 $O(m^3)$；三对角情形
  三种迭代均为每步 $O(m)$，非对称 Hessenberg 情形为每步 $O(m^2)$。
- 习题 27.1–27.6 全部保留，尤其是复数值域 $W(A)$、非 Hermitian 情形的
  线性精度、对角矩阵化简、病态逆迭代及重特征值对图 27.1 的影响。

## 插图处理

- 图 27.1：从目标 PDF 第 219 页（原书页 204）以 300 dpi 渲染后裁切，保留
  单位球面网格与驻点，不把正文图注重复嵌入图片。
- 图 27.2：从目标 PDF 第 222 页（原书页 207）以 300 dpi 渲染后裁切，保留
  “一次逆迭代”和“Rayleigh quotient”箭头及近似 $\lambda_J$、$q_J$ 标记。
- 两幅图均为工作区最终 PNG；没有新增 Matplotlib、Python 或 Notebook 脚本。

## 编译与视觉结果

- `latex/l27.tex`：从 `translation/latex` 目录执行 XeLaTeX 两遍通过。
- 最终输出：`/tmp/l27.pdf`，共 8 页。
- 最终渲染页 `page-1.png` 至 `page-8.png` 已逐页回看；两幅插图、公式
  (27.1)–(27.7)、算法和习题均未越界。
- 最终日志未出现 `Undefined`、`Error`、`Overfull`、`Underfull`、`Warning`
  或 `Missing character`。
