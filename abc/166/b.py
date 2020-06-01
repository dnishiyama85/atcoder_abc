n, k = map(int, input().strip().split())
okashi = [0] * n
for i in range(k):
    d = int(input())
    as_ = list(map(int, input().strip().split()))
    for a in as_:
        okashi[a - 1] += 1

no_okashi = [1 for ok in okashi if ok == 0]

print(len(no_okashi))
