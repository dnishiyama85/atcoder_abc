N = int(input())

length = len(str(N))
ans = length // 3

k = 1000000
count = 0

while True:
    if N < k:
        count += 10 ** 6 - 1 - 10 ** 3 - 1
