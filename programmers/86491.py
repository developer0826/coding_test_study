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