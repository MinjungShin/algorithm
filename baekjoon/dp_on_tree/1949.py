"""
1949. 우수 마을

https://www.acmicpc.net/problem/1949
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(x):
    visited[x] = 1
    for y in graph[x]:
        if visited[y] == 0:
            dfs(y)
            dp[x][0] += max(dp[y][0], dp[y][1])  # x가 우수 마을 아닌 경우
            dp[x][1] += dp[y][0]  # x가 우수 마을인 경우


if __name__ == "__main__":
    n = int(input())
    people = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    dp = [[0, 0]]
    dp += [[0, x] for x in people]
    for i in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    print(max(dp[1][0], dp[1][1]))
