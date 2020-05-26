s = input().strip()
t = input().strip()

ok = False
if len(s) + 1== len(t):
    if s == t[:-1]:
        ok = True

if ok:
    print('Yes')
else:
    print('No')
