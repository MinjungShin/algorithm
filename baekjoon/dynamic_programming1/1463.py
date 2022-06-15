"""
1로 만들기

https://www.acmicpc.net/problem/1463
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
dp = [2147000000] * (n + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, n + 1):
    if i == 2:  # dp[2]인 경우 초기화
        dp[2] = 1
    elif i == 3:  # dp[3]인 경우 초기화
        dp[3] = 1
    # 3으로 나눠지면 3으로 냐눴을 때, 2로 나눠지면 2로 나눴을 때, 1 뻈을 때 경우 모두 비교하여 최솟값 찾기
    else:
        if i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])
        dp[i] = min(dp[i - 1] + 1, dp[i])

print(dp[n])
