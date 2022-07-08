"""
숫자 카드

https://www.acmicpc.net/problem/10815
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def search(left, right, num):
    mid = (left + right) // 2
    if left > right:
        result.append(0)
        return

    if num < cards[mid]:
        search(left, mid - 1, num)
    elif num > cards[mid]:
        search(mid + 1, right, num)
    elif num == cards[mid]:
        result.append(1)


def search2(left, right, num):
    while left <= right:
        mid = (left + right) // 2
        if num < cards[mid]:
            right = mid - 1
        elif num > cards[mid]:
            left = mid + 1
        elif num == cards[mid]:
            result.append(1)
            break
    else:
        result.append(0)


n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
m_list = list(map(int, input().split()))

result = []
for x in m_list:
    # search(0, n - 1, x)
    search2(0, n - 1, x)
print(*result)
