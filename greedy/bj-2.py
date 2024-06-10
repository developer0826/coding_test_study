# 코딩테스트 스터디 숙제
# 백준 1931번: 회의실 배정
# https://www.acmicpc.net/problem/1931

# 입력값 정리
cnt = int(input())
times_arr = []
for i in range(cnt):
    start, end = [int(num) for num in input().split()]
    times_arr.append([end, start])

# 문제 해결
result = 0
end = 0
sorted_arr = list(enumerate(sorted(times_arr)))
for index, time in sorted_arr :
    this_end, this_start = time
    if index == 0 :
        result += 1
        end = this_end
    elif end <= this_start :
        end = this_end
        result += 1
print(result)