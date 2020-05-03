s = input().strip()

min_diff = 1000000

for i in range(len(s) - 2):
    num = int(s[i: i+3])
    diff = abs(753 - num)
    min_diff = min(diff, min_diff)

print(min_diff)
