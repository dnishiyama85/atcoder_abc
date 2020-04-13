a, b = map(int, input().strip().split())

outlet = 1
taps = 0
while outlet < b:
    taps += 1
    outlet += a - 1

print(taps)
