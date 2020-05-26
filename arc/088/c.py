x, y = map(int, input().strip().split())

last = x
count = 0
while last <= y:
    last *= 2
    count += 1

print(count)
