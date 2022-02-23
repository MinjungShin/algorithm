"""
2019 KAKAO BLIND RECRUITMENT
오픈채팅방
"""

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
words = ["Enter", "Leave", "Change"]


def solution(record):
    ids = dict()
    answer = []
    inn = "님이 들어왔습니다."
    outt = "님이 나갔습니다."

    for x in record:
        tmp = x.split(' ')
        if tmp[0] in ["Enter", "Change"]:
            ids[tmp[1]] = tmp[2]

    for x in record:
        tmp = x.split(' ')
        if tmp[0] == "Enter":
            answer.append(ids[tmp[1]] + inn)
        elif tmp[0] == "Leave":
            answer.append(ids[tmp[1]] + outt)
    return answer


print(solution(record))
