N_str = input().strip()
N = int(N_str)
k = len(N_str)
shortest = k

for n in range(1, 2 ** k + 1):
    bits = bin(n)[2:].zfill(k)
    masked = [int(d) for d, b in zip(N_str, bits) if b == '1']
    if sum(masked) % 3 == 0:
        deleted = len([0 for b in bits if b == '0'])
        shortest = min(deleted, shortest)

if shortest == k:
    print(-1)
else:
    print(shortest)
