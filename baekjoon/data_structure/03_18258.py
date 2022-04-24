"""
큐2

https://www.acmicpc.net/problem/18258

list로 큐를 구현하면 시간 초과
따라서 idx로 큐의 첫번째 요소를 가리키게 함
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def push(x):
    queue.append(x)


def pop():
    global idx
    if empty() == 0: # 비어있지 않음
        tmp = queue[idx]
        idx += 1
        return tmp
    else:
        return -1


def size():
    if empty() == 0: # 비어있지 않음
        return len(queue) - idx
    else:
        return 0


def empty():
    if idx == len(queue) or len(queue) == 0:
        return 1
    else:
        return 0


def front():
    if empty() == 0: # 비어있지 않음
        return queue[idx]
    else:
        return -1


def back():
    if empty() == 0:  # 비어있지 않음
        return queue[-1]
    else:
        return -1


if __name__ == "__main__":
    queue = list()
    idx = 0
    cnt = int(input())
    for i in range(cnt):
        line = input().rstrip()
        if "push" in line:
            tmp = int(line.split(" ")[1])
            push(tmp)
        elif "pop" in line:
            print(pop())
        elif "size" in line:
            print(size())
        elif "empty" in line:
            print(empty())
        elif "front" in line:
            print(front())
        elif "back" in line:
            print(back())
