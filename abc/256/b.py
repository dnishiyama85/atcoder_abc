n = int(input())
as_ = map(int, input().strip().split())

p = 0

runners = []

for a in as_:
    runners.append(0)
    new_runners = []
    for r in runners:
        if r + a >= 4:
            p += 1
        else:
            new_runners.append(r + a)
    runners = new_runners

print(p)
