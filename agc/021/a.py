n = list(map(int, list(input().strip())))

total = sum(n)

for i in range(len(n)):
    subtotal = 0
    for j in range(i - 1):
        subtotal += n[j]
    subtotal += n[i] - 1
    for k in range(i + 1, len(n)):
        subtotal += 9

    total = max(total, subtotal)

print(total)
