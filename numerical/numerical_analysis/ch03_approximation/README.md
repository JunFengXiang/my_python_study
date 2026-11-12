# 第3章 函数逼近与计算作业

依据李庆扬、王能超、易大义《数值分析》第5版及2026年11月12日收到的老师作业安排。这里是助手完成的参考解答与计算复核，不代表学习者已经独立完成或掌握。

## 文件

- [老师作业安排](第3章作业安排.docx)：原附件，按字节保留。
- [必做题解答](homework.md)：4、7、9、13、17、18、20、23。
- [选做题解答](optional.md)：定理3.6、最佳平方逼近、例3.2—3.5、最小二乘过程，共7项。
- [排版解答 PDF](数值分析第3章作业解答.pdf)：含必做与选做。
- [Python 验算](verify.py)及[实际运行结果](validation.json)。

老师要求：第13题不做比较；第20题用 $f(x)=\sin(\pi x/2)$，只按 Legendre 多项式展开，不画图。第23题给出二次拟合，并单列强制 $s(0)=0$ 的版本。

## 教材依据

| 内容 | 教材入口 | 书页 |
|---|---|---|
| 必做题原题 | [第3章习题](../../../local_books/numerical-analysis/verified/sections/3.exercises.md) | 78—79 |
| 一致逼近与交错定理 | [§3.2](../../../local_books/numerical-analysis/verified/sections/3.2.md) | 47—52 |
| 法方程与定理3.6 | [§3.3](../../../local_books/numerical-analysis/verified/sections/3.3.md) | 52—56 |
| Legendre与Chebyshev多项式 | [§3.4](../../../local_books/numerical-analysis/verified/sections/3.4.md) | 57—63 |
| 正交展开与误差 | [§3.5](../../../local_books/numerical-analysis/verified/sections/3.5.md) | 63—65 |
| 最小二乘与例3.5 | [§3.6.1](../../../local_books/numerical-analysis/verified/sections/3.6.1.md) | 65—67 |

已对照原扫描的相关页。页码以书页为准：仓库原页图的编号比本次取得的323页PDF物理页序少1，例如书页78对应仓库 `pdf-091.jpeg`、本次PDF第92页。

例3.2的舍入误差、例3.3的定理引用以及例3.5的系数不一致，已在选做解答中明确说明，未改动教材文件。

## 运行验算

Python 3.11+，唯一外部依赖为 NumPy：

```bash
python -m pip install numpy
python numerical/numerical_analysis/ch03_approximation/verify.py
python numerical/numerical_analysis/ch03_approximation/verify.py --json numerical/numerical_analysis/ch03_approximation/validation.json
```

使用解析条件、精确分数、残差正交性、128/256点 Gauss-Legendre 积分及 NumPy 最小二乘交叉复核。程序不生成图像。

## 重新生成 PDF

需要 Pandoc，另安装 Python 包 `reportlab ziamath svglib pymupdf`。`build_pdf.py` 将显示公式转为 SVG 路径、行内公式转为高分辨率图片，由 ReportLab 排版；无需浏览器或在线公式资源。在本目录运行：

```bash
python build_pdf.py
```
