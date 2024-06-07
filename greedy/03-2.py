# Part 1. 요구사항 입력
n, m, k = [int(i) for i in input().split()]
num_list = list(map(int, input().split()))

# Part 2. 풀이
result = 0
num_list.sort(reverse=True)

max_times = m // k * k
second_times = m % k
result = num_list[0] * max_times + num_list[1] * second_times

print(result)

##### For문 이용 #####

# while m > 0 :

#     for i in range(k):
#         if m < 1 : break
#         result += num_list[0]
#         m -= 1

#     if m < 1 : break
#     result += num_list[1]
#     m -= 1

# print(result)