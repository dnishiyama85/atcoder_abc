n = int(input())

# n のビットが１となる場所を調べる
positives = []
b = 0
while n > 0:
    if n & 1 == 1:
        positives.append(b)

    n >>= 1
    b += 1

max_num = 2 ** len(positives)
for x in range(max_num):
    x_bits = [0] * len(positives)
    b = 0
    while x > 0:
        if x & 1 == 1:
            x_bits[b] = 1
        x >>= 1
        b += 1

    ans = sum([xb * 2 ** b for (xb, b) in zip(x_bits, positives)])
    print(ans)
