N = int(input())
A = list(map(int, input().strip().split()))

_max = A[0]
step = 0
for i in range(1, N):
    if _max > A[i]:
        step += _max - A[i]
    else:
        _max = A[i]

print(step)
