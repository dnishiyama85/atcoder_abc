import fractions
from functools import reduce

n = int(input())
as_ = list(map(int, input().strip().split()))


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


lcm_as = lcm_list(as_)

b_sum = sum([lcm_as // a for a in as_]) % 1000000007

print(b_sum)
