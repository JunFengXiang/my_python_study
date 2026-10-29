# 50天逐日计划：从文件数据到数值与AI实验

更新：2026-10-30。执行规则见[学习指南](LEARNING_GUIDE.md)，下一次详细输入见[当前任务](TASKS.md)。这是建议进度，不是完成清单。原周期为2026-10-27—12-15，每天最多120分钟；不重新起算。

## 怎样使用

每天读一个目标，完成2—3个相连动作，留下真实输出和简短解释。表中的选做最多取一项；核心提前完成可进入下一单元。每张实际任务卡只给当天所需1—2处阅读。所有未来数据路径均为**拟创建路径**：助手在发卡时先提供小数据文件或明确生成步骤，学习者的正式程序从文件读取，不能把不存在的文件当作已交付。测试可保留小样例，正式输入与测试分开。

前三次记录实际用时和卡点；基础单元太轻就合并，过重就减少新概念。D21、D31、D44留作缓冲；D45—50保留实验与结项。日期变化不代表自动过关，仍于12月15日按真实成果结束。

## 已发生的三天

| 日历日 | 可确认状态 |
|---|---|
| D1 · 10/27 | Python基础起步，讨论列表、均值、阈值筛选与返回字典；实际学习用时未记录。 |
| D2 · 10/28 | PY01任务卡已发出；不能据发布任务就标记完成。 |
| D3 · 10/29 | 学习分支已有`grammar/10_27/10_27_test.py`及配套笔记。10月30日本轮复跑5类输入通过，输入未被修改；这验证程序行为，不替代本人理解检查。 |

## 第一段：文件输入、数组与第一张图（Mac）

贯穿输入先采用可手算的教学函数f(x)=x²。`nodes.csv`含case_id,x,y，每例两个节点；`queries.csv`含x,y_reference。参考值只用于评估，不传入插值算法。后续三案例的共同查询范围位于各节点区间交集。D4开始的最小CSV见当前任务；其余数据包到任务发布时准备。前段每一天增加不同的实做能力：例如D6验收通过且用时不足60分钟，当天直接开始D7；已掌握内容允许合并，不要求同一公式机械练七天。

