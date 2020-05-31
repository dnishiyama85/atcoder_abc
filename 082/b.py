s = input().strip()
t = input().strip()

s1 = ''.join(sorted(list(s)))
t1 = ''.join(sorted(list(t), reverse=True))

if s1 < t1:
    print('Yes')
else:
    print('No')
