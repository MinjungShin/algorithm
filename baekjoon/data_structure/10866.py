"""
덱

https://www.acmicpc.net/problem/10866
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

deq = deque()
n = int(input())
for i in range(n):
    tmp = list(input().rstrip().split())
    if tmp[0] == "push_front":
        deq.appendleft(tmp[1])
    elif tmp[0] == "push_back":
        deq.append(tmp[1])
    elif tmp[0] == "pop_front":
        if deq:
            val = deq.popleft()
            print(val)
        else:
            print(-1)
    elif tmp[0] == "pop_back":
        if deq:
            val = deq.pop()
            print(val)
        else:
            print(-1)
    elif tmp[0] == "size":
        print(len(deq))
    elif tmp[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif tmp[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif tmp[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)
