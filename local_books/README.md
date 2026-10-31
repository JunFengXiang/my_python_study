# 学习参考书：Python、数值分析与数值线性代数

这里整理 Python 与数值课程使用的四本参考书，保存可编辑 Markdown、阅读索引及既有校对记录，收录在 `my_python_study` 仓库的 `local_books/` 目录中。各书的附件、收录范围与验证程度见各自说明。

书籍内容的权利归原作者及出版方所有，本仓库用于个人学习，不附加开源许可证。

- [《Python 编程：从入门到实践（第 3 版）》](python-crash-course/README.md)：Python 基础、练习与项目。
- [《利用 Python 进行数据分析（原书第 3 版）》](python-data-analysis/README.md)：NumPy、pandas、绘图及数据分析。
- [《数值分析（第 5 版）》](numerical-analysis/README.md)：李庆扬、王能超、易大义；[275 个章节条目](numerical-analysis/index/INDEX.md)、542 个编号公式、322 张原页图片及全书 Markdown/LaTeX/PDF。
- [《Numerical Linear Algebra》中文阅读版](numerical-linear-algebra/README.md)：Trefethen、Bau（SIAM，1997）原著的现有自译稿；[40 讲目录](numerical-linear-algebra/INDEX.md)、全书 Markdown、分讲 PDF 和第 6–40 讲独立 LaTeX。

两本数值教材保持原拆解稿的收录范围，包含书前材料与附录。本次仅整理阅读入口、修复搬运后的链接并核对文件完整性；旧校对与编译记录随书保留，不代表本次重新执行或人工逐页审校。原扫描 PDF、虚拟环境和临时编译产物不上传。数值分析保留全部原页图像；数值线性代数保留已有插图与页码映射。

## 两本 Python 参考书的范围与检查

两本 Python 参考书的转换范围以技术正文、练习和技术附录为主；前言、版权页、推荐语和致谢等非技术部分不收录。页面编号采用原 PDF 的页码，便于回到源文件核对。

**阅读提示：**纳入范围的技术页面已由 AI 对照原页整理为可编辑正文、代码和公式。每页保留本地原页画面，以便核对代码、公式和图表；代码能否运行取决于上下文及软件版本，只有明确注明运行结果的示例才经过执行验证。这些记录不表示人类逐页审核。[查看处理范围与校对记录](校对记录.md)。

在 `my_python_study` 仓库根目录运行 `python3 local_books/tools/report.py`，可查看两本书已校对和待校对的 PDF 页码，以及链接和页码完整性检查结果。运行 `python3 local_books/tools/check_code.py` 可扫描 Python 代码片段的语法提示。

部分 `ipython` 代码块保留了原书的 `In [数字]:`、`Out[数字]:` 交互提示和输出，用于展示原始会话；复制到普通 `.py` 文件时，需要分离输入、输出和提示符。书中的 `--snip--` 表示省略的上下文，也不是可直接运行的 Python 语句。

建议先按需要快速复习列表、字典和函数，然后以《利用 Python 进行数据分析》的 NumPy、pandas 和绘图章节为主线；基础有疑问时，再回到第一本对应章节。
