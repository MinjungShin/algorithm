"""
최단경로

https://www.acmicpc.net/problem/1753
"""

import sys
import heapq

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


# 다익스트라는 특정 노드 -> 다른 모든 노드로 가는 최단 거리
# 힙, 우선순위큐를 이용한다! (그래야 시간이 적게 걸림)
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))  # 힙에 넣을 때 (거리, 노드)로 넣어서 거리에 따라 정렬될 수 있도록 함
    distance[start] = 0
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:  # 이미 거리가 결정됨
            continue

        for x in graph[node]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(heap, (cost, x[0]))


if __name__ == "__main__":
    INF = int(1e9)
    n, e = map(int, input().split())
    start = int(input())
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    dijkstra(start)

    for i in range(1, n + 1):
        if distance[i] >= INF:
            print("INF")
        else:
            print(distance[i])
