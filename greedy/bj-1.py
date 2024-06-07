# 코딩테스트 스터디 숙제
# 백준 11399번: ATM
# https://www.acmicpc.net/problem/11399

people = input()
times = [int(i) for i in input().split()]
idx = 1
result = 0

for i in sorted(times, reverse=True):
    result += i * idx
    idx += 1

print(result)