hour = int(input())
cnt = 0

for h in range(hour+1) :
    for m in range(60) :
        for s in range(60) :
            time_str = str(h) + str(m) + str(s)
            if time_str.find('3') != -1 :
                cnt += 1

print(cnt)