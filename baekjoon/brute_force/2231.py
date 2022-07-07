"""
분해합

https://www.acmicpc.net/problem/2231
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    sep = str(i)
    total = i
    for x in sep:
        total += int(x)

    if total == n:
        print(i)
        break
else:
    print(0)
