import bisect

_n = input()
ls = list(sorted(map(int, input().strip().split())))
total = 0

for i in range(len(ls) - 2):
    for j in range(i + 1, len(ls) - 1):
        a = ls[i]
        b = ls[j]
        left = j + 1
        num = bisect.bisect_left(ls, a + b) - left
        total += num

print(total)


