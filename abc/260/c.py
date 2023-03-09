n, x, y = map(int, input().strip().split())

# 普通に全部交換してしまえば良い?
stack = [(n, 'r', 1)]
count = 0
while len(stack) > 0:
    jewell = stack.pop()
    level, color, num = jewell
    if color == 'r':
        if level >= 2:
            new_r = (level - 1, 'r', num)
            new_b = (level, 'b', x * num)
            stack.append(new_r)
            stack.append(new_b)
    if color == 'b':
        if level >= 2:
            new_r = (level - 1, 'r', num)
            new_b = (level - 1, 'b', y * num)
            stack.append(new_r)
            stack.append(new_b)
        if level == 1:
            count += num

print(count)
