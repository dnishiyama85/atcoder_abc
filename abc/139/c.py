n = int(input())
h = list(map(int, input().strip().split()))

left = 0
right = 0
max_len = 0

while left < n:
    if right == n - 1:
        max_len = max(max_len, right - left)
        break

    if h[right] >= h[right + 1]:
        right += 1
    else:
        max_len = max(max_len, right - left)
        left = right + 1
        right = left

print(max_len)
