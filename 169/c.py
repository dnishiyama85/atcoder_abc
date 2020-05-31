import decimal

decimal.getcontext().prec = 100

a, b = input().strip().split()
a = decimal.Decimal(a)
b = decimal.Decimal(b)

print(int(a * b))
