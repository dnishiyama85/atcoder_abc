a, b, c, k = map(int, input().strip().split())


def solve():
    global k

    total = 0
    num_a = min(k, a)

    total += num_a

    k -= num_a

    if k <= 0:
        return total

    num_b = min(k, b)

    if k <= 0:
        return total

    k -= num_b

    num_c = k
    total -= num_c

    return total

print(solve())
