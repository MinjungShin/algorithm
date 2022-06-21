"""
8진수 2진수

https://www.acmicpc.net/problem/1212
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline


def solution1():
    n = str(input().rstrip())
    answer = ""
    for x in n:
        binary = n_to_binary(int(x))
        answer += binary

    if all(x == "0" for x in answer):
        print(0)
    else:
        while answer[0] == "0":
            answer = answer[1:]
        print(answer)


def n_to_binary(n):
    var = n
    result = ""
    while var > 0:
        remainder = var % 2
        var = var // 2
        result = str(remainder) + result

    while len(result) < 3:
        result = "0" + result

    return result


def solution2():
    n = int(input().rstrip(), 8)
    n = bin(n)[2:]  # 0b가 붙으므로 이 부분 제외
    print(n)


solution1()
# solution2()
