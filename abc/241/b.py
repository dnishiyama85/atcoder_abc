from collections import defaultdict

n, m = map(int, input().strip().split())
as_ = map(int, input().strip().split())
bs = map(int, input().strip().split())

pasta = defaultdict(int)
for a in as_:
    pasta[a] += 1

success = True
for b in bs:
    if pasta[b] == 0:
        success = False
    else:
        pasta[b] -= 1

if success:
    print('Yes')
else:
    print('No')
