"""
특정한 최단 경로

https://www.acmicpc.net/problem/1504
"""

import sys
import heapq

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue

        for x in graph[node]:  # x[0]가 노드, x[1]이 가중치
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(heap, (cost, x[0]))
    return distance


if __name__ == "__main__":
    n, e = map(int, input().split())
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    for i in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, input().split())

    distance1 = dijkstra(1)
    distance2 = dijkstra(v1)
    distance3 = dijkstra(v2)
    d1 = distance1[v1] + distance2[v2] + distance3[n]  # 1->v1->v2->n
    d2 = distance1[v2] + distance3[v1] + distance2[n]  # 1->v2->v1->n
    result = min(d1, d2)
    print(result if result < INF else -1)
