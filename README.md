# Python 学习

Python 练习与本月参考书学习资料。

## 学习方法与经验

前期在 MacBook 完成 Python、NumPy、pandas、Matplotlib 和工程基础，验收后衔接小型 GPT 实践。

- [学习方法与路线](docs/LEARNING_GUIDE.md)：阅读顺序、约 21 个基础学习单元、贯穿项目和验收标准。
- [每日任务卡](docs/TASKS.md)：当前任务、验收条件与15分钟版本；定时计划检查进度后更新。
- [学习记录](docs/LEARNING_LOG.md)：逐步记录问题、原因、修改、真实验证与可复用经验。

当前文档整理的是方法和计划；练习完成情况以学习记录中的证据为准。

## 参考书

- [参考书总目录与阅读说明](local_books/README.md)
- [《Python 编程：从入门到实践（第 3 版）》](local_books/python-crash-course/README.md)：20 章与 5 个技术附录，678 个技术页面。
- [《利用 Python 进行数据分析（原书第 3 版）》](local_books/python-data-analysis/README.md)：13 章与 2 个技术附录，492 个技术页面。
- [《数值分析（第 5 版）》](local_books/numerical-analysis/README.md)：275 个章节条目，配套 LaTeX、阅读 PDF 和 322 张原页图片。
- [《Numerical Linear Algebra》中文阅读版](local_books/numerical-linear-algebra/README.md)：Trefethen、Bau 原著的现有自译稿，共 40 讲，附分讲 PDF 和校对记录。
- [转换范围与校对记录](local_books/校对记录.md)

书籍保存为可编辑 Markdown，并按各书说明提供章节索引、原页图片或插图。既有校对为 AI 对照，不代表人类逐页复核或全部代码均已运行。此次数值教材搬运只检查文件完整性与链接，未重新校对数学内容。内容权利归原作者及出版方所有。

## 练习与检查

日常 Python 练习保存在 [grammar/](grammar/)。

在仓库根目录检查两本 Python 参考书的页码和本地链接：

```bash
python3 local_books/tools/report.py
```
