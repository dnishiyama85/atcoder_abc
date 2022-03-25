import math

s = list(input().strip())
# A = 0, B = 1, C = 2
d = {'A': 0, 'B': 1, 'C': 2}
d_inv = ['A', 'B', 'C']
s_num = [d[n] for n in s]

q = int(input())
queries = []
for _ in range(q):
    t, k = map(int, input().strip().split())
    queries.append((t, k))

for t, k in queries:
    # k がどの文字をルートに持つか
    # t回の変換をしたあとは len(s) * 2^t の長さになる
    # → k // (2 ** t) 番目の文字をルートに持つ。
    if t * math.log(2) > math.log(len(s)):
        root = 0
        k2 = k
    else:
        root = s_num[(k - 1) // (2 ** t)]
        k2 = k - root * (2 ** t)

    # k を2進数表示したときの 1 の個数
    num_1_of_k = str.count(bin(k2 - 1), '1')
    # key となる量
    key = (t + root - 1 + num_1_of_k) % 3
    print(d_inv[key])

