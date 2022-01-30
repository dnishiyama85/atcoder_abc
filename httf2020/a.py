cards = [list(map(int, input().strip().split())) for _ in range(100)]

pos = 0, 0
actions = []


def get_next_route(start, goal):
    # 縦移動 → 横移動 (縦が x, 横が y)
    cx, cy = start
    nx, ny = goal
    dx = nx - cx
    dy = ny - cy

    x_actions = []
    y_actions = []

    if dx > 0:
        x_actions = ['D'] * dx
    elif dx < 0:
        x_actions = ['U'] * (-dx)

    if dy > 0:
        y_actions = ['R'] * dy
    elif dy < 0:
        y_actions = ['L'] * (-dy)

    return x_actions + y_actions


for card_pos in cards:
    route = get_next_route(pos, card_pos)
    actions.extend(route)
    actions.append('I')
    pos = card_pos

print(''.join(actions))
