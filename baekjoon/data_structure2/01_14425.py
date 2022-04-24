"""
문자열 집합

https://www.acmicpc.net/problem/14425
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


# set 이용 - 148ms
def sol_set():
    s = set()
    cnt = 0
    for i in range(n):
        s.add(input().rstrip())
    for i in range(m):
        if input().rstrip() in s:
            cnt += 1
    print(cnt)


# dict 이용 - 152ms
def sol_dict():
    s = dict()
    cnt = 0
    for i in range(n):
        s[input().rstrip()] = 1
    for i in range(m):
        if input().rstrip() in s.keys():
            cnt += 1
    print(cnt)


# 시간이 너무 오래 걸림 - 3940ms
def sol_list():
    s = list()
    cnt = 0
    for i in range(n):
        s.append(input().rstrip())
    for i in range(m):
        if input().rstrip() in s:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    n, m = map(int, input().split())
    sol_dict()
