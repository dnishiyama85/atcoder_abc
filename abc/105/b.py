n = int(input())

def num_divisor(m):
    num = 0
    for d in range(1, m + 1):
        if m % d == 0:
            num += 1
    return num

count = 0
for m in range(1, n + 1):
    if m % 2 == 1 and num_divisor(m) == 8:
        count +=1

print(count)
