# 프로그래머스 알고리즘 고득점 Kit
# [완전탐색] - 최소직사각형 Lv.1
def solution(sizes):
    answer = 0
    widths = []
    heights = []

    # sizes로 들어온 가로, 세로값을 받아
    # 긴 값이 가로(너비)값이 될 수 있도록 기준 잡아 정렬
    for w, h in sizes:
        if w < h:
            w, h = h, w
        
        # 가로/세로를 별도의 리스트에 담는다.
        widths.append(w)
        heights.append(h)
    
    # 지갑의 너비는 너비가 가장 긴 카드의 너비
    # 지갑의 높이는 높이가 가장 긴 카드의 높이여야
    # 모든 카드를 담을 수 있다.
    answer = max(widths) * max(heights)
    return answer