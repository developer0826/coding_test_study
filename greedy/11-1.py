population = int(input())

list = list(map(int, input().split()))
list.sort()

print(list)
group_cnt = 0
people_cnt = 0

for fear in sorted(list) :
    people_cnt += 1
    if people_cnt >= fear :
        group_cnt += 1
        people_cnt = 0

print(group_cnt)