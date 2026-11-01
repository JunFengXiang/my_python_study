# Lecture 13 OCR 与视觉核验记录

- 原书：Numerical Linear Algebra，Lecture 13 “Floating Point Arithmetic”。
- 原书页码：97--101。
- 目标 PDF 页码：112--116。
- 核验方式：使用 pdftotext -layout 生成候选文本，并将目标 PDF 第 112--116 页以 150 dpi 渲染，逐页比对 IEEE 数值、浮点系统定义、机器 epsilon、舍入模型、公理和习题多项式。OCR 无法可靠恢复的希腊字母、指数、运算符和不等式，以原页视觉结果为准。

## 重点纠正的 OCR 风险

1. IEEE 双精度可表示的数量级约为最大 $1.79\times10^{308}$、最小 $2.23\times10^{-308}$；区间 $[1,2]$ 的间隔是 $2^{-52}$，相邻区间 $[2,4]$ 的间隔是 $2^{-51}$，相对间隔上界为 $2^{-52}\approx2.22\times10^{-16}$。
2. 浮点系统参数是基数 $\beta\ge2$ 与精度 $t\ge1$，定义式 (13.2) 为 $x=\pm(m/\beta^t)\beta^e$；唯一尾数表示使用 $\beta^{t-1}\le m\le\beta^t-1$。OCR 容易把 $\beta$、$t$ 和 $\beta^t$ 混写。
3. 暂定机器 epsilon 是 $\varepsilon_{\mathrm{machine}}=\frac12\beta^{1-t}$。式 (13.4) 使用存在 $x'\in\mathbb F$ 的相对误差界；IEEE 单/双精度分别核对为 $2^{-24}\approx5.96\times10^{-8}$ 和 $2^{-53}\approx1.11\times10^{-16}$。
4. 舍入函数是 $\operatorname{fl}:\mathbb R\to\mathbb F$，式 (13.5) 为 $\operatorname{fl}(x)=x(1+\delta)$ 且 $|\delta|\le\varepsilon_{\mathrm{machine}}$。浮点运算记为 $\oplus,\ominus,\otimes,\oslash$，设计原则式 (13.6) 为 $x\circledast y=\operatorname{fl}(x*y)$。
5. 浮点运算基本公理式 (13.7) 为 $x\circledast y=(x*y)(1+\delta)$，其中 $|\delta|\le\varepsilon_{\mathrm{machine}}$。其含义是每次运算的相对误差至多为机器 epsilon。
6. “再次讨论机器 epsilon”部分说明：截断硬件可能需要 $2\varepsilon_{\mathrm{machine}}$；从这一处开始，机器 epsilon 定义为使式 (13.5) 和 (13.7) 成立的最小数。历史例子中的 Pentium 数值是约 $6.1\times10^{-5}$，Cray 无保护数字时可能需要 $\varepsilon_{\mathrm{machine}}=1$。
7. 复数浮点运算中，乘法与除法对应的机器 epsilon 放大因子分别为 $2^{3/2}$ 与 $2^{5/2}$；不能把两者顺序或指数误读。
8. 习题 13.3 的多项式是 $(x-2)^9$，展开式系数依次为 $1,-18,144,-672,2016,-4032,5376,-4608,2304,-512$，采样区间为 $-1.920$ 到 $2.080$、步长 $0.001$。习题 13.4 的多项式是 $x^5-2x^4-3x^3+3x^2-2x-1$，初值 $x_0=0$，目标零点约为 $-0.315$，机器精度为约 $10^{-16}$。

## 图形资产

- 本讲原书页 97--101 没有插图或需要保留的图形资产，因此未新增 assets 文件。
- 本讲没有调用 Matplotlib；若后续讲次出现无法可靠提取的图，绘图脚本只放在 /tmp 等临时目录，工作区只保存最终 PNG/SVG。

## 译文验收范围

- 已覆盖 Lecture 13 导言、数字表示的局限、浮点数系统、机器 epsilon、浮点运算基本公理、机器 epsilon 的修订、复数浮点运算和习题 13.1--13.4。
- 已从读者视角补充了“表示误差—舍入模型—运算误差”之间的衔接，但保留原书的历史说明和习题要求，不擅自补写答案。
- latex/l13.tex 已独立 XeLaTeX 编译两遍，并渲染检查 4 页；无插图，页面公式、盒装公理和习题多项式已逐页检查。