| 日期／任务 | 当天目标与三个动作 | 输入→产出 | 验收、选做与负荷 |
|---|---|---|---|
| **D4 10/30 · PY02** | 从文件做第一次插值：①读 nodes 与 queries，确认字段和数值转换；②自己写两节点插值函数，批量计算查询点；③核对两端节点，解释一个内部点的结果。 | 助手预备的一组 nodes.csv、queries.csv → 可运行脚本与控制台结果。今天不强求图、保存表和pytest一起完成。 | 两端复现节点值；修改输入文件后结果随之改变；重复横坐标明确不能算。选做：读取另一节点区间，比较一个内部点误差。主要新知识是文件输入，数学公式只做必要回顾，约90—120分钟。阅读：P10的10.1.1—10.1.2，PDA6的6.1.3中csv读取示例。 |
| **D5 10/31 · NP01＋VIZ早用** | 把查询点数组化：①从文件得到ndarray，写明shape/dtype并提取两列；②让插值函数一次处理整列查询点；③借助最少Figure/Axes示例画节点、插值线、参考曲线并保存第一张图。 | 沿用输入 → 数组版预测、interpolation.png。 | 与D4逐点循环结果一致；能解释切片取列；图的数据来自实际计算。选做：通过一次切片修改比较view与copy。先学数组和向量化；绘图只会改数据、轴标签及保存即可。阅读：PDA4 4.1.1—4.1.4选段；PDA9 9.1.1与9.1.5必要例子。 |
| **D6 11/01 · NP02** | 形成真正的误差表：①对助手补充的三组节点分别运行；②堆叠成“案例×查询点”误差矩阵，沿axis求每例最大/平均绝对误差；③用掩码找超过阈值的查询点并打印案例与位置。 | 三个案例＋共同queries → 各案例误差摘要与一个失败定位示例。 | 先手算2×3缩小矩阵检查axis；零误差和空筛选不误判；参考值来自同版数据。选做：记录各列误差以发现困难查询点。新增axis与掩码，数学不另加内容。阅读：PDA4 4.1.5、4.4.2—4.4.3。 |
| **D7 11/02 · NP03** | 批量计算且不混淆维度：①将共同查询点整成(1,n)、各案例节点值整成(k,1)；②广播得到(k,n)预测并与D6循环版核对；③对案例误差做中心化，解释keepdims的作用。 | 同一份三案例输入 → 批量预测数组、形状注释和数值核对。 | 不运行先写出中间shape；故意遗漏一个单例轴时能定位问题；核对只比较同一数据和误差定义。选做：换查询点数量而不改核心计算。广播是当天难点，不再加新算法。阅读：PDA附录A A.2.1、A.3—A.3.1。 |
| **D8 11/03 · NP05** | 把节点约束写成线性系统：①从已有节点文件为每例建立2×2系数系统；②用np.linalg.solve求直线系数，以@批量预测；③用列的线性组合核对矩阵乘法，并保存/重载一个数组。 | 原节点与查询文件 → 系数、矩阵版预测与一个.npy结果。 | 写清各矩阵shape；能区分*与@；节点约束与D7预测一致。本次调用solve不等于独立实现消元。选做：迁移为X@W+b。阅读：PDA4 4.6、4.5。 |
| **D9 11/04 · NP04** | 检查精度和输入扰动：①读取助手预备、明确标注扰动量的第二份节点文件；②用同一算法比较原/扰动输入及float32/float64；③记录误差和失败状态，解释观察到的差异或差异不明显。 | 原节点、独立perturbed_nodes.csv及同版reference → 真实的精度／扰动对照结果。 | 不覆盖原数据；区分插值误差与扰动造成的变化；不预设float64必然显著更好。选做：提供一个精度转换使节点重合的小反例并报告失败。随机数据若使用，由准备步骤记录seed，核心程序仍读文件。阅读：PDA4 4.1.2、4.3—4.4相关选段。 |
| **D10 11/05 · NP06＋ENG起步** | 把一周代码变成可交接的小实验：①从指定输入文件完成运行，不依赖Notebook旧变量；②保存最少参数表与长格式误差表，点级预测表有余量再加；③读取一份新节点文件重跑，核对图与输出来自新数据。 | 已完成算法＋新输入 → runs.csv、metrics.csv、一个可重跑入口与简短README（predictions.csv选做）。 | 结果ID能关联输入与图；三组中选一组手算复核；冷启动可跑。选做：给重复节点或空查询增加一条自动检查。今天主线为整合与换输入，不引入新数值方法。阅读：P10 10.4.3、PDA6 6.1.2—6.1.3写出示例。 |

## 第二段：方法对照、实验表和模型入口（Mac）

D11换用明确标注教学生成的sin(x)案例（x单位为弧度），不要混用前段x²的参考表。D12扫描可从固定目标点0.3367、4个h开始，线性与二次方法使用各自规定节点、相同目标与h；目标点不与节点重合。所有正式节点和参考表先保存，再读取；参考列来自注明版本的数值计算，不称为解析精确数值。只解释实际观察到的误差，不要求证明整套误差界。

结果起步保留run_id/method/dtype/status，h与舍入条件需要时才加。参数表与指标表分别保存；清洗练习使用标注过的副本，不篡改原结果。D18仅做一个线代迁移检查，QR/SVD等不同时追加为必修。

