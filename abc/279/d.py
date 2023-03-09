import math

a, b = map(int, input().strip().split())

ans = math.pow(a / (2 * b), 2.0 / 3.0) - 1

ans_0 = int(ans)
ans_1 = int(ans) - 1
ans_2 = int(ans) + 1

if ans_1 <= 0:
    ans_1 = 0

t0 = a / math.sqrt(ans_0 + 1) + b * ans_0
t1 = a / math.sqrt(ans_1 + 1) + b * ans_1
t2 = a / math.sqrt(ans_2 + 1) + b * ans_2

print(min([t0, t1, t2]))
