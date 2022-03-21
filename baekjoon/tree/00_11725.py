"""
트리의 부모 찾기

https://www.acmicpc.net/problem/11725
"""
import sys
from collections import deque

# 백준에서 dfs로 하는 경우 추가해줘야 런타임 에러 발생 안함
# sys.setrecursionlimit(10**9)

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def dfs(start):
    for x in tree[start]:
        if parent[x] == 0:
            parent[x] = start
            dfs(x)


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        tmp = queue.popleft()
        for x in tree[tmp]:
            if parent[x] == 0:
                parent[x] = tmp
                queue.append(x)


if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        v1, v2 = map(int, input().split())
        tree[v1].append(v2)
        tree[v2].append(v1)
    # print(tree)
    parent = [0] * (n + 1)
    # dfs(1)
    bfs(1)

    for x in range(2, n + 1):
        print(parent[x])
