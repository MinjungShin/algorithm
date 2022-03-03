"""
프린터
스택/큐
"""

from collections import deque


def solution(priorities, location):
    queue = deque(i for i in range(len(priorities)))
    cnt = 0

    while queue:
        tmp = queue.popleft()
        if any(priorities[x] > priorities[tmp] for x in queue):
            queue.append(tmp)
        else:
            cnt += 1
            if tmp == location:
                break
    return cnt


if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))
