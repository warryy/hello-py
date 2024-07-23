def hanoi(n, source, target, auxiliary):
    """
    解决汉诺塔问题的函数。
    
    圆盘编号从 1 到 n, 顺序为从上到下。

    :param n: 圆盘数量
    :param source: 起始柱子
    :param target: 目标柱子
    :param auxiliary: 辅助柱子
    """
    if n == 1:
        print(f"将圆盘 1 从 {source} 移动到 {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"将圆盘 {n} 从 {source} 移动到 {target}")
        hanoi(n - 1, auxiliary, target, source)


# 调用函数解决三层汉诺塔问题
hanoi(3, "A", "C", "B")

"""
将圆盘 1 从 A 移动到 C
将圆盘 2 从 A 移动到 B
将圆盘 1 从 C 移动到 B
将圆盘 3 从 A 移动到 C
将圆盘 1 从 B 移动到 A
将圆盘 2 从 B 移动到 C
将圆盘 1 从 A 移动到 C
"""
