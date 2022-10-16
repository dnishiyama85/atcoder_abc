n = int(input())

alive = [True] * (2 * n + 2)
p = 1

while True:
    while not alive[p]:
        p += 1

    print(p, flush=True)
    alive[p] = False
    a = int(input())
    if a == 0:
        break

    alive[a] = False


