"""
거스름돈

https://www.acmicpc.net/problem/14916
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    money = n
    result = [500000] * (n + 5)
    result[2] = 1
    result[4] = 2
    result[5] = 1
    for i in range(6, n + 1):
        result[i] = min(result[i - 2] + 1, result[i - 5] + 1)

    if result[n] >= 500000:
        print(-1)
    else:
        print(result[n])
