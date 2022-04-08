"""
바이러스

https://www.acmicpc.net/problem/2606
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    check = [0] * (n + 1)

    m = int(input())
    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1

    queue = deque()
    queue.append(1)
    while queue:
        tmp = queue.popleft()
        check[tmp] = 1  # 방문 체크
        for i in range(1, n + 1):
            if graph[tmp][i] == 1 and check[i] == 0:
                queue.append(i)
    print(sum(check) - 1)  # 1번 컴퓨터 제외
