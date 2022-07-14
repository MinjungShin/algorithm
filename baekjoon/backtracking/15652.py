"""
N과 M (4)

https://www.acmicpc.net/problem/15652
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def dfs(x, cnt, list):
    if cnt == m:
        print(*list)
        return
    for i in range(x, n + 1):
        dfs(i, cnt + 1, list + [i])


if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        dfs(i, 1, [i])
