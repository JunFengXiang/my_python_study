# Python 学习

数值代数、数值分析与配套 Python 实践。

## P0：12 月 20 日之前的最高优先级

**自 2026-11-11 起，至 2026 年 12 月 20 日之前，每天总计两小时（120 分钟），数值代数和数值分析同步推进。** 默认两科各 60 分钟，每天都留下两科的实际进展；不能只学一科或隔天轮换。

Python/NumPy、绘图和数据整理按两科需要学习；独立的 pandas、PyTorch、小 GPT 等后移。旧 50 天计划和 12 月 15 日结项安排已被替代。执行细则见[学习指南](docs/LEARNING_GUIDE.md)，助手协作约束见 [AGENTS.md](AGENTS.md)。

## 学习方法与经验

每天用“预测或手算 → 做题或写少量代码 → 检查结果 → 自己解释”的短循环推进两科；编程工具直接用于当前课程问题。

- [学习方法与路线](docs/LEARNING_GUIDE.md)：最高优先级、每日两科时间分配、学习方法和验收标准。
- [每日任务卡](docs/TASKS.md)：两科的当前任务、时间预算和验收条件，按实际进展更新。
- [学习记录](docs/LEARNING_LOG.md)：逐步记录问题、原因、修改、真实验证与可复用经验。

当前文档整理的是方法和计划；练习完成情况以学习记录中的证据为准。

## 课程课件

- [数值代数课程课件](数值代数/README.md)：已提供 17 份 HTML 演示课件，按讲次索引；课程与考试范围以学校要求为准。

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
