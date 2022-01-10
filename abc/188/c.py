N = int(input())
A = list(map(int, input().strip().split()))
rate_to_id = {}
for id in range(len(A)):
    rate_to_id[A[id]] = id

while len(A) > 2:
    next_A = []
    for i in range(0, len(A), 2):
        a = A[i]
        b = A[i + 1]
        if a > b:
            next_A.append(a)
        else:
            next_A.append(b)

    A = next_A

second_rate = min(A)
second_id = rate_to_id[second_rate]
print(second_id + 1)
