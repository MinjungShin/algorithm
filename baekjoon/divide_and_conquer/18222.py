"""
투에-모스 문자열

https://www.acmicpc.net/problem/18222
"""

import sys
import math

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def sol1(n):
    x = n - 1
    cnt = 0
    while x >= 2:
        tmp = int(math.log2(x))
        x = x - 2 ** tmp
        cnt += 1

    if cnt % 2 == 1:
        print(abs(x - 1))
    else:
        print(x)


def sol2(n):
    print(bin(n - 1).count('1') % 2)


if __name__ == "__main__":
    n = int(input())

    sol1(n)
    # sol2(n)
