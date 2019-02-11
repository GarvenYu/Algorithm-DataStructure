#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
假设天猫双11满200-50，现购物车内有n个物品，从里面选几个，在凑够满减条件的前提下，让选出来的商品价格总和最大程度地接近满减条件（200 元）
"""


def buy_item(price: list, n: int, limit=200, maxmoney=300):
    """
    :param price: 商品价格
    :param n: 数量
    :param limit: 200
    :param maxmoney: 最大能承受的金额
    :return: list
    """
    states = [[0 for j in range(maxmoney + 1)] for i in range(n)]
    states[0][0] = 0
    states[0][price[0]] = price[0]
    for i in range(1, n):
        for j in range(0, maxmoney + 1):
            if states[i - 1][j]:
                states[i][j] = states[i - 1][j]  # 不购买商品
        for k in range(0, maxmoney - price[i] + 1):
            if states[i - 1][k]:
                states[i][k + price[i]] = 1  # 购买商品
    for r in range(limit, maxmoney + 1):
        # 输出结果>=limit的最小值
        if states[n - 1][r]:
            print("最小购买金额为:" + str(r))
            for i in range(n - 1, 0, -1):
                if states[i - 1][r - price[i]]:
                    # 买了第i件商品
                    print("购买了：" + str(price[i]))
                    r = r - price[i]
                else:
                    # 没有购买
                    pass
            if r > 0:
                print("购买了：" + str(price[0]))
            break


if __name__ == "__main__":
    price = [100, 50, 30, 22, 57]
    n = 5
    buy_item(price, n)
