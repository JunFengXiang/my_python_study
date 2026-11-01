# Lecture 14 OCR 与视觉核验记录

- 原书：Numerical Linear Algebra，Lecture 14 “Stability”。
- 原书页码：102--107。
- 目标 PDF 页码：117--122。
- 核验方式：使用 pdftotext -layout 生成候选文本，并将目标 PDF 第 117--122 页以 150 dpi 渲染，逐页比对算法映射、波浪号记号、准确/稳定/后向稳定定义、$O(\varepsilon_{\mathrm{machine}})$ 的量词和极限、维数依赖、范数等价定理及习题。OCR 无法可靠恢复的波浪号、范数分母、箭头和大写字母，以原页视觉结果为准。

## 重点纠正的 OCR 风险

1. 数学问题记为 $f:X\to Y$，算法及其计算结果记为 $\widetilde f$；方程组的计算解记为 $\widetilde x$。不能把问题 $f$ 与算法 $\widetilde f$ 的波浪号混淆。
2. 相对误差式 (14.1) 是 $\|\widetilde f(x)-f(x)\|/\|f(x)\|$，准确性式 (14.2) 是该相对误差为 $O(\varepsilon_{\mathrm{machine}})$。
3. 稳定性必须存在某个近似输入 $\widetilde x$，同时满足式 (14.3) $\|\widetilde f(x)-f(\widetilde x)\|/\|f(\widetilde x)\|=O(\varepsilon_{\mathrm{machine}})$ 与式 (14.4) $\|\widetilde x-x\|/\|x\|=O(\varepsilon_{\mathrm{machine}})$。后向稳定性式 (14.5) 则把前一误差直接收紧为 $\widetilde f(x)=f(\widetilde x)$。
4. $O$ 记号的定义是存在正数 $C$，在默认极限附近满足 $|\varphi(t)|\le C\psi(t)$。关于 $s$ 一致的式 (14.8) 要求同一个常数 $C$ 对所有 $s$ 成立；$(\sin^2t)(\sin^2s)=O(t^2)$ 是源页给出的例子。
5. 式 (14.9) 隐含 $\varepsilon_{\mathrm{machine}}\to0$，并且对所有数据 $x\in X$ 一致；具体机器上的 $\varepsilon_{\mathrm{machine}}$ 是固定量，极限应理解为满足式 (13.5)、(13.7) 的理想计算机族。
6. 维数例子是非奇异 $m\times m$ 方程组 $Ax=b$，误差界为式 (14.10)--(14.12)，隐含常数独立于 $A,b$ 但通常依赖于维数 $m$。若 $\|x\|=0$，要使用无分母形式 (14.12) 解释。
7. 源页特别指出，最坏情况下误差对 $m,n$ 的依赖通常为线性、二次或三次；原则上可能出现 $2^m$ 的维数因子，但全书只有带部分选主元的高斯消去法会遇到这种危险。实际计算中常见量级通常不超过机器 epsilon 的 100 或 1000 倍。
8. 定理 14.1 使用有限维空间中范数等价性：若 $\|\cdot\|$ 与 $\|\cdot\|'$ 是同一空间上的范数，则存在正数 $C_1,C_2$ 使 $C_1\|x\|\le\|x\|'\le C_2\|x\|$。因此准确性、稳定性和后向稳定性是否成立与范数选择无关。
9. 习题 14.1 的最后两项分别区分 $\operatorname{fl}(\pi)-\pi$ 与对所有整数 $n$ 一致的 $\operatorname{fl}(n\pi)-n\pi$；习题 14.2 要证明两个 $O(\varepsilon_{\mathrm{machine}})$ 乘积仍为 $1+O(\varepsilon_{\mathrm{machine}})$，以及其逆仍有同样形式。

## 图形资产

- 本讲原书页 102--107 没有插图或需要保留的图形资产，因此未新增 assets 文件。
- 本讲没有调用 Matplotlib；若后续讲次出现无法可靠提取的图，绘图脚本只放在 /tmp 等临时目录，工作区只保存最终 PNG/SVG。

## 译文验收范围

- 已覆盖 Lecture 14 导言、算法模型、准确性、稳定性、后向稳定性、$O(\varepsilon_{\mathrm{machine}})$ 的严格含义、维数依赖、范数独立性、定理 14.1 及习题 14.1--14.2。
- 已从读者视角补充了“正确答案/正确问题”的解释以及相对误差分母为零时的等价表述，但保留原书定义、证明和习题，不擅自补写答案。
- latex/l14.tex 已独立 XeLaTeX 编译两遍，并渲染检查 5 页；公式编号、定理证明和习题页面已逐页检查。
