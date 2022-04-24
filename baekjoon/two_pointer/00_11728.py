"""
배열 합치기

https://www.acmicpc.net/problem/11728
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    len1, len2 = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    result = []
    pt1, pt2 = 0, 0
    while pt1 < len1 and pt2 < len2:
        if arr1[pt1] <= arr2[pt2]:
            result.append(arr1[pt1])
            pt1 += 1
        else:
            result.append(arr2[pt2])
            pt2 += 1
    if pt1 < len1:
        result += arr1[pt1:]
    if pt2 < len2:
        result += arr2[pt2:]

    print(*result)
