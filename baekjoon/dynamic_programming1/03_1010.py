"""
다리놓기

https://www.acmicpc.net/problem/1010
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


# 조합으로 풀었음 -> mCn
def solution1():
    for i in range(t):
        n, m = map(int, input().split())
        a = b = c = 1
        for j in range(1, m + 1):
            a *= j
        for h in range(1, n + 1):
            b *= h
        for k in range(1, m - n + 1):
            c *= k
        print(a // b // c)


# dp
def solution2():
    for i in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # 초기화
        # dp[1][y] = y로 초기화
        # dp[x][x] = 1로 초기화
        for x in range(1, m + 1):
            dp[1][x] = x
        for x in range(1, n + 1):
            dp[x][x] = 1

        # 2차원 배열 엄청 그려서 풀었다.......................
        for x in range(2, n + 1):
            for y in range(1, m + 1):
                dp[x][y] = dp[x][y - 1] + dp[x - 1][y - 1]
        print(dp[n][m])


if __name__ == "__main__":
    t = int(input())
    # 조합
    # solution1()

    # dp로 풀기
    solution2()
