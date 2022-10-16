n, q = map(int, input().strip().split())

balls = [i for i in range(n)]

# 整数xが書かれているボールが左から何番目にあるかを管理する
x_positions = [0] * n
for x in range(n):
    x_positions[x] = x

for _ in range(q):
    x = int(input()) - 1
    x_pos = x_positions[x]
    if x_pos < n - 1:
        right_x = balls[x_pos + 1]
        # swap
        balls[x_pos], balls[x_pos + 1] = balls[x_pos + 1], balls[x_pos]
        x_positions[x] = x_positions[x] + 1
        x_positions[right_x] = x_pos
    else:
        left_x = balls[x_pos - 1]
        balls[x_pos], balls[x_pos - 1] = balls[x_pos - 1], balls[x_pos]
        x_positions[x] = x_positions[x] - 1
        x_positions[left_x] = x_pos

for i in range(n):
    balls[i] += 1

print(' '.join(map(str, balls)))
