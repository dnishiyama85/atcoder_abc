n = int(input())
ps = list(map(int, input().strip().split()))

numbers = [0] * 200001

min_pointer = 0
for i in range(n):
    next_p = ps[i]
    numbers[next_p] = 1
    if min_pointer != next_p:
        print(min_pointer)
    else:
        while numbers[min_pointer] == 1:
            min_pointer += 1

        print(min_pointer)
