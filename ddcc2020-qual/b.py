n = int(input())
as_ = list(map(int, input().strip().split()))

total_length = sum(as_)
current = 0
for a in as_:
    if current + a == total_length // 2:
        print(0)
        exit(0)
    if current + a > total_length / 2:
        candidate1 = current
        candidate2 = current + a
        break

    current += a

left1 = candidate1
right1 = total_length - left1
left2 = candidate2
right2 = total_length - left2


ans = min(
    right1 - left1, # 左が短いので左を伸ばすまたは右を縮める
    left2 - right2 # 左が長いので左を縮めるまたは右を伸ばす
)
print(ans)
