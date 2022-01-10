xs = map(int, input().strip().split())

originals = [1, 2, 3, 4, 5]

for i, x in enumerate(xs):
    if x != originals[i]:
        print(originals[i])
        break

