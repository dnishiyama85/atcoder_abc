a, b, c = list(map(int, input().strip().split()))

ans = ''

if a > 0 and b > 0:
    diff = b - a
    if 0 < diff:
        ans = '<'
    elif 0 > diff:
        ans = '>'
    else:
        ans = '='
elif a > 0 and b == 0:
    ans = '>'
elif a > 0 and b < 0:
    if c % 2 == 0:
        diff = abs(b) - a
        if 0 < diff:
            ans = '<'
        elif 0 > diff:
            ans = '>'
        else:
            ans = '='
    else:
        ans = '>'
elif a == 0 and b > 0:
    ans = '<'
elif a == 0 and b == 0:
    ans = '='
elif a == 0 and b < 0:
    if c % 2 == 0:
        ans = '<'
    else:
        ans = '>'
elif a < 0 and b > 0:
    if c % 2 == 0:
        diff = b - abs(a)
        if 0 < diff:
            ans = '<'
        elif 0 > diff:
            ans = '>'
        else:
            ans = '='
    else:
        ans = '<'
elif a < 0 and b == 0:
    if c % 2 == 0:
        ans = '>'
    else:
        ans = '<'
elif a < 0 and b < 0:
    if c % 2 == 0:
        diff = abs(b) - abs(a)
        if 0 < diff:
            ans = '<'
        elif 0 > diff:
            ans = '>'
        else:
            ans = '='
    else:
        diff = abs(b) - abs(a)
        if 0 < diff:
            ans = '>'
        elif 0 > diff:
            ans = '<'
        else:
            ans = '='

print(ans)
