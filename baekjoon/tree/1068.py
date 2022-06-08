"""
트리

https://www.acmicpc.net/problem/1068
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def dfs(x):
    global result
    if len(tree[x]) == 0:
        result += 1
        return
    for y in tree[x]:
        if visited[y] == 0:
            visited[y] = 1
            dfs(y)


if __name__ == "__main__":
    # 입력 받기
    n = int(input())
    tree = [[] for _ in range(n)]
    tmp = list(map(int, input().split()))
    remove = int(input())

    visited = [0] * n
    root = -1
    result = 0
    for idx, val in enumerate(tmp):
        if idx == remove:  # 지워야 하는 노드면 continue
            continue
        if val == -1:  # 루트인 경우
            root = idx
            continue
        tree[val].append(idx)

    if root == -1:  # 지워야 하는 노드가 루트인 경우
        print(0)
    else:
        dfs(root)
        print(result)
