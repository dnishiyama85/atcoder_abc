from collections import defaultdict

INF = 1e9

cards = [tuple(map(int, input().strip().split())) for _ in range(100)]


map = defaultdict(lambda : None)
for num, card_pos in enumerate(cards):
    map[card_pos] = num


def get_route(start, goal):
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


def get_just_before(route, goal):
    x, y = goal
    last_action = route[-1]
    if last_action == 'D':
        x -= 1
    elif last_action == 'U':
        x += 1
    elif last_action == 'R':
        y -= 1
    elif last_action == 'L':
        y += 1

    return x, y


def actions_when_skip1(pos, card_pos):
    # 直前のマスに山のトップのカードをいったん置いて、次のカードを取って、
    # いったんおいておいたカードを回収し、次のカードのとこまで戻るまでの行動
    route = get_route(pos, card_pos)
    just_before = get_just_before(route, card_pos)
    if map[just_before] is not None:
        # いったん置くことができない
        return False

    reverse_actions = {
        'D': 'U',
        'U': 'D',
        'R': 'L',
        'L': 'R',
    }

    actions = route[:-1]
    actions.append('O')
    actions.append(route[-1])
    actions.append('I')
    actions.append(reverse_actions[route[-1]])
    actions.append('I')
    actions.append(route[-1])

    return actions


pos = 0, 0
total_actions = []

i = 0
# import pdb; pdb.set_trace()
while i < len(cards):
    if i == len(cards) - 1:
        card_pos = cards[i]
        route = get_route(pos, card_pos)
        total_actions.extend(route)
        total_actions.append('I')
        pos = card_pos
        i += 1
        continue

    # 次に
    # A) 素直に i → i + 1 と取るか
    # B) 逆に i + 1 → i と取るか
    # どっちがお得か？
    next_card = cards[i]
    next2_card = cards[i + 1]

    # B) の場合がそもそも可能か？ TODO: カードの仮の削除
    acts_B = actions_when_skip1(next2_card, next_card)
    if acts_B is False:
        card_pos = cards[i]
        route = get_route(pos, card_pos)
        total_actions.extend(route)
        total_actions.append('I')
        pos = card_pos
        i += 1
        map[card_pos] = None
        continue

    # A) の場合
    route1 = get_route(pos, next_card)
    cost_A = len(route1)\
             + 1\
             + len(get_route(next_card, next2_card)) \
             + 1
    # B) の場合
    route2 = get_route(pos, next2_card)
    cost_B = len(route2)\
             + 1 \
             + len(acts_B)

    if cost_A <= cost_B:
        total_actions.extend(route1)
        total_actions.append('I')
        pos = next_card
        map[next_card] = None
        i += 1
    else:
        # スキップしたほうがお得
        total_actions.extend(route2)
        total_actions.append('I')
        total_actions.extend(acts_B)
        pos = next_card
        map[next_card] = None
        map[next2_card] = None
        i += 2

print(''.join(total_actions))
