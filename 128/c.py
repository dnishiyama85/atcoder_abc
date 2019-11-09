import numpy as np

n, m = list(map(int, input().split()))

ks = []
ss = []
for i in range(m):
    row = list(map(int, input().split()))
    k = row.pop(0)
    ss.append(row)


ps = list(map(int, input().split()))

ks = np.array(ks, dtype=np.int64)
ps = np.array(ps, dtype=np.int64)

masks = []
for s in ss:
    mask = sum([2 ** (a - 1)for a in s])
    masks.append(mask)


# 電球iにつながっていて、ONになっているスイッチの個数を2で割ったあまり
def calc_switch_state(i, switch_state):
    num_on = 0
    mask = masks[i]
    switch_state = switch_state & mask
    while switch_state > 0:
        num_on += switch_state % 2
        switch_state //= 2

    return num_on % 2

# i 番目の電球がスイッチの状態sで点灯するかどうか
def is_light_on(i, switch_state):
    return calc_switch_state(i, switch_state) == ps[i]

# 探索
total = 0
for state in range(2**n):
    if all([is_light_on(i, state) for i in range(m)]):
        total += 1

print(total)

