s = input().strip()
t = input().strip()

match = False

for start in range(0, len(s) - len(t) + 1):
    sub_s = s[start:start+len(t)]
    if t == sub_s:
        match = True
        break

if match:
    print('Yes')
else:
    print('No')
