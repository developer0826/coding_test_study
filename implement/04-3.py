hori, vert = input()

diff = ord('a') - 1
hori = ord(hori) - diff
vert = int(vert)

directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
result = 0

for h, v in directions:
    new_hori = hori + h
    new_vert = vert + v
    if new_hori * new_vert > 0 : result += 1

print(result)