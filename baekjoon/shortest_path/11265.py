"""
끝나지 않는 파티

https://www.acmicpc.net/problem/11265
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


# 플로이드 워셜은 모든 노드 -> 모든 노드 최단거리 구할 때
# 3중 for문을 사용하므로 시간복잡도가 높음
# 하지만 다익스트라보다 간단하게 구현 가능
# 백준에서 pypy3로 돌려야 통과됨(python은 시간초과)
def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(m):
        a, b, c = map(int, input().split())
        if graph[a - 1][b - 1] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")


# 이건 python 통과함
def floyd_warshall2():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 차이1: min 대신 if 문 사용
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # 차이2: 변수가 필요 없으므로 i 대신 _ 사용
    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a - 1][b - 1] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []

    for _ in range(n):
        tmp = list(map(int, input().split()))
        graph.append(tmp)

    # floyd_warshall()
    floyd_warshall2()
