_ = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
a = sorted(A, reverse=True)
b = sorted(B)

for i in range(len(b)) :
    result += a[i] * b[i]

print(result)