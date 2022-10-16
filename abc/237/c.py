import re

s = input().strip()
# 最初から回文になっている場合
if s == s[::-1]:
    print('Yes')
    exit(0)

# 先頭に連続する a の個数
a1 = 0
ind1 = 0
while True:
    if s[ind1] == 'a':
        a1 += 1
        ind1 += 1
    else:
        break

# 末尾に連続する a の個数
a2 = 0
ind2 = len(s) - 1
while True:
    if s[ind2] == 'a':
        a2 += 1
        ind2 -= 1
    else:
        break

if a1 > a2:
    print('No')
    exit(0)

if a1 == a2:
    if s == s[::-1]:
        print('Yes')
    else:
        print('No')
    exit(0)

# a2 - a1 個の a を末尾から消して回文になってればOK
s = s[:-(a2-a1)]
# print(s)

trimmed = s
reversed = trimmed[::-1]
# print(trimmed)
# print(reversed)
if trimmed == reversed:
    print('Yes')
else:
    print('No')
