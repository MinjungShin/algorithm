"""
힙(Heap)
더 맵게
"""

import heapq


def get_scoville(a, b):
    return a + b * 2


def solution(scoville, K):
    heapq.heapify(scoville)

    cnt = 0
    while scoville:
        v1 = heapq.heappop(scoville)
        if v1 > K:
            break
        if not scoville:
            return -1
        v2 = heapq.heappop(scoville)
        scov = get_scoville(v1, v2)
        heapq.heappush(scoville, scov)
        cnt += 1
    return cnt
