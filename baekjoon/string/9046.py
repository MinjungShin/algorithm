"""
복호화

https://www.acmicpc.net/problem/9046
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = [0] * 26
    tmp = list(input().rstrip().split())
    for x in tmp:
        for y in x:
            arr[ord(y) - 97] += 1  # a는 97

    maxx = 0
    max_idx = -1
    for idx, val in enumerate(arr):
        if val > maxx:
            maxx = val
            max_idx = idx

    if arr.count(maxx) > 1:
        print("?")
    else:
        print(chr(max_idx + 97))
