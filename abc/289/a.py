s = input().strip()
t = []

for c in s:
    if c == '0':
        t.append('1')
    else:
        t.append('0')

print(''.join(t))
