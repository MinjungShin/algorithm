"""
다리를 지나는 트럭
스택/큐
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    queue = deque()
    done = list()
    size = len(truck_weights)
    answer = 0
    while len(done) < size:
        answer += 1
        for idx, value in enumerate(queue):
            queue[idx][1] += 1
        if queue and queue[0][1] > bridge_length:
            done.append(queue.popleft())
        for _ in range(len(truck_weights)):
            tmp = truck_weights[0]
            if sum(queue[i][0] for i in range(len(queue))) + tmp > weight or len(queue) >= bridge_length:
                break
            else:
                truck_weights.pop(0)
                queue.append([tmp, 1])
    return answer


if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10]
    print(solution(bridge_length, weight, truck_weights))
