"""
절댓값 힙

https://www.acmicpc.net/problem/11286
"""

import sys
import heapq

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        if result:
            val = heapq.heappop(result)[1]
            print(val)
        else:
            print(0)
    else:
        heapq.heappush(result, (abs(tmp), tmp))
