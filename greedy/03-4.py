n, k = [int(i) for i in input().split()]

i = 0
# while n > 1 :
#     if n % k == 0 :
#         n = n // k
#     else : n -= 1
#     i += 1

# print(i)

while n >= k :
    if n % k == 0 :
        n = n // k
    else : n -= 1
    i += 1

i += n - 1

print(i)