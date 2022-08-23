"""
21924. 도시 건설

https://www.acmicpc.net/problem/21924
"""

import sys

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
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    edges = []

    total = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        # 비용, 노드1, 노드2 순서
        edges.append([c, a, b])
        total += c
    edges.sort()

    result = 0
    cnt = 0  # 간선의 개수
    for x in edges:
        if find(x[1]) != find(x[2]):
            union(x[1], x[2])
            result += x[0]
            cnt += 1

    # MST는 (간선의 개수) = (노드의 개수) - 1
    if cnt < n - 1:
        print(-1)
    else:
        print(total - result)
