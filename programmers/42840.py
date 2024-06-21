# 프로그래머스 알고리즘 고득점 Kit
# [완전탐색] - 모의고사 Lv.1
def solution(answers):
    answer = []
    len_ans = len(answers)

    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    person = [person_1, person_2, person_3]

    person_answers = []
    for i in person:
        person_answers.append(i * (len_ans // len(i)) + i[:len_ans % len(i)])

    person_ans_cnt = []
    for i in person_answers:
        person_ans_cnt.append(sum([p == a for p, a in zip(i, answers)]))
    
    answer_int = max(person_ans_cnt)
    for i in range(3):
        if person_ans_cnt[i] == answer_int:
            answer.append(i+1)
    
    return answer