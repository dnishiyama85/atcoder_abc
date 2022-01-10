N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

inner = sum([a * b for a, b in zip(A, B)])

if inner == 0:
    print('Yes')
else:
    print('No')
