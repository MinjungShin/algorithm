"""
카드2

https://www.acmicpc.net/problem/2164
"""

import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    cnt = int(input())
    queue = deque(range(1, cnt+1))
    while len(queue) > 1:
        queue.popleft()
        tmp = queue.popleft()
        queue.append(tmp)
    print(queue[0])