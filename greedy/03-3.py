# Part 1. 요구사항 입력

a, b = [int(i) for i in input().split()]
list = []

for i in range(a) :
    list.append([int(a) for a in input().split()])

# Part 2. 문제 해결

max = 0

for num_list in list:
    if max < min(num_list):
        max = min(num_list)

print(max)