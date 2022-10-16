n = int(input())
xs = list(map(int, input().strip().split()))
cs = list(map(int, input().strip().split()))

for i in range(n):
    xs[i] -= 1

# 貪欲？
# 今残っている中で、不満度のたまりが最も低い人（誰からも憎まれていない人）から配っていく。

# i 番目の人が集めている憎しみ
hates = {}
for i in range(n):
    hates[i] = 0

for x, c in zip(xs, cs):
    hates[x] += c

# print(hates)

hates_id = sorted(hates, key=hates.get)
print(hates_id)
next_p = [-1] * n
for i, p in enumerate(hates_id):
    if i > 0:
        next_p[i] = p

print(next_p)
total_hate = 0
while len(hates) > 0:
    min_hate_i = min(hates, key=hates.get)
    hate = hates[min_hate_i]
    total_hate += hate
    x = xs[min_hate_i]
    if x in hates:
        hates[x] -= cs[min_hate_i]
    del hates[min_hate_i]
    #  print(hates)

print(total_hate)