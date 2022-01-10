N = int(input())

count = 0
i = 1

while True:
    target = int(str(i) + str(i))
    if target <= N:
        count += 1
    else:
        break

    i += 1

print(count)
