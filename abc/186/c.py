n = int(input())
count = 0

for i in range(1, n + 1):
    digit = str(i)
    octet = str(oct(i))
    if ('7' not in digit) and ('7' not in octet):
        count += 1

print(count)
