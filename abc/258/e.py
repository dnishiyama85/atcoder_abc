n, q, x = map(int, input().strip().split())
ws = list(map(int, input().strip().split()))
ks = []

# 箱に詰める周期を見つける。
# 箱の重さはたかだかN種類しかない。詰め始めるのがWiから始まるもの。
# それより少ない場合もある。
# 箱詰めをしていって、詰めはじめが前と同じになったらそれが周期になっている。
start = {}
box_idx = 0
start_idx = 0
weight = 0
to_start = True
count = 0
potato = 0
potato_nums = []
c = 0
box_num = 0
while True:
    count += 1
    if to_start:
        if box_idx in start:
            # 周期を見つけた
            start_period = box_idx
            break
        start_idx = box_idx
        to_start = False


    weight += ws[box_idx]
    potato += 1
    box_idx += 1
    if box_idx >= n:
        box_idx = 0

    if weight >= x:
        start[start_idx] = box_num
        box_num += 1
        potato_nums.append(potato)
        weight = 0
        potato = 0
        to_start = True

# print(start)
# print("count = ", count)
# print(potato_nums)
# print("box_num =", box_num)
# print("start_period = ", start_period)
len_box = len(potato_nums)
period = len_box - start_period
for _ in range(q):
    k = int(input()) - 1
    if k < len_box:
        print(potato_nums[k])
    else:
        print(potato_nums[k % len_box] + 1)
