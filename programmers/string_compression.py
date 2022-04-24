"""
2020 KAKAO BLIND RECRUITMENT
문자열 압축
"""

string = "aabbaccc"

def solution(s):
    answer = ""
    f_cnt =2147000000

    for i in range(1, len(s) + 1):
        f_answer = ""
        cur = s[0:i]
        cnt = 0
        for j in range(0, len(s), i):
            tmp = s[j:j+i]
            if cur == tmp:
                cnt += 1
            else:
                if cnt == 1:
                    f_answer += cur
                else:
                    f_answer += str(cnt) + cur
                cur = tmp
                cnt = 1
        if cnt == 1:
            f_answer += cur
        else:
            f_answer += str(cnt) + cur
        if f_cnt > len(f_answer):
            answer = f_answer
            f_cnt = len(f_answer)
    return len(answer)

print(solution(string))