s = input().strip()

counts = [0] * len(s)

for i, c in enumerate(s):
    prev = counts[i - 1] if i > 0 else 0
    if c == 'B':
        counts[i] = prev + 1
    else:
        counts[i] = prev

allowable = 0
for i in range(len(s)):
    if s[i] == 'W' and i > 0:
        count = counts[i - 1]
        allowable += count

print(allowable)
