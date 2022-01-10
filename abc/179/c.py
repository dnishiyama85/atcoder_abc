N = int(input())
count = 0

for A in range(1, N):
    count += (N + A - 1) // A - 1

print(count)
