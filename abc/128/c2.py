import numpy as np

n, m = map(int, input().strip().split())
bits = []
for _ in range(m):
    ks = list(map(int, input().strip().split()))
    k = ks[0]
    s = np.array(ks[1:]) - 1
    bit = np.sum(2 ** s)
    bits.append(bit)

ps = list(map(int, input().strip().split()))

total_count = 0
for switch in range(0, 2**n):
    ok = True
    for bit, p in zip(bits, ps):
        b = bit & switch
        # b に現れる1の数を数える
        bit_count = 0
        while b > 0:
            bit_count += b & 1
            b = b >> 1
        if bit_count % 2 != p:
            ok = False
            break

    if ok:
        total_count += 1

print(total_count)
