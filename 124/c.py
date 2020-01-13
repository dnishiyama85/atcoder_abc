s = input().strip()

# 0101010... または 1010101... のどちらかになるしかない。

count0 = 0
count1 = 0
for i, c in enumerate(s):
    if i % 2 == 0:
        if c == '0':
            count1 += 1
        else:
            count0 += 1
    else:
        if c == '0':
            count0 += 1
        else:
            count1 += 1

count = min(count0, count1)
print(count)
