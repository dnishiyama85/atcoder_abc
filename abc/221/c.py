nums = list(map(int, list(input().strip())))

d = len(nums)
mx = 1

for bits in range(2**d):
    set1 = []
    set2 = []
    idx = 0
    for idx in range(d):
        b = bits & 1
        if b == 0:
            set1.append(nums[idx])
        else:
            set2.append(nums[idx])
        bits >>= 1

    if len(set1) == 0 or len(set2) == 0:
        continue

    if max(set1) == 0 or max(set2) == 0:
        continue

    num1 = int(''.join(map(str, sorted(set1, reverse=True))))
    num2 = int(''.join(map(str, sorted(set2, reverse=True))))

    mx = max(mx, num1 * num2)

print(mx)
