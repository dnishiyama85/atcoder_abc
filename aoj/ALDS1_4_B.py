n = int(input())
ss = list(map(int, input().strip().split()))
q = int(input())
ts = list(map(int, input().strip().split()))

# ss中のtの左端を見つける
def bin_search(t):
    left = -1
    right = n - 1
    while left < right - 1:
        center = (left + right) // 2
        if t <= ss[center]:
            right = center
        elif ss[center] < t:
            left = center

    ans = 0
    i = right
    while i < n and ss[i] == t:
        ans += 1
        i += 1

    return 1 if ans > 0 else 0

total = sum([bin_search(t) for t in ts])
print(total)