| 日期 | 当天目标与动作 | 输入→产出 | 通过检查 | 阅读与一项选做 |
|---|---|---|---|---|
| **D11 · 11月6日** | **同一份节点数据比较两种插值**。①读取助手拟提供的三节点案例及查询点；②自己实现三点基函数并在节点上验证，复用原线性方法；③用同一目标点生成两种方法的预测与误差，保存结果。 | 拟新增 `data/interpolation/nodes_quadratic.csv`（case_id,x,y）与对应queries.csv → 本人运行的预测表与一张叠加图。输入标注教学生成和参考来源。 | 三个节点值在合理浮点容差内重现；目标点不是节点；改变节点值能改变输出；只在本组数据上评价优劣。 | [数值分析§2.2.2][N222]线性与抛物插值；公式已实际核对。 选做：比较一个区间外查询点，明确标注外推。 |
| **D12 · 11月7日** | **从单次结果到参数扫描**。①读取拟提供的节点间距配置与按规则生成的输入文件；②复用两种算法批量运行4个h，生成唯一run_id；③保存参数表、指标表和失败状态，检查手选一组与单次运行相同。 | `configs/interpolation_scan.json`及正式节点文件 → `results/interpolation/runs.csv/metrics.csv`。8次运行起步，速度充分时再比较节点舍入。 | 配置与输出逐项对应；运行数可预测；失败结果不记为零误差；更换h无需改算法函数。 | [数据分析6.1.2、6.1.4][B6]；复习[N222]。 选做：增加完整精度与6位小数输入对照。 |
| **D13 · 11月8日** | **把自己的运行记录读成实验表**。①用pandas读取自己生成的CSV，检查字段、类型、行数；②用loc/iloc及条件筛选找到指定方法、h和run；③与原NumPy输出核对，导出一张便于查看的选择结果表。 | D12真实结果CSV → `results/analysis/selected_runs.csv`与字段说明。 | 打乱行索引后仍按run_id找对实验；能解释位置与标签的区别；行数与运行数对账。 | [5.1.2、5.2.3][B5]；CSV参数按[6.1][B6]按需查。 选做：把同一筛选封装成接收DataFrame的函数。 |
| **D14 · 11月9日** | **处理不完整记录，保证对应关系**。①在原结果副本上检查缺失和重复键；②对助手拟提供、明确标注“清洗教学副本”的坏记录输出问题表，保留原因；③按run_id对齐两份顺序不同的记录，检查对齐后缺失来源。 | 真实原始结果＋独立教学副本 → `clean_metrics.csv/issues.csv`，原文件保持不变。 | 零误差保留；失败次数仍能统计；重复记录有处理说明；打乱顺序不改变正确匹配。 | [7.1、7.2.1][B7]；[5.2.4][B5]。 选做：读取一个误写为字符串的数值列并报告无法转换的行。 |
| **D15 · 11月10日** | **合并参数与指标，检查是否多算漏算**。①concat两批本人结果并检查run_id冲突；②按run_id合并参数和指标，声明一对多/多对一关系；③检查未匹配行、空键、合并前后行数，导出合并表。 | 两批runs/metrics CSV → `analysis_long.csv`与合并核对结果。 | 不能因重复键意外扩行；不能通过inner join悄悄丢掉失败/未匹配项；每个指标能找到唯一运行参数。 | [8.2.1、8.2.3][B8]；[pandas.merge官方说明][MERGE]。 选做：加入一个重复参数键，确认校验能发现。 |
| **D16 · 11月11日** | **汇总与公平比较**。①按已有method/h分组统计有效数、失败数和误差；②比较size/count并与原表对账；③仅用一种pivot准备方法对照表，遇重复键先追查原因。 | analysis_long.csv → summary.csv与plot_table.csv；precision只有实际记录过才加入分组。 | 总数与有效/失败/缺失的约定能说明；同条件比较；不靠默认平均掩盖重复键。 | [10.1—10.2][B10]、[8.3.2—8.3.3][B8]按需各读一段。选做：melt转回长表；未完成移到D17开头。 |
| **D17 · 11月12日** | **画出误差现象并解释**。①从汇总CSV读取绘图输入；②完成误差-h对数图与一张局部拟合/残差图；③打开导出图片检查标注、图例、参考来源，写3句基于实际结果的解释。 | 汇总表/预测表 → 最多2张PNG或PDF与简短说明。 | 单位清楚、不同方法同坐标；零值与非正值在对数图中有明确处理；不靠图片看起来重合宣称误差为零。 | [9.1.1、9.1.3/9.1.5按需选][B9]；[Axes.loglog][LOGLOG]。正式任务只选当天确需的1—2处。 选做：在适用区间估计经验收敛斜率，不要求它在所有h上严格等于理论阶。 |
| **D18 · 11月13日** | **线性代数中的残差与解误差**。①读取助手拟提供的小矩阵、右端项与明确标注的参考解；②求解并分别计算残差、解误差，比较一组受控右端扰动；③沿用同一CSV和绘图流程记录结果，解释两种误差的含义。 | 拟新增 `data/linear_systems/A.csv/b.csv/x_reference.csv`与扰动说明 → 小结果表和一张比较图。 | shape一致；已知参考解用于验算而非算法输入；能解释小残差为何不能单独保证小解误差；容差随数据尺度说明。 | [NumPy solve][SOLVE]；课程范数/条件数材料按当天实际课件选段，不编造页码。 选做：比较良态与病态的两个小例子。 |
| **D19 · 11月14日** | **把实验连成一个入口**。①从已有代码拆清读取/计算/汇总/绘图职责；②用一个入口连接已有函数，路径和参数从配置读取；③在独立结果目录重新运行，检查输出及必要依赖说明。 | 既有正式输入＋配置 → 一个可重跑入口、完整结果目录和简短运行说明。 | 新进程可运行；没有依赖Notebook隐藏变量；重新运行不会覆盖原始输入；能指出每张图来自哪张表。 | 复用已核验的6.1.4 JSON与前述API；代码组织按已有函数知识补，不新开框架课。 选做：输入缺文件时给出明确报错。 |
| **D20 · 11月15日** | **换数据独立验收**。①读取助手当天准备的第二套未见过节点/查询文件；②先预测形状、输出数量及一个可手算检查，再运行；③定位一个有意设置的输入问题并修正读取策略，记录新结果和差异。 | 新的正式教学输入 → 独立运行结果、问题定位记录。 | 无需改算法内硬编码数据；能找到重复节点或字段缺失；说明新结果与旧结果的差异来自什么条件。 | 只回查实际卡住的1—2处已有小节，不要求新增章节。 选做：在不看旧函数实现的情况下重写一个关键计算函数并对照。 |
| **D21 · 11月16日** | **补欠与经验固化**。①根据D20证据选择一个明确卡点；②做一个更小复现并修好，补一项有效检查；③重跑主实验，把问题—原因—验证写成短记录。 | 既有失败输入/代码 → 修复、实际输出、短经验记录。 | 原失败可复现，修复有证据，解释能迁移；若前面均通过，改为给入口做一次陌生参数压力检查。 | 卡点对应的小节，发布任务时再精确指定。 选做：仅在已过关且时间充分时，做课程当前QR/SVD等一个小演示；不设为必修。 |
| **D22 · 11月17日** | **从实验表到模型输入**。①读取助手拟提供的带sample_id的独立同分布教学回归CSV，明确特征列与目标列；②按样本ID保存训练/验证/测试划分，仅用训练部分计算特征标准化参数；③转换为固定顺序与dtype的X/y数组，保存划分和预处理参数，检查行对应。 | 拟新增 `data/regression/samples.csv`（sample_id,x,y）与生成说明 → `split_ids.json/preprocess.json`及数组形状记录。建议用256个独立同分布x∈[-π,π]，y=sin(x)+已说明的小噪声；生成器、噪声尺度、种子由助手在当天资料中明确记录。特征顺序固定为["x"]，目标为"y"，sample_id只作索引而非特征；X形状(N,1)、y形状(N,1)或(N,)由后段统一选择并保持一致。数据明确标注教学生成，不宣称真实观测；不能把不同实验参数表错误当监督学习样本。 | ID无交叉且全集覆盖；目标列不混入特征；验证/测试不影响均值方差；重新读取划分得到相同样本。 | [12.1][B12]；[官方数据泄漏说明][LEAK]。 选做：调整CSV列顺序，检查特征顺序仍受显式列名控制。 |
| **D23 · 11月18日** | **设备与文件交接**。①当天查官方安装说明，在5080建立独立环境、通过Git同步代码并单独复制必要数据；②确认D22文件/划分可读，运行小tensor并记录dtype/device；③用10分钟结合已有结构认识self和__init__，继承/super留到D26。 | 代码、数据、配置 → 环境记录与小tensor输出；不复制.venv，不启动长训练。 | 解释器与文件路径明确；CPU或GPU小运算通过。CUDA排障约30分钟仍无进展时先CPU继续，状态如实记录。 | 入门书9.1需当天实际打开；PyTorch安装按当天官方说明。选做：干净终端重跑。 |

