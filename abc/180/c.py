N = int(input())

i = 1
ans = []
while i * i <= N:
    if N % i == 0:
        if i * i != N:
            ans.append(i)
            ans.append(N // i)
        else:
            ans.append(i)
    i += 1

ans = sorted(ans)
for a in ans:
    print(a)
