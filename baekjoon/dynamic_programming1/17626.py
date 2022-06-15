"""
Four Squares

https://www.acmicpc.net/problem/17626
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
dp = [2147000000] * (n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    tmp = pow(i, 0.5)
    if int(tmp) == tmp:  # 제곱수인 경우
        dp[i] = 1  # 1로
        continue

    # 만약에 i = 12인 경우
    # 11 + 1, 8 + 4, 3 + 9 가능
    # 그래서 dp[11] + 1, dp[8] + 1, dp[3] + 1 중에 min 값이 dp[12]
    j = 1
    val = pow(j, 2)  # j의 제곱수
    while i - val > 0:  # 현재 수부터 제곱수를 뺀 값
        if dp[i] == 1 or dp[i] == 2:  # 최소
            break
        dp[i] = min(dp[i - val] + 1, dp[i])  # 현재 값과 새로 구한 값 비교
        j += 1
        val = pow(j, 2)  # j의 제곱수

print(dp[n])
