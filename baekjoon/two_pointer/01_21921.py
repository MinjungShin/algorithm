"""
블로그

https://www.acmicpc.net/problem/21921
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    total = [0] * (n + 1)

    # 누적합 구하기(total[0] = 0)
    for i in range(1, n + 1):
        total[i] = total[i - 1] + arr[i - 1]

    # 최댓값, 기간이 몇개 있는지 구하기
    maximum = 0
    cnt = 0
    for i in range(x, n + 1):
        t = total[i] - total[i - x]
        if t > maximum:
            maximum = t
            cnt = 1
        elif t == maximum:
            cnt += 1

    if maximum != 0:
        print(maximum)
        print(cnt)
    else:
        print("SAD")
