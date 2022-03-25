import re

s = input().strip()
# 最初から回文になっている場合
if s == s[::-1]:
    print('Yes')
    exit(0)

s = re.sub('^a+', '', s)
s = re.sub('a+$', '', s)

# print(s)

trimmed = s
reversed = trimmed[::-1]
# print(trimmed)
# print(reversed)
if trimmed == reversed:
    print('Yes')
else:
    print('No')
