"""
돌 게임

https://www.acmicpc.net/problem/9655
"""
import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    if n % 2 == 1:
        print("SK")
    else:
        print("CY")
