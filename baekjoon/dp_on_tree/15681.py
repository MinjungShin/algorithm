import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(v):
    dp[v] = 1
    visited[v] = 1
    for x in tree[v]:
        if not visited[x]:
            dfs(x)
            dp[v] += dp[x]


if __name__ == "__main__":
    n, r, q = map(int, input().split())

    tree = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)
    visited = [0] * (n + 1)

    for i in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    dfs(r)

    for i in range(q):
        root = int(input())
        print(dp[root])
