"""
설탕 배달

https://www.acmicpc.net/problem/2839
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [500000000] * (n + 1)
    dp[3] = 1
    if n > 4:
        dp[5] = 1
    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1

    if dp[n] >= 500000000:
        print(-1)
    else:
        print(dp[n])
