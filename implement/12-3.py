input_str = list(input())
str_len = len(input_str)
times = str_len // 2

min_len = str_len

for split_len in range(1, times+1) :
    str_before = ''
    str_this = ''
    result = ''
    this_cnt = 1
    test_str = input_str.copy()

    split_times = str_len // split_len if str_len % split_len == 0 else (str_len // split_len) + 1

    for i in range(split_times+1) :
        str_this = ''.join(test_str[:split_len])

        if i == 0 :
            pass
        elif str_this == str_before :
            this_cnt += 1
        else :
            if this_cnt != 1 :
                result += str(this_cnt)
            result += str(str_before)
            this_cnt = 1
        
        str_before = str_this
        test_str = test_str[split_len:]
    
    if len(result) < min_len : min_len = len(result)

print(min_len)