"""
로프

https://www.acmicpc.net/problem/2217
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n = int(input())
weights = [int(input()) for _ in range(n)]
weights.sort(reverse=True)

"""
로프의 개수가 1~n까지일 때 (30,20,10)
만약 1개면 로프 중 최대 중량을 버티는 친구인 30 -> 답 30
2개면 30, 20 사용하고 답은 20 * 2(로프 사용 개수) -> 40이 됨
3개면 30, 20, 10 사용하고 답은 10 * 3 -> 30이 됨
사용하는 로프 중 (가장 중량이 작은 로프 * 로프 사용 개수)가 답
이렇게 1~n까지 다해서 가장 값이 큰 게 답
"""
result = 0
for idx, val in enumerate(weights):
    tmp = val * (idx + 1)
    if result < tmp:
        result = tmp
print(result)
