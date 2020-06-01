n = int(input())
a = [int(input()) for _ in range(n)]

sorted_a = sorted(a)

mx = sorted_a[-1]
next = sorted_a[-2]

for _a in a:
    if _a == mx:
        print(next)
    else:
        print(mx)
