# 단순하게 푸는 방법...

# space = int(input())
# moving = [i for i in input().split()]
# l, r = 1, 1

# for step in moving:
#     if step == 'L' :
#         r -= 1
#         if r < 1 : r = 1
#     elif step == 'R' :
#         r += 1
#         if r > space : r = space
#     elif step == 'U' :
#         l -= 1
#         if l < 1 : l = 1
#     elif step == 'D' :
#         l += 1
#         if l > space : l = space

# print(l, r)

# Tree로 추후 응용할 수 있는 방법

space = int(input())
steps = [i for i in input().split()]

move = ['L', 'R', 'U', 'D']
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]
x, y = 1, 1

for step in steps :
    move_index = move.index(step)
    move_x = mx[move_index]
    move_y = my[move_index]
    
    mvd_x = x + move_x
    mvd_y = y + move_y
    
    if mvd_x > space or mvd_x < 1 or mvd_y > space or mvd_y < 1 :
        continue
    else :
        x, y = mvd_x, mvd_y

print(x, y)