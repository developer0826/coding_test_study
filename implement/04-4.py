vert_max, hori_max = list(map(int, input().split()))
a, b, d = list(map(int, input().split()))
d = str(d)

game_map = [list(map(int, input().split())) for _ in range(vert_max)]
visit_map = []

direction = ['0', '1', '2', '3']
a_move = [-1, 0, 1, 0]
b_move = [0, 1, 0, -1]

for _ in range(vert_max) :
    line = []
    for _ in range(hori_max) :
        line.append(0)
    visit_map.append(line)

visit_map[a][b] = 1

def get_next_position(d_str):
    this_idx = direction.index(d_str)
    next_idx = this_idx - 1 if this_idx != 0 else 3

    next_d = direction[next_idx]
    next_a = a + a_move[next_idx]
    next_b = b + b_move[next_idx]

    return [next_d, next_a, next_b]

def get_visit_cnt() :
    cnt = 0
    for line in visit_map:
        cnt += sum(line)
    return cnt

def is_available(a, b) :
    if a < 0 or b < 0 or a > (vert_max - 1) or b > (hori_max - 1) : return False
    else :
        return game_map[a][b] + visit_map[a][b] == 0

# 환경 설정 완료 #
# 문제 풀이 시작 #

this_space_cnt = 0
while(True) :
    this_space_cnt += 1
    if this_space_cnt > 4 :
        now_idx = direction.index(d)
        next_a = a - a_move[now_idx]
        next_b = b - b_move[now_idx]
        if is_available(next_a, next_b) :
            a, b = next_a, next_b
            visit_map[a][b] = 1
            this_space_cnt = 0
            continue
        else : break
    else :
        next_d, next_a, next_b = get_next_position(d)
        if is_available(next_a, next_b) :
            d, a, b = next_d, next_a, next_b
            visit_map[a][b] = 1
            this_space_cnt = 0
        else :
            d = next_d

print(get_visit_cnt())