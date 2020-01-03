# import math
import fractions

a, b, c, d = [int(ch) for ch in input().strip().split()]


# upper 以下で div で割り切れるものの個数
def num_divisor(upper, div):
    return upper // div


# upper 以下で c でも d でも割り切れないものの個数
def num_divisor_c_d(upper, c, d):
    # gcd_cd = c * d // math.gcd(c, d)
    gcd_cd = c * d // fractions.gcd(c, d)

    n1 = num_divisor(upper, c)
    n2 = num_divisor(upper, d)
    n12 = num_divisor(upper, gcd_cd)

    return upper - (n1 + n2 - n12)


ans = num_divisor_c_d(b, c, d) - num_divisor_c_d(a - 1, c, d)

print(ans)
