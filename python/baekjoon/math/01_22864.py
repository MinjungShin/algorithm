"""
피로도

https://www.acmicpc.net/problem/22864
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    a, b, c, m = map(int, input().split())
    cur_m = 0  # 피로도
    total = 0  # 전체 일
    if a > m:
        print(0)
        exit(0)
    for i in range(24):
        if cur_m + a > m:
            cur_m -= c
            if cur_m < 0:
                cur_m = 0
        elif cur_m + a <= m:
            cur_m += a
            total += b
    if total < 0:
        print(0)
    else:
        print(total)
