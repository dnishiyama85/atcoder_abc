n = int(input())

as_ = map(int, input().strip().split())


def color(rate):
    if rate < 400:
        return 0
    elif rate < 800:
        return 1
    elif rate < 1200:
        return 2
    elif rate < 1600:
        return 3
    elif rate < 2000:
        return 4
    elif rate < 2400:
        return 5
    elif rate < 2800:
        return 6
    elif rate < 3200:
        return 7
    else:
        return 8


colors = [0] * 8
num_expert = 0
for a in as_:
    c = color(a)
    if c == 8:
        num_expert += 1
    else:
        colors[c] += 1

num_colors = len([True for c in colors if c > 0])
min_colors = max(num_colors, 1)
max_colors = num_colors + num_expert


print(min_colors, max_colors)
