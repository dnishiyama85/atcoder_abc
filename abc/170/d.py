import collections

n = int(input())
d = list(map(int, input().strip().split()))

counts = collections.Counter(d)
dic = {a: True for a, c in counts.items()}

keys = sorted(dic.keys())
last = keys[-1]

for k in keys:
    if dic[k]:
        n = 2
        while k * n <= last:
            if k * n in dic:
                dic[k * n] = False
            n += 1
    # 重複していた場合の処理
    if counts[k] > 1:
        dic[k] = False

count = len([True for v in dic.values() if v])
print(count)
