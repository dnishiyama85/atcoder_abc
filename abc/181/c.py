N = int(input())

xy = [list(map(int, input().strip().split())) for _ in range(N)]

count = 0
for i in range(N):
    xi, yi = xy[i][0], xy[i][1]
    for j in range(i + 1, N):
        xj, yj = xy[j][0], xy[j][1]
        for k in range(j + 1, N):
            xk, yk = xy[k][0], xy[k][1]
            vec1 = (xj - xi, yj - yi)
            vec2 = (xk - xi, yk - yi)
            if vec1[0] * vec2[1] - vec1[1] * vec2[0] == 0:
                count += 1

if count > 0:
    print('Yes')
else:
    print('No')
