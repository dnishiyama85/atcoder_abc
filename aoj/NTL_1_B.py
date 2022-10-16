# べき乗を高速に求めるアルゴリズム
# m^n を求める。
m, n = map(int, input().strip().split())

MOD = 1000000007

# m^2h を順に求めていく:
# m^2h = m^(2h-1) * m^(2h-1)
# k 〜 log(n) なのでこれは log(n) 回の計算でできる。

m_powers = [0] * 100  # 適当に多めに取っておく
m_powers[0] = m  # m^1 = m^(2^0) = m

for h in range(1, 100):
    m_powers[h] = m_powers[h - 1] * m_powers[h - 1]
    m_powers[h] %= MOD


# n を2進数表記する
# n = b0 * 2^0 + b1 * 2^1 + b2 * 2^2 + ... + bk * 2^k
# m^n = ((m^(2^0))^b0) * ((m^(2^1)^b1) * ... * ((m^(2^k)^bk)
k = 0
result = 1
# 以下では2進表記のビット (bi) を求めるのと
# 計算結果の積を作っていくのを同時にやっている。
while n > 0:
    b = n & 1
    m_pow_k = m_powers[k]
    result *= m_pow_k ** b
    result %= MOD
    n >>= 1
    k += 1

print(result)
