n = int(input())
s = 1


def print_s(k):
    if k == 1:
        return "1"

    return print_s(k - 1) + f" {k} " + print_s(k - 1)

print(print_s(n))
