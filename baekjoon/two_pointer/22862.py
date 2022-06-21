"""
가장 긴 짝수 연속한 부분 수열 (large)

https://www.acmicpc.net/problem/22862
"""

import sys

sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
for i in range(n):  # 짝수부터 시작
    if arr[i] % 2 == 0:
        left = i
        right = i
        break

cnt = 0  # 삭제 횟수
result = 0
while right < len(arr):
    if arr[left] == -1:  # 삭제로 표시했던 값
        cnt -= 1
        left += 1
    elif arr[right] % 2 == 0:  # 짝수인 경우
        right += 1
    elif arr[right] % 2 == 1:  # 홀수인 경우
        if cnt < k:
            arr[right] = -1  # 삭제로 표시
            right += 1
            cnt += 1  # 삭제 횟수 증가
        else:  # 최대 삭제 횟수를 초과하는 경우
            left += 1

    result = max(result, right - left - cnt)

print(result)
