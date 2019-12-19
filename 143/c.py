n = int(input())
s = input().strip()

p = s[0]
cnt = 1

for i in range(1, n):
    if p == s[i]:
        pass
    else:
        p = s[i]
        cnt += 1

print(cnt)
