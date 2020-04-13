x = int(input())

n500 = x // 500

rest = x - n500 * 500

n5 = rest // 5

ans = n500 * 1000 + n5 * 5

print(ans)
