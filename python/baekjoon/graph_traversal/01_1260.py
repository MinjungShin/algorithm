"""
DFS와 BFS

https://www.acmicpc.net/problem/1260
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def dfs(v):
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            result1.append(i)  # 리스트에 추가
            dfs(i)


def bfs():
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        tmp = queue.popleft()
        result2.append(tmp)  # 리스트에 추가
        for i in range(1, n + 1):
            if graph[tmp][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)


if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    result1 = []
    result2 = []

    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1

    # DFS
    visited = [0] * (n + 1)
    visited[v] = 1
    result1.append(v)
    dfs(v)

    # BFS
    visited = [0] * (n + 1)
    bfs()

    print(*result1)
    print(*result2)
