"""
최대 힙

https://www.acmicpc.net/problem/11279
"""

import sys
import heapq

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
result = []
for i in range(n):
    tmp = int(input())
    if tmp == 0:
        if result:
            val = heapq.heappop(result)[1]
            print(val)
        else:
            print(0)
    elif tmp > 0:
        heapq.heappush(result, (-tmp, tmp)) # 최대힙으로
