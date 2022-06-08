"""
완전 이진 트리

https://www.acmicpc.net/problem/9934
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = []

while arr:
    tmp = []
    for idx, val in enumerate(arr):
        if idx % 2 == 0:
            tmp.append(val)
    for x in tmp:
        arr.remove(x)
    result.append(tmp)

result.reverse()

for x in result:
    print(*x)
