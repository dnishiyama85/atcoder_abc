s = input().strip()
count = 0
for c in s:
    if c == 'v':
        count += 1
    if c == 'w':
        count += 2

print(count)
