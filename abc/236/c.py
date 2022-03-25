n, m = map(int, input().strip().split())
ss = input().strip().split()
ts = input().strip().split()

stop = {}
for t in ts:
    stop[t] = True

for s in ss:
    ans = 'Yes' if s in stop else 'No'
    print(ans)
