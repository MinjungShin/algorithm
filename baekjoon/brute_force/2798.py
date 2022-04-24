"""
블랙잭

https://www.acmicpc.net/problem/2798
"""

import sys


def dfs(i, total, cnt):
    global result
    if cnt == 3:
        if total <= m:
            result = max(result, total)
        return

    if i >= n or total > m:
        return

    dfs(i + 1, total + cards[i], cnt + 1)
    dfs(i + 1, total, cnt)


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))

    result = 0
    dfs(0, 0, 0)
    print(result)
