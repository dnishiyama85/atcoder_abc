n, m = map(int, input().strip().split())
hands = []
for _ in range(2 * n):
    row = list(input().strip())
    hands.append(row)

wins = {i: 0 for i in range(2 * n)}

for j in range(m):
    table = sorted([[v, i] for i, v in wins.items()])
    for i in range(0, 2 * n, 2):
        p1 = table[i][1]
        p2 = table[i + 1][1]
        h1 = hands[p1][j]
        h2 = hands[p2][j]
        if h1 == 'G':
            if h2 == 'C':
                wins[p1] -= 1
            elif h2 == 'P':
                wins[p2] -= 1
        elif h1 == 'C':
            if h2 == 'G':
                wins[p2] -= 1
            elif h2 == 'P':
                wins[p1] -= 1
        elif h1 == 'P':
            if h2 == 'G':
                wins[p1] -= 1
            elif h2 == 'C':
                wins[p2] -= 1


table = sorted([[v, i] for i, v in wins.items()])

for v, i in table:
    print(i + 1)
