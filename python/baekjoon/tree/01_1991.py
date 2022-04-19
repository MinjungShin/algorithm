"""
트리 순회

https://www.acmicpc.net/problem/1991
"""

import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def pre_order(node):
    if node == ".":
        return
    print(node, end="")
    pre_order(tree[node][0])
    pre_order(tree[node][1])


def in_order(node):
    if node == ".":
        return
    in_order(tree[node][0])
    print(node, end="")
    in_order(tree[node][1])


def post_order(node):
    if node == ".":
        return
    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end="")


if __name__ == "__main__":
    n = int(input())
    tree = {}
    for i in range(n):
        v1, v2, v3 = map(str, input().rstrip().split())
        tree[v1] = [v2, v3]
    # print(tree)
    pre_order('A')
    print()
    in_order('A')
    print()
    post_order('A')
