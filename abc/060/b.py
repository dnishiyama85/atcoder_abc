import fractions

a, b, c = map(int, input().strip().split())

if a % b == 0 or b <= c:
    print('NO')
else:
    r = a % b
    d = fractions.gcd(r, b)
    if d == 1:
        print('YES')
    elif c % d == 0:
        print('YES')
    else:
        print('NO')
