from collections import defaultdict

n = int(input())
as_ = list(map(int, input().strip().split()))

numbers = defaultdict(int)
for a in as_:
    numbers[a] += 1

total = sum([m * (m - 1) // 2 for m in numbers.values()])

for k in range(1, n + 1):
    m_k = as_[k - 1]
    num_k = numbers[m_k]
    ans = total
    if num_k > 1:
        ans += - num_k * (num_k - 1) // 2 \
               + (num_k - 1) * (num_k - 2) // 2

    print(ans)
