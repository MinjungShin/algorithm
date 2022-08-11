"""
4195. 친구 네트워크

https://www.acmicpc.net/problem/4195
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def find(name):
    if name == dictionary[name]:
        return name

    dictionary[name] = find(dictionary[name])
    count(dictionary[name], name)
    return dictionary[name]


def union(a, b):
    x = find(a)
    y = find(b)

    if x != y:
        dictionary[x] = y
        count(x, y)


def count(n1, n2):
    visited[n1] += visited[n2]
    visited[n2] = 0


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        f = int(input())
        dictionary = {}
        visited = {}
        for i in range(f):
            name1, name2 = map(str, input().rstrip().split())
            if name1 not in dictionary:
                dictionary[name1] = name1
                visited[name1] = 1
            if name2 not in dictionary:
                dictionary[name2] = name2
                visited[name2] = 1
            union(name1, name2)
            print(visited[find(name1)])
