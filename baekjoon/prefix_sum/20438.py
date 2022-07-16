"""
출석체크

https://www.acmicpc.net/problem/20438
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep_entrance_nums = list(map(int, input().split()))
entrance_nums = list(map(int, input().split()))

for x in sleep_entrance_nums:
    if x in entrance_nums:
        entrance_nums.remove(x)

sums = [0] * (n + 3)
for x in entrance_nums:
    for i in range(1, n + 2):
        var = x * i
        if var <= n + 2:
            if var not in sleep_entrance_nums:
                sums[var] = 1
        else:
            break

for i in range(3, n + 3):
    sums[i] += sums[i - 1]

for i in range(m):
    s, e = map(int, input().split())
    print(e - s + 1 - (sums[e] - sums[s - 1]))
