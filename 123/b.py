import itertools

times = [int(input()) for _ in range(5)]

p = itertools.permutations([0, 1, 2, 3, 4])

min_time = 10e9
for orders in p:
    current_time = 0
    for idx, order in enumerate(orders):
        t = times[order]
        current_time += t
        if idx < 4 and current_time % 10 != 0:
            current_time += 10 - current_time % 10

    min_time = min(min_time, current_time)

print(min_time)
