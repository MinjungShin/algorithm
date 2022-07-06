"""
트리의 부모 찾기

https://www.acmicpc.net/problem/11725
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 이거 안 해주면 백준 통과 못함(최대 노드 개수가 100,000)


def dfs(x):
    for y in graph[x]:
        if parent[y] == 0:
            parent[y] = x
            dfs(y)


if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    for i in range(2, n + 1):
        print(parent[i])
