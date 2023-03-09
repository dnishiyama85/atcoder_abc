s = input().strip()
t = input().strip()

for i in range(len(s)):
    if s[i] != t[i]:
        print(i + 1)
        exit(0)

print(len(t))
