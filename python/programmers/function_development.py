"""
기능개발
스택/큐
"""


def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for idx, val in enumerate(progresses):
            progresses[idx] = val + speeds[idx]
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                break
        if cnt != 0:
            answer.append(cnt)
    return answer


if __name__ == "__main__":
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))
