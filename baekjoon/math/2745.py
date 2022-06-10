"""
진법 변환

https://www.acmicpc.net/problem/2745
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n, b = map(str, input().rstrip().split())
b = int(b)
dictionary = dict()

tmp = 65
for i in range(26):
    dictionary[chr(tmp + i)] = i + 10

result = 0
var = 0
for i in range(len(n) - 1, -1, -1):
    if n[i].isalpha():
        result += pow(b, var) * dictionary[n[i]]
    else:
        result += pow(b, var) * int(n[i])
    var += 1
print(result)
