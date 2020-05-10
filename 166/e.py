n = int(input())
as_ = list(map(int, input().strip().split()))

count = 0
for k in range(n):
    # j - i == k となる組み合わせは？
    for i in range(n - k):
        j = i + k
        if as_[i] + as_[j] == k:
            count += 1

print(count)
