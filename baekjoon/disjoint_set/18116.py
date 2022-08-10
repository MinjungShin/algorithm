"""
18116. 로봇 조립

https://www.acmicpc.net/problem/18116
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    count(parent[x], x)
    return parent[x]


def union(a, b):
    x = find(a)
    y = find(b)

    if x != y:
        parent[x] = y
        count(y, x)


def count(a, b):
    cnt[a] += cnt[b]
    cnt[b] = 0


if __name__ == "__main__":
    n = int(input())
    parent = [i for i in range(10 ** 6 + 1)]
    cnt = [1] * (10 ** 6 + 1)
    for i in range(n):
        tmp = list(input().rstrip().split())
        if tmp[0] == "I":
            union(int(tmp[1]), int(tmp[2]))
        elif tmp[0] == "Q":
            root = find(int(tmp[1]))
            print(cnt[root])
