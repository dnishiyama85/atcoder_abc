k = int(input())
n = 1

# 最上位が d でn桁の lunlun 数の個数
def n_lunlun(d, n):
    if n == 1:
        return 1

    if d == 0:
        return n_lunlun(0, n - 1) + n_lunlun(1, n - 1)
    else:
        return n_lunlun(d - 1, n - 1) + n_lunlun(d, n - 1) + n_lunlun(d + 1, n - 1)


while True:
    # n 桁のルンルン数の個数を求める
    lunlun_n = 0
    for d in range(1, 10):
        lunlun_n = d
