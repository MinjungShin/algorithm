"""
동전

https://www.acmicpc.net/problem/9084
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        cnt = int(input())
        coins = list(map(int, input().split()))
        money = int(input())

        dp = [0] * (money + 1)
        dp[0] = 1

        # 각 동전으로 money까지 채우는 경우 계산
        for x in coins:
            for i in range(money + 1):
                if i >= x:
                    dp[i] += dp[i - x]
        print(dp[money])
