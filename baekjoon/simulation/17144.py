"""
미세먼지 안녕!

https://www.acmicpc.net/problem/17144
"""

import sys
import copy

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def diffuse(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    val = graph[x][y] // 5

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < r and 0 <= yy < c:
            if graph[xx][yy] >= 0:
                new_graph[xx][yy] += val
                cnt += 1
    new_graph[x][y] -= cnt * val


def clean_up(x):
    before = new_graph[x][1]
    for i in range(2, c):
        cur = new_graph[x][i]
        new_graph[x][i] = before
        before = cur
    new_graph[x][1] = 0
    for i in range(x - 1, -1, -1):
        cur = new_graph[i][c - 1]
        new_graph[i][c - 1] = before
        before = cur
    for i in range(c - 2, -1, -1):
        cur = new_graph[0][i]
        new_graph[0][i] = before
        before = cur
    for i in range(1, x):
        cur = new_graph[i][0]
        new_graph[i][0] = before
        before = cur


def clean_down(x):
    before = new_graph[x][1]
    for i in range(2, c):
        cur = new_graph[x][i]
        new_graph[x][i] = before
        before = cur
    new_graph[x][1] = 0
    for i in range(x + 1, r):
        cur = new_graph[i][c - 1]
        new_graph[i][c - 1] = before
        before = cur
    for i in range(c - 2, -1, -1):
        cur = new_graph[r - 1][i]
        new_graph[r - 1][i] = before
        before = cur
    for i in range(r - 2, x, -1):
        cur = new_graph[i][0]
        new_graph[i][0] = before
        before = cur


graph = []
new_graph = []
r, c, t = map(int, input().split())
for i in range(r):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
new_graph = copy.deepcopy(graph)

for T in range(t):
    air_x = -1
    air_y = -1
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                diffuse(i, j)
            if graph[i][j] == -1:
                air_x = i
                air_y = j
    clean_up(air_x - 1)
    clean_down(air_x)
    graph = copy.deepcopy(new_graph)

total = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] >= 0:
            total += graph[i][j]
print(total)
