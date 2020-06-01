import fractions

a, b = map(int, input().strip().split())
lcm = a * b // fractions.gcd(a, b)
print(lcm)
