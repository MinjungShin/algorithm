"""
괄호

https://www.acmicpc.net/problem/9012
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == "__main__":
    stack = list()
    cnt = int(input())
    for i in range(cnt):
        line = list(map(str, input().rstrip()))
        for x in line:
            if x == "(":
                stack.append(x)
            else:
                if not stack:
                    print("NO")
                    break
                stack.pop(-1)
        else:
            if stack:
                print("NO")
            else:
                print("YES")
            stack.clear()
