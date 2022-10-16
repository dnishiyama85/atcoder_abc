n = int(input())
s = input().strip()

nums = set()

# 1 〜 n から3つを選ぶやり方
for d1 in range(0, n - 2):
    for d2 in range(d1 + 1, n - 1):
        for d3 in range(d2 + 1, n):
            num = int(s[d1]) * 100 + int(s[d2]) * 10 + int(s[d3])
            nums.add(num)

print(len(nums))
