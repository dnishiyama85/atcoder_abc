n = int(input())
as_ = map(int, input().strip().split())

num_mul2 = 0
num_mul4 = 0

for a in as_:
    if a % 4 == 0:
        num_mul4 += 1
    elif a % 2 == 0:
        num_mul2 += 1

d = n - num_mul4 * 2 - (num_mul2 // 2) * 2
if num_mul4 > 0:
    d -= 1

if d <= 0:
    print('Yes')
else:
    print('No')
