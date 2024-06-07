money = int(input())

list = [500, 100, 50, 10]
count = 0

for i in list:
    while money // i > 0 :
        money -= i
        count += 1

print(count)