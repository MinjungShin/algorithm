"""
공약수

https://www.acmicpc.net/problem/5618

Python3는 시간초과
PyPy3는 시간초과 X
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


# gcd(a,b) == gcd(b,r)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def GCD(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


if __name__ == "__main__":
    n = int(input())
    if n == 2:
        v1, v2 = map(int, input().split())
        gcd = gcd(v1, v2)
    else:
        v1, v2, v3 = map(int, input().split())
        gcd = gcd(gcd(v1, v2), v3)

    for i in range(1, gcd // 2 + 1):
        if gcd % i == 0:
            print(i)
    print(gcd)
