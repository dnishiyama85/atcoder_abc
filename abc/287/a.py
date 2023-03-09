n = int(input())

sansei = 0

for _ in range(n):
    s = input().strip()
    if s == 'For':
        sansei += 1

if sansei * 2 > n:
    print('Yes')
else:
    print('No')
