"""
16398. 행성 연결

https://www.acmicpc.net/problem/16398
"""

import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)

    if a != b:
        parent[a] = b


if __name__ == "__main__":
    n = int(input())
    parent = [i for i in range(n + 1)]
    edges = []
    result = 0
    for i in range(1, n + 1):
        tmp = list(map(int, input().split()))
        for j in range(1, n + 1):
            if i == j:
                continue
            # 노드1, 노드2, 비용 순서
            edges.append([i, j, tmp[j - 1]])
    edges.sort(key=lambda x: (x[2]))

    result = 0
    for x in edges:
        if find(x[0]) != find(x[1]):
            union(x[0], x[1])
            result += x[2]
    print(result)
