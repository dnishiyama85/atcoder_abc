n = int(input())
as_ = list(map(int, input().strip().split()))
leq2000 = [0] * 2001

for a in as_:
    leq2000[a] = 1

for i in range(0, 2001):
    if leq2000[i] == 0:
        print(i)
        exit(0)
