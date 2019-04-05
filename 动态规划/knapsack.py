#! usr/bin/env python3
# -*-coding:utf-8-*-


def knapsack(items: list, value: list, n: int, w: int):
    """
    背包问题
    :param items: 物品重量
    :param value: 价值
    :param n: 数量
    :param w: 背包最大承重
    :return: 最大价值
    """
    states = [[-1 for j in range(w + 1)] for i in range(n)]
    states[0][0] = 0
    states[0][items[0]] = value[0]  # 第一步决策
    # 从第二步开始
    for i in range(1, n):
        for j in range(0, w + 1):
            # 不选择第i个物品
            if states[i - 1][j] >= 0:
                states[i][j] = states[i - 1][j]
        for k in range(0, w - items[i] + 1):
            # 选择第i个物品
            if states[i - 1][k] >= 0:
                v = states[i - 1][k] + value[i]
                if v > states[i][k + items[i]]:
                    # 两种决策重量相同，选价值大较大的方案
                    states[i][k + items[i]] = v
    # 找出最大值
    print(max(states[n - 1]))


if __name__ == "__main__":
    items = [2, 2, 4, 6, 3]
    value = [3, 4, 8, 9, 6]
    n = 5
    w = 9
    knapsack(items, value, n, w)
