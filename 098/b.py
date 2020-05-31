n = int(input())
s = input().strip()

mx = 0
for i in range(len(s)):
    first = set(list(s[:i + 1]))
    second = set(list(s[i + 1:]))

    intersection = first & second
    mx = max(len(intersection), mx)

print(mx)
