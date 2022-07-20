"""
구간 합 구하기 5

https://www.acmicpc.net/problem/11660
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
graph.append([0] * (n + 1))
for i in range(n):
    tmp = [0]
    tmp += list(map(int, input().split()))
    graph.append(tmp)

total = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        total[i][j] = graph[i][j] + total[i - 1][j] + total[i][j - 1] - total[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(graph[x1][y1])
    else:
        val = total[x2][y2] - total[x1 - 1][y2] - total[x2][y1 - 1] + total[x1 - 1][y1 - 1]
        print(val)
