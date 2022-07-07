"""
효율적인 해킹

https://www.acmicpc.net/problem/1325
"""

import sys
from collections import deque

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    counts = [0] * (n + 1)
    # bfs
    for i in range(1, n + 1):
        queue = deque()
        visited = [0] * (n + 1)
        cnt = 0
        queue.append(i)
        while queue:
            tmp = queue.popleft()
            visited[tmp] = 1
            for x in graph[tmp]:
                if visited[x] == 0:
                    visited[x] = 1
                    queue.append(x)
            cnt += 1
        counts[i] = cnt

    maxx = max(counts)
    for i in range(1, n + 1):
        if counts[i] == maxx:
            print(i, end=" ")
