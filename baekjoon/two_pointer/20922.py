"""
겹치는 건 싫어

https://www.acmicpc.net/problem/20922
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
counts = [0] * (max(arr) + 1)  # 숫자를 중복 몇번 사용했는지 저장하기 위한 리스트
result = 0
while right < n:
    if counts[arr[right]] < k:  # 개수를 넘지 않는 경우
        counts[arr[right]] += 1
        right += 1
    else:  # 개수를 넘는 경우
        counts[arr[left]] -= 1
        left += 1
    result = max(result, right - left)  # result 갱신

print(result)
