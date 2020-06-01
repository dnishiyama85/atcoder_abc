s = int(input())

d = {}

n = 1

while s not in d:
    d[s] = n
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
    n += 1

print(n)
