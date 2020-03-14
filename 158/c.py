a, b = map(int, input().strip().split())


def check(p):
    return int(p * 0.08) == a and int(p * 0.10) == b


def check_all():
    for p in range(10001):
        if check(p):
            return p

    return -1


ans = check_all()
print(ans)
