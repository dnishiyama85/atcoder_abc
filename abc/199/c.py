n = int(input())
s = list(input().strip())
q = int(input())

s1 = s[:n]
s2 = s[n:]

for _ in range(q):
    t, a, b = map(int, input().strip().split())
    a -= 1
    b -= 1
    if t == 1:
        if b < n:
            s1[a], s1[b] = s1[b], s1[a]
        elif a >= n:
            a -= n
            b -= n
            s2[a], s2[b] = s2[b], s2[a]
        else:
            b -= n
            s1[a], s2[b] = s2[b], s1[a]
    else:
        s1, s2 = s2, s1

print(''.join(s1 + s2))
