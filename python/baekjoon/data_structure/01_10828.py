"""
스택

https://www.acmicpc.net/problem/10828
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def push(x):
    stack.append(x)


def pop():
    if not stack:
        return -1
    else:
        return stack.pop(-1)


def size():
    return len(stack)


def empty():
    if stack:
        return 0
    else:
        return 1


def top():
    if stack:
        return stack[-1]
    else:
        return -1


if __name__ == "__main__":
    stack = list()
    cnt = int(input())
    for i in range(cnt):
        line = input().strip()
        if "push" in line:
            tmp = line.split(" ")[1]
            push(tmp)
        elif "top" in line:
            print(top())
        elif "size" in line:
            print(size())
        elif "empty" in line:
            print(empty())
        elif "pop" in line:
            print(pop())