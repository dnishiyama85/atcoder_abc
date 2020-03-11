h = int(input())

count = 0
p = 0

while h > 0:
    count += 2 ** p
    p += 1
    h //= 2

print(count)
