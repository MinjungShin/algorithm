"""
주식가격
스택/큐
"""

from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        tmp = queue.popleft()
        cnt = 0
        for x in queue:
            cnt += 1
            if tmp > x:
                break
        answer.append(cnt)
    return answer


## 효율성 통과 못함
def solution2(prices):
    answer = [0] * len(prices)
    check = [0] * len(prices)
    for i in range(len(prices)):
        tmp = prices[i]
        for j in range(0, i):
            if prices[j] <= tmp:
                if check[j] == 0:
                    answer[j] += 1
            else:
                if check[j] == 0:
                    answer[j] += 1
                check[j] = 1
    return answer


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))
