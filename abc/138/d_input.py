n = 100000
q = 100000 - 1

print(n, q)
for i in range(n - 1):
    if i < 50000:
        a = 1
        b = i + 1
    else:
        a = 50000
        b = i + 1
    print(a, b)


for i in range(q):
    p = i + 1
    x = 1
    print(p, q)
