h, w = map(int, input().strip().split())
pattern1 = (w + 1) // 2
pattern2 = w // 2

ans = pattern1 * ((h + 1) // 2) + pattern2 * (h // 2)

if h == 1 or w == 1:
    print(1)
else:
    print(ans)
