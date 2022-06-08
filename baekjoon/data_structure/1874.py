"""
스택 수열

https://www.acmicpc.net/problem/1874
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]  # 만들어야하는 수열

queue = deque()
pointer = 0  # arr의 포인터
current = 1  # queue에 넣을 수
result = []
while queue or current < n + 1:
    if arr[pointer] > current:  # 큐에 넣어주기
        queue.append(current)
        current += 1
        result.append("+")
        continue
    elif arr[pointer] == current:  # 큐에 넣었다 빼기
        queue.append(current)
        queue.pop()
        current += 1
        pointer += 1
        result.append("+")
        result.append("-")
        continue
    else:  # 큐에서 빼기
        val = queue.pop()
        if val != arr[pointer]:
            print("NO")
            break
        else:
            result.append("-")
            pointer += 1
else:
    for x in result:
        print(x)
