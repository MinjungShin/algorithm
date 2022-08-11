"""
16562. 친구비

https://www.acmicpc.net/problem/16562
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x = find(a)
    y = find(b)

    if x != y:
        if cost[x] < cost[y]:  # 비용이 적은 친구로 업데이트
            parent[y] = x
        else:
            parent[x] = y


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    cost = list(map(int, input().split()))
    cost = [0] + cost

    parent = [i for i in range(n + 1)]
    for i in range(m):
        v, w = map(int, input().split())
        union(v, w)

    money = 0
    for idx, x in enumerate(parent):
        if x == idx:
            money += cost[x]
    if money > k:
        print("Oh no")
    else:
        print(money)
