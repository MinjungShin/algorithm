"""
폴리오미노

https://www.acmicpc.net/problem/1343
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    string = input().rstrip()
    string = string.replace("XXXX", "AAAA")
    string = string.replace("XX", "BB")
    if "X" in string:
        print(-1)
    else:
        print(string)
