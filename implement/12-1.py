str_arr = list(input())
idx = len(str_arr) // 2

first = list(map(int, str_arr[:idx]))
second = list(map(int, str_arr[idx:]))

f_sum = sum(first)
s_sum = sum(second)

if f_sum == s_sum:
    print('LUCKY')
else:
    print('READY')