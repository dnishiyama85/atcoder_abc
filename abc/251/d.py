w = int(input())

ans = []
for i in range(1, 101):
    ans.append(i)
    ans.append(i * 100)
    ans.append(i * 10000)

ans = sorted(ans)
print(300)
print(' '.join(map(str, ans)))