## 第三段：PyTorch、小GPT和完整对照（基础过关后转5080）

复用D22的回归CSV、固定划分和预处理参数，避免另开一套高斯分类项目。现有ToyMLP仅作结构参考，回归任务使用合适的输出维度、MSE/RMSE，不沿用分类准确率验收。测试集封存到D48；此前只用训练和验证。

已有文本示例引用的the-verdict.txt不在已核对的仓库树中，D32须先落实授权文本与真实文件。文本先分割再切窗口。默认1—2层小GPT；模型/上下文规模按短运行估时调整，主动学习仍限120分钟，训练等待单独记录。D44若GPT尚不能可靠重跑，最终对照使用已成熟的MLP，保留GPT真实进度，不延长截止日。


| Day / 日期 | 一个目标与三个连续动作 | 输入 → 产出（未来拟创建项按需落地） | 通过检查 | 精读 / 选做（最多一项） |
|---|---|---|---|---|
| 24 / 11-19 | 建立线性拟合参考并认识自动求导。①读取D22训练划分及固定预处理，用NumPy lstsq拟合带截距的线性基线；②将同一小样本转tensor，核对shape并比较手算/自动梯度；③做少量梯度更新，观察MSE向最小二乘参考靠近。 | D22训练X/y与固定预处理 → 训练集拟合的基线参数、梯度检查与短loss记录 | 验证/测试不参与拟合；手算梯度一致；有限步不要求严格收敛。若过载先保存lstsq参考和一次正确更新，后续循环并入D27。 | P1、P2；lstsq接口查NPLS。选做：无额外主题 |
| 25 / 11-20 | 把文件化回归数据接入训练。①读取D22的CSV、split_ids与preprocess，只应用已保存的训练集变换；②固定特征列次序并构建TensorDataset/DataLoader；③检查shuffle和最后一批。 | D22的 `data/regression/samples.csv`、`split_ids.json`、`preprocess.json` → 文件读取器、批次检查 | 三组ID不相交且覆盖原数据；特征与回归目标为浮点；训练与验证特征列顺序一致，尾batch计数明确 | P3、R2；选做：检查不同batch_size下样本计数 |
| 26 / 11-21 | 自己写小回归MLP。①结合nn.Module补self、__init__、继承与super；②实现Linear-ReLU-Linear，输出一维预测；③核对预测与目标形状，再计算MSE。 | D25文件batch、拟小配置 → 自己的回归模型和前向输出 | 预测与y均为(batch,1)，无意外广播；loss有限；能解释参数与模块关系。 | R3、P4；类语法仅查当天所需。选做：比较隐藏宽度与参数量 |
| 27 / 11-22 | 写通训练更新。①独立写zero_grad/forward/loss/backward/step；②确认梯度与参数确实变化；③只拟合一个训练batch并画loss。 | 固定训练batch → 训练循环、单batch曲线 | 固定极小batch的loss显著下降；梯度与参数更新正确；不强求分类准确率，也不把此结果作为泛化证据 | P4、R4；选做：故意漏zero_grad后解释现象，随后恢复 |
| 28 / 11-23 | 得到可信训练/验证指标。①扩展到全训练集；②实现eval/no_grad、按样本数累计MSE并计算RMSE；③复用整理绘图流程，与D24仅在训练集拟合的线性基线及训练y均值常数基线比较。 | D22固定划分、D24基线 → metrics.csv、train/val曲线、基线表 | 尾batch计数正确；各方法使用相同split与指标；验证不更新参数，测试集封存。 | P4、R5；选做：查看残差随x的分布 |
| 29 / 11-24 | 让实验能中断后接着运行。①保存config、模型、优化器、step与最佳验证值；②新进程加载，再继续几个step；③比较加载前后固定输入预测。 | D28运行 → `last.pt`、`best.pt`、恢复记录 | 保存/加载后的eval预测一致；optimizer与step恢复，不把重启说成续训 | P5、R4；选做：保存随机数状态；不要求本日实现逐位续训 |
| 30 / 11-25 | 做第一个小模型对照。①只改变学习率，固定数据与步数；②每次运行重新初始化，同一配对seed用相同初始权重和样本顺序，B不能接着A续训；③仅用验证结果比较，保存简短结论，测试集继续封存。 | 两个小配置、固定划分 → A/B结果表与最多两张图 | 数据划分seed与训练seed分开记录；不能把训练改善当泛化改善；无差异照实报告。 | R6、R5；选做：第二个配对seed检查波动 |
| 31 / 11-26 | 缓冲与MLP迁移验收。①补最影响可信度的缺口；②清理输出后按说明从文件重新运行；③口述一条样本如何变成loss与更新。无欠账则换一份小CSV验收。 | MLP完整流程 → 一条可重跑命令、简短运行说明 | 数据→训练→验证→保存→重载均可复现；否则后续模型规模下调 | R1、R5；选做：无新增主题 |
| 32 / 11-27 | 落实文本文件与分割。①选本人、明确授权或公版文本，保存并登记来源；②检查编码、重复与长度；③先按文档分train/val/test（单文档用不重叠区间），冻结清单，并确认各份足以形成窗口。 | 拟data/text/raw/*.txt与manifest → 实际文本文件、固定split与长度统计；以可获取的数万字符起步，规模不足则缩短context。 | 输入真实存在，来源清楚；划分无交叉；窗口不能跨文档或split边界，语料极小的结论限于教学。 | R7、R5；选做：检查各文档长度差异 |
| 33 / 11-28 | 从文件生成next-token样本。①默认字符tokenizer，词表只从训练文本建立并预留UNK；②冻结词表、统计验证未知率，在各split内切输入/右移目标；③核对长度、步长、尾窗口。验证/测试默认不重复计目标token，尾段规则固定。 | D32文本文件 → vocab约定、窗口Dataset和计数记录；已有条件适合时才用预训练BPE替代。 | token0—11、长度4步长2可手算核对；未知字符有明确处理；窗口不跨split，不用验证/测试扩充词表。 | R8、P3；选做：步长改3并核对样本数 |
| 34 / 11-29 | 把词元批次变为嵌入。①DataLoader读取窗口；②实现token与位置嵌入；③核对(batch,context,embedding)及位置上限。 | token批次 → 嵌入模块、形状检查 | 同一token不同位置的表示可解释；token ID越界被发现 | R9、R7；选做：记录embedding参数量 |
| 35 / 11-30 | 实现单头注意力。①在3词元小矩阵上计算Q/K/V；②写缩放点积、softmax与加权求和；③与参考计算逐项比较。 | 固定小tensor、嵌入batch → 注意力实现 | 维度正确；每行注意力和约为1；小样例数值对齐 | R10、O1第3章入口；选做：可视化一张注意力矩阵 |
| 36 / 12-01 | 加入因果约束。①实现上三角mask；②验证未来token权重为0；③修改后方token，检查前方输出不变（eval下）。 | D35模块 → 因果注意力、行为检查 | 不能看到未来；无全mask导致的NaN；检查具有实际因果意义 | R10、O1第3章入口；选做：比较mask放在softmax前后的结果 |
| 37 / 12-02 | 把单头扩展成多头。①拆分并转置head维；②合并heads并投影；③检查head数整除与不同batch/context。 | D36模块 → 多头注意力 | 输出保持(batch,context,embedding)；head=1时可与单头对照 | R10、O1第3章入口；选做：查看连续性与reshape关系 |
| 38 / 12-03 | 构建Transformer Block。①核心使用nn.LayerNorm并解释归一化轴；②接前馈层和残差；③检查真实batch的一次反向传播。 | D37输出 → 单个Block | 输入输出形状相同，梯度有限；残差相加条件正确。 | R11、O1第4章入口；选做：独立实现小LayerNorm并与库核对 |
| 39 / 12-04 | 组合最小GPT。①连接embedding、1—2个Block、最终norm与词表头；②输出logits并统计参数；③用真实文件批次做前向和loss。 | D33批次、拟 `configs/tiny_gpt.json` → 小GPT | logits=(batch,context,vocab)；目标右移与交叉熵对应；没有以训练结果证明架构正确 | R11、O1第4章入口；选做：列出主要激活张量大小 |
| 40 / 12-05 | 让GPT先拟合极小样本。①复用MLP训练流程，只更换batch与loss接口；②训练单batch；③检查loss下降、梯度、padding/有效token计数（如使用）。 | 固定文本batch → GPT训练入口、调试曲线 | 单batch可明显拟合；错误先按数据→loss→梯度定位，不盲目加层 | R12、R5；选做：对照均匀预测loss量级 |
| 41 / 12-06 | 扩展到训练/验证集。①在固定split上短训练；②按约定有效目标token数汇总验证loss；③保存step、tokens_seen、lr、耗时和状态。 | D32/33文件数据、配置 → 真实训练日志 | 验证文本与训练分割无交叉；目标token计数与尾段规则一致；不宣称相邻窗口统计独立，不删除失败run美化结果。 | R12、R6；选做：画loss对tokens_seen图 |
| 42 / 12-07 | 生成与恢复检查。①实现逐token贪心生成，处理context截断；②保存并重载GPT checkpoint；③用固定prompt比较恢复前后输出。 | GPT checkpoint、拟固定prompt文本 → 生成样本文件、恢复记录 | eval下固定prompt可重复；续训恢复optimizer/step；生成流畅度不替代验证loss | P5、R12；选做：只加入temperature一个采样参数 |
| 43 / 12-08 | 建立正式基线运行。①冻结小配置、数据版本与预算；②估时后跑一个短基线；③检查日志、曲线与固定prompt样本并登记异常。 | 固定数据与配置 → 基线run及一页以内观察 | 产物可追溯到配置/commit；验证loss与样本都保存；测试集仍未用于调参 | R6、R12；选做：查看tokens/s，不做性能优化项目 |
| 44 / 12-09 | 缓冲与最终实验定型。①修复阻塞问题；②完成一次干净重跑；③决定最终对照使用GPT或已成熟的MLP，冻结问题与衡量指标。 | 已有成果 → 最终实验方案 | 有可重复运行的基线才做对照；GPT未达标时选择MLP结题并如实列进度 | R1、R5；选做：无新增模型主题 |
| 45 / 12-10 | 固定单变量实验与选择规则。①选两个学习率，固定数据/模型/训练预算/评估频率；②准备A/B各3个配对seed，每次重新初始化，配对初始权重与样本顺序相同；③预先固定按验证指标选配置/checkpoint的规则，短运行检查。 | 基线配置 → 2×3实验清单与选择规则 | 仅学习率不同，B不续训A；划分seed与训练seed分开。GPT按相同token预算，MLP按相同样本/step预算；失败同样登记。 | R6、P6；选做：写出支持或否定假设的结果 |
| 46 / 12-11 | 执行小规模配对对照。①按清单跑A/B；②检查每个run的配置和完整日志；③保留失败原因。运行过慢先等比例缩短所有配置预算并重跑，不能只缩某一组。 | D45清单 → 原始run结果 | 每个配置/seed唯一对应结果；目标为3对短run，资源不足至少2对并明确局限 | R6；选做：无额外搜索超参数 |
| 47 / 12-12 | 分析结果及不确定性。①用已有pandas流程合并run与metrics；②报告各seed结果和均值/波动；③画一张公平对齐的曲线和一张汇总图，解释失败/无差异。 | D46真实记录 → 汇总CSV与图 | 不只挑最好一次；样本数少不做夸大显著性结论；计算预算一致 | R6；选做：检查一个异常run的原始日志 |
| 48 / 12-13 | 冻结最终方案并独立评估。①只根据验证结果选配置，按D45规则固定各重复运行的checkpoint；②首次评估预留测试集，报告所选配置各seed结果；③从新输出目录重载checkpoint重生成评价与图表。 | 冻结checkpoint、配置、测试文件 → 最终评估表与评价复现记录 | 看测试后不换配置、checkpoint或最好seed；重载评价不称为完整训练复现，后者如未做就明确。 | R1、P6；选做：按README由新进程复现评价 |
| 49 / 12-14 | 写出完整实验结论。①用问题/数据/方法/对照/结果/限制组织1—2页；②插入必要表图与复现命令；③核对每句话都有数据或明确推测。 | 结果表图 → 简洁报告、README补充 | 读者能知道改了什么、效果如何、哪些结论不能推出；保留无效结果 | R6、R13；选做：删去一段重复说明 |
| 50 / 12-15 | 独立验收与结项。①抽查一个核心函数解释/变式实现；②从原始文件做一次极短训练以检查入口，并独立重载最终checkpoint复现评价；③列已完成、未完成、常见错误与下一阶段前置。 | 代码、数据说明、报告 → 结项清单 | 区分参考代码运行、独立实现、短运行检查与完整训练复现；未验证项不补造，到期总结，不自动续期。 | R1、R13；选做：只整理现有成果 |

## 阅读索引

两本书的相关正文和数值插值小节已由分工组实际核对。第一段使用的简写：P10=[入门第10章][P10]，PDA4=[数据分析第4章][PDA4]，PDA6=[第6章][PDA6]，PDA9=[第9章][PDA9]，PDA附录A=[附录A][PDAA]。本版4.2是随机数、4.3是ufunc；CSV在6.1.3，广播在A.3。具体API按实际安装版本核验，转写错误不算学习者错误。

D23的入门书9.1、D26的9.3与设备安装组合在执行当天再打开核验，不锁定未来版本。AI段的来源如下；只读当天需要的函数或小节。

每天只读表中关联的一小段。以下链接为已读取的现有资源；官方章节入口用于按当天模块寻找示例，不要求逐章抄写。

- P1：[PyTorch Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
- P2：[PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- P3：[PyTorch Datasets & DataLoaders](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)
- P4：[PyTorch Optimization Loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- P5：[PyTorch Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)
- P6：[PyTorch Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html)（已跟随重定向核验；执行时按安装版本阅读）
- NPLS：[NumPy lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html)
- O1：[作者官方 LLMs-from-scratch 仓库](https://github.com/rasbt/LLMs-from-scratch)（已读根页；ch03/ch04/ch05目录网页本轮抓取受限，不能声称已深读这些章节代码）
- R1：[既有路线与验收](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/docs/ROADMAP.md)
- R2：[既有数据生成与加载](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/src/llm_from_scratch_lab/data.py)
- R3：[既有 ToyMLP](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/src/llm_from_scratch_lab/models.py)
- R4：[既有训练检查](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/tests/test_training.py)
- R5：[调试清单](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/docs/DEBUGGING_CHECKLIST.md)
- R6：[工程规范](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/docs/ENGINEERING_GUIDE.md)
- R7：[文本阶段入口](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/chapters/02_text_data/README.md)
- R8：[现有滑动窗口示例](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/examples/ch02_text_data/sliding_window.py)
- R9：[现有位置嵌入示例](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/examples/ch02_text_data/positional_embedding.py)
- R10：[注意力阶段入口](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/chapters/03_attention/README.md)
- R11：[GPT阶段入口](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/chapters/04_gpt_model/README.md)
- R12：[预训练阶段入口](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/chapters/05_pretraining/README.md)
- R13：[实验记录模板](https://github.com/JunFengXiang/llm-from-scratch-lab/blob/main/experiments/template.md)

[B5]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/05.md
[B6]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/06.md
[B7]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/07.md
[B8]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/08.md
[B9]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/09.md
[B10]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/10.md
[B12]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/12.md
[N222]: https://github.com/JunFengXiang/numerical-computing-lab/blob/main/numerical-analysis/book/verified/sections/2.2.2.md
[MERGE]: https://pandas.pydata.org/docs/reference/api/pandas.merge.html
[LOGLOG]: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html
[SOLVE]: https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
[LEAK]: https://scikit-learn.org/stable/common_pitfalls.html
[PDA4]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/04.md
[PDA6]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/06.md
[PDA9]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/09.md
[PDAA]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-data-analysis/chapters/14.md
[P10]: https://github.com/JunFengXiang/my_python_study/blob/study/mac-data-analysis/local_books/python-crash-course/10_第_10_章_文件和异常.md

## 两轮规划后的必要修订

第一轮由Python/数据、数值/绘图、AI训练和任务负荷四组分工，再由AI教学、计算机教学与负荷审查分别复核。本轮仅补关键依赖与删减过载：D24落实真正的训练集线性基线；D23把继承放到实际写模型时学；D38默认库LayerNorm；字符词表只使用训练文本；配对对照固定初始化和选择规则；D48明确评价复现与完整重训的区别。未新增课程、模型方向或额外学习时长。
