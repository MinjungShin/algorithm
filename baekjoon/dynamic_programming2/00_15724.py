"""
주지수

https://www.acmicpc.net/problem/15724
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0] * (m + 2) for _ in range(n + 2)]  # 둘레에 0으로 채우기
    dp = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        tmp = list(map(int, input().split()))
        for j in range(1, m + 1):
            arr[i][j] = tmp[j - 1]
            # 자기 자신 + [i - 1][j]까지의 누적합(위) + [i][j - 1]까지의 누적합(왼) - [i - 1][j - 1]까지의 누적합(증복)
            dp[i][j] = arr[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
    # print(dp)

    k = int(input())
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
