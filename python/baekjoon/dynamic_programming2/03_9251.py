"""
LCS

https://www.acmicpc.net/problem/9251
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    w1, w2 = input().rstrip(), input().rstrip()
    len1, len2 = len(w1), len(w2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[len1][len2])
