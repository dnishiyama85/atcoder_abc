n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    data.append((x, y))

s = input().strip()

# Y座標が同じ人をまとめる
same_y = {}
for i, (x, y) in enumerate(data):
    if y not in same_y:
        same_y[y] = {'R': [], 'L': []}
    if s[i] == 'L':
        same_y[y]['L'].append(x)
    else:
        same_y[y]['R'].append(x)


# 右向きに歩いている人で一番左にいる人が
# 左向きに歩いている人で一番右にいる人より左
# にいれば衝突する。
collision = False
for d in same_y.values():
    left = sorted(d['L'])
    right = sorted(d['R'])

    if len(left) == 0 or len(right) == 0:
        continue

    if right[0] < left[-1]:
        collision = True
        break

if collision:
    print('Yes')
else:
    print('No')
