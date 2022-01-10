N, M = map(int, input().strip().split())
conditions = [list(map(int, input().strip().split())) for _ in range(M)]
K = int(input())
choices = [list(map(int, input().strip().split())) for _ in range(K)]

max_satisfied = 0

for i in range(2 ** K):
    dishes = [0] * N
    for j in range(K):
        b = (i >> j) & 1
        if b == 0:
            choice = choices[j][0]
        else:
            choice = choices[j][1]

        dishes[choice - 1] += 1

    # 集計
    satisfied = 0
    for a, b in conditions:
        if dishes[a - 1] > 0 and dishes[b - 1] > 0:
            satisfied += 1

    max_satisfied = max(max_satisfied, satisfied)

print(max_satisfied)
