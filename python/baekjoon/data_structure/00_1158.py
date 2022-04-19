"""
요세푸스 문제

https://www.acmicpc.net/problem/1158
"""
from collections import deque


def solution(n, k):
    arr = [i + 1 for i in range(n)]
    answer = []
    queue = deque(arr)
    while queue:
        for _ in range(k - 1):
            tmp = queue.popleft()
            queue.append(tmp)
        answer.append(queue.popleft())

        if len(queue) == 1:
            answer += list(queue)
            break
    return answer


if __name__ == "__main__":
    N, K = map(int, input().split())
    answer = solution(N, K)
    print("<", ", ".join(str(x) for x in answer), ">", sep='')
