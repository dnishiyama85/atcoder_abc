n = int(input())


def num_div2(m):
    cnt = 0
    while m > 0 and m % 2 == 0:
        cnt += 1
        m //= 2

    return cnt


mx = max([(m, num_div2(m)) for m in range(1, n + 1)], key=lambda t: t[1])
print(mx[0])
