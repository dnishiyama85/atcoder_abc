k, a, b = map(int, input().strip().split())

# ビスケットa枚を1円に交換し、1円をb枚に交換するという操作を考えると、
# これは操作回数を2回消費して b - a 枚だけビスケットが増える
# よって、 b - a > 2 で残り回数が2回以上なら
# ビスケットを叩いて1枚増やすより常に有利なのでやるべし。

biscuits = 1
if b - a > 2:
    # 何回できる?
    # 最初に a - 1回叩いてビスケットを a 枚に増やす必要がある
    if a - 1 > k:
        # a枚まで増やせないので k 回叩いて終わる
        biscuits += k
    else:
        # a枚まで増やした
        biscuits += a - 1
        k -= a - 1
        if k > 0:
            times = k // 2
            rest = k - times * 2
            biscuits += (b - a) * times
            biscuits += rest
else:
    # 常に叩いて1枚増やすほうがマシ
    biscuits += k

print(biscuits)
