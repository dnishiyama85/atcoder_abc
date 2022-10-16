s = input().strip()
n = len(s)

max_length = 0

for start in range(0, n):
    for end in range(start + 1, n):
        substr = s[start:end]
        removed = (substr
                   .replace('A', '')
                   .replace('C', '')
                   .replace('G', '')
                   .replace('T', ''))

        if removed == '':
            max_length = max(max_length, len(substr))

print(max_length)
