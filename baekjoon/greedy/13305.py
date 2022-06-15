"""
주유소

https://www.acmicpc.net/problem/13305
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
prices = list(map(int, input().split()))
total = sum(length)

result = 0

smallest = 2147000000
for idx, x in enumerate(length):
    if idx == 0:
        result += prices[idx] * x
        smallest = prices[idx]
    else:
        smallest = min(prices[idx], smallest)
        result += x * smallest
print(result)
