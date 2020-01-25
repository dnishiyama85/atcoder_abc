import copy
from collections import defaultdict

n = int(input())

count = defaultdict(int)

# (先頭, 末尾) = (h, t) となるモノの数を数える
for i in range(1, n + 1):
    h = int(str(i)[0])
    t = int(str(i)[-1])
    count[(h, t)] += 1

copied_count = copy.deepcopy(count)
ans = 0
for (h, t), v in count.items():
    ans += v * copied_count[(t, h)]

print(ans)
