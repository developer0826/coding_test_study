# 주어지는 값 받아오기
kind, total = map(int, input().split())
coins = [int(input()) for _ in range(kind)]

# 풀이
coins.sort(reverse=True)
result = 0

for coin in coins :
    if total >= coin :
        this_coin_cnt = total // coin
        this_coin_total = coin * this_coin_cnt
        total = total - this_coin_total
        result += this_coin_cnt

print(result)