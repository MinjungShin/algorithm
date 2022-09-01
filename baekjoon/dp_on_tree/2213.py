"""
2213. 트리의 독립집합

https://www.acmicpc.net/problem/2213
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def dfs(x):
    visited[x] = 1
    dp[x][1] = values[x - 1]
    nodes[x][1].append(x)
    for y in graph[x]:
        if visited[y] == 0:
            dfs(y)
            dp[x][1] += dp[y][0]  # x 포함일 때
            for z in nodes[y][0]:  # x 포함일 때에 대한 node 추가
                nodes[x][1].append(z)

            # x 포함 아닐 때
            if dp[y][0] > dp[y][1]:  # y를 포함 하지 않는 경우
                dp[x][0] += dp[y][0]
                for h in nodes[y][0]:
                    nodes[x][0].append(h)
            else:  # y를 포함 하는 경우
                dp[x][0] += dp[y][1]
                for h in nodes[y][1]:
                    nodes[x][0].append(h)


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    dp = [[0] * 2 for _ in range(n + 1)]
    nodes = [[[], []] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    if dp[1][0] > dp[1][1]:
        nodes[1][0].sort()
        print(dp[1][0])
        print(*nodes[1][0])
    else:
        nodes[1][1].sort()
        print(dp[1][1])
        print(*nodes[1][1])
