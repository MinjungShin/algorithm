"""
나는야 포켓몬 마스터 이다솜

https://www.acmicpc.net/problem/1620
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def solution(x):
    if x.isdigit():
        tmp = int(x)
        return map[tmp]
    else:
        return map2[x]


if __name__ == "__main__":
    n, m = map(int, input().split())
    map = dict()
    map2 = dict()
    for i in range(1, n + 1):
        tmp = input().rstrip()
        map[i] = tmp
        map2[tmp] = i

    for i in range(m):
        print(solution(input().rstrip()))
