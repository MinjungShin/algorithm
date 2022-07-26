"""
!밀비 급일

https://www.acmicpc.net/problem/11365
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

tmp = input().rstrip()
while tmp != "END":
    arr = list(tmp)
    arr.reverse()
    for x in arr:
        print(x, end="")
    print()
    tmp = input().rstrip()
