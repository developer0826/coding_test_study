input_arr = input()
result_arr = []
result_num = 0
result = ''

for i in input_arr :
    if i.isalpha() : result_arr.append(i)
    else : result_num += int(i)

result_arr.sort()
result = ''.join(result_arr) + str(result_num)
print(result)