"""
윤년

https://www.acmicpc.net/problem/2753
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())

if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
    print(1)
else:
    print(0)
