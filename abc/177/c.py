N = int(input())
A = list(map(int, input().strip().split()))
S = sum(A)
ans = 0
for i in range(N - 1):
    S -= A[i]
    ans += A[i] * S

print(ans % 1000000007)

