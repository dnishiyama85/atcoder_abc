N, A, B = map(int, input().strip().split())
print(N, A, B)
hs = sorted([int(input()) for _i in range(N)])
print(hs)
count = 0
while len(hs) > 0:
    max_h = hs.pop(-1)
    m = max_h / A 



