"""
나무 자르기

https://www.acmicpc.net/problem/2805
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def cut(x):
    total = 0
    for y in heights:
        if y - x > 0:
            total += y - x
    return total


if __name__ == "__main__":
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))

    left = 0
    right = max(heights)
    while left <= right:
        mid = (left + right) // 2
        total = cut(mid)
        if total >= m:
            left = mid + 1
        else:
            right = mid - 1

    print(right)
