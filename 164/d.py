s = input().strip()
cnt = 0
for i in range(0, len(s) - 1):
    for j in range(i, len(s) - 1):
        num = int(s[i:j + 1])
        if num % 2019 == 0:
            print(num)
            cnt += 1

print(cnt)
