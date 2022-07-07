"""
수학은 비대면강의입니다

https://www.acmicpc.net/problem/19532
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        tmp1 = a * x + b * y
        tmp2 = d * x + e * y
        if tmp1 == c and tmp2 == f:
            print(x, y)
