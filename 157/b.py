table = [list(map(int, input().strip().split())) for _ in range(3)]
n = int(input())
bs = [int(input()) for _ in range(n)]

bingo = [[False] * 3 for _ in range(3)]

for b in bs:
    for i in range(3):
        for j in range(3):
            if b == table[i][j]:
                bingo[i][j] = True

win = False
for i in range(3):
    row = bingo[i]
    if all(row):
        win = True

for j in range(3):
    col = [bingo[i][j] for i in range(3)]
    if all(col):
        win = True

d1 = [bingo[0][0], bingo[1][1], bingo[2][2]]
d2 = [bingo[0][2], bingo[1][1], bingo[2][0]]

if all(d1) or all(d2):
    win = True

if win:
    print('Yes')
else:
    print('No')
