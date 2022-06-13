"""
더하기 사이클

https://www.acmicpc.net/problem/1110
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())

result = 0
num = n
while True:
    if num > 9:
        n1 = num // 10
        n2 = num % 10
        num = n2 * 10 + (n1 + n2) % 10
    else:
        num = num * 10 + num

    result += 1
    if num == n:
        break
print(result)
