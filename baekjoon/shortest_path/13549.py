"""
숨바꼭질 3

https://www.acmicpc.net/problem/13549
"""

import sys
from collections import deque

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def bfs(n):
    global result
    queue = deque()
    queue.append((n, 0))  # (위치, 지금까지 시간)
    while queue:
        tmp = queue.popleft()
        m1 = tmp[0] - 1
        m2 = tmp[0] + 1
        m3 = 2 * tmp[0]
        # 범위 체크, 시간이 최대 시간보다 작은지 확인
        if 0 <= m1 <= 2 * maxx and tmp[1] + 1 < visited[m1]:
            visited[m1] = tmp[1] + 1
            queue.append((m1, tmp[1] + 1))
        if 0 <= m2 <= 2 * maxx and tmp[1] + 1 < visited[m2]:
            visited[m2] = tmp[1] + 1
            queue.append((m2, tmp[1] + 1))
        if 0 <= m3 <= 2 * maxx and tmp[1] < visited[m3]:
            visited[m3] = tmp[1]
            queue.append((m3, tmp[1]))


if __name__ == "__main__":
    n, k = map(int, input().split())
    maxx = 100000
    visited = [abs(k - n)] * (maxx * 2 + 1)
    bfs(n)
    print(visited[k])
