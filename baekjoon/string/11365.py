"""
!밀비 급일

https://www.acmicpc.net/problem/11365
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

tmp = input().strip()
while tmp != "END":
    arr = list(tmp.split(" "))
    for i in range(len(arr) - 1, -1, -1):
        string = list(arr[i])
        string.reverse()
        string = "".join(string)
        print(string, end=" ")
    print()
    tmp = input().rstrip()
