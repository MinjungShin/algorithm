"""
타겟 넘버
"""


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt


def dfs(numbers, target, h, total):
    global cnt
    if h == len(numbers):
        if total == target:
            cnt += 1
    else:
        dfs(numbers, target, h + 1, total + numbers[h])
        dfs(numbers, target, h + 1, total - numbers[h])


if __name__ == "__main__":
    numbers = [4, 1, 2, 1]
    target = 4
    cnt = 0
    print(solution(numbers, target))
