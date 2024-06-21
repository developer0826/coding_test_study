# 프로그래머스 알고리즘 고득점 Kit
# [완전탐색] - 최소직사각형 Lv.1
def solution(sizes):
    answer = 0
    widths = []
    heights = []

    for w, h in sizes:
        if w < h:
            w, h = h, w
        widths.append(w)
        heights.append(h)
    
    answer = max(widths) * max(heights)
    return answer