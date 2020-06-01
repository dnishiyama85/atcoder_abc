d, n = map(int, input().strip().split())


def judge(num):
    count = 0
    while True:
        if count == d:
            return num % 100 != 0

        if num % 100 == 0:
            count += 1
            num //= 100
        else:
            return False


found = 0
num = 1
while True:
    if judge(num):
        found += 1

    if found == n:
        print(num)
        break

    num += 1
