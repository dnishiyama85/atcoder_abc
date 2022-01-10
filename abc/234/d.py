n, k = list(map(int, input().strip().split()))
ps = list(map(int, input().strip().split()))[::-1]
ans = []
removed_set = set()
# 逆から考える
# 全部揃っているときに k 番目に大きい値は
now = n - k + 1
ans.append(now)
# 取り除いていく
for i in range(0, n - k):
    removed = ps[i]
    removed_set.add(removed)
    # 取り除かれた値が now 以上の場合、 k 番目に大きい値は1減る
    if removed >= now:
        now -= 1
        while now in removed_set:
            now -= 1

    # そうでない場合は変わらず
    ans.append(now)

for a in ans[::-1]:
    print(a)
