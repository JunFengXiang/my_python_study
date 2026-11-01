cases = {
    "scores1": {
        "scores": [60, 80, 80, 100],
        "threshold": 80
    },
    "scores2": {
        "scores": [60, 80, 80],
        "threshold": 80
    },
    "scores3": {
        "scores": [80],
        "threshold": 80
    },
    "scores4": {
        "scores": [],
        "threshold": 80
    },
}


def summarize_scores(scores, threshold):
    count = len(scores)
    if count == 0:
        mean = None
    else:
        mean = sum(scores) / count

    above = [n for n in scores if n > threshold]
    return {
        "count": count,
        "mean": mean,
        "above": above,
        "above_count": len(above)
    }

for name in cases:
    case = cases[name]
    result = summarize_scores(case["scores"], case["threshold"])

    print(f"\n{name} 的统计结果：")
    print(f"总人数：{result['count']}")
    if result["mean"] is None:
        print("平均分：无数据")
    else:
        print(f"平均分：{result['mean']:.2f}")
    print(f"超过阈值的分数：{result['above']}")
    print(f"超过阈值的人数：{result['above_count']}")
