import numpy as np
# 貪欲法
n = int(input())
ss = []
pos_of_ks = []
for _ in range(n):
    s = list(map(int, list(input().strip())))
    pos = [0] * 10
    for i, k in enumerate(s):
        pos[k] = i
    pos_of_ks.append(pos)

# print(pos_of_ks)
pos_of_ks = np.array(pos_of_ks)
min_t = 1e9

def get_min_t_and_i(pos_of_ks, k, done_list):
    min_t = 1e9
    min_i = None
    for i, (done, pos) in enumerate(zip(done_list, pos_of_ks)):
        if done:
            continue
        pos_of_k = pos[k]
        if pos_of_k < min_t:
            min_t = pos_of_k
            min_i = i

    return min_t + 1, min_i


for k in range(10):
    total_min_t_k = 0
    pos_of_ks_ = pos_of_ks.copy()
    done_list = [False] * n
    for i in range(n):
        min_t_k, min_i = get_min_t_and_i(pos_of_ks_, k, done_list)
        # print(min_t_k, min_i)
        total_min_t_k += min_t_k
        done_list[min_i] = True
        # 回転
        pos_of_ks_ = (pos_of_ks_ - min_t_k) % 10

    min_t = min(min_t, total_min_t_k)

print(min_t - 1)
