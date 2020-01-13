alphabet = 'abcdefghijklmnopqrstuvwxyz'

c = input().strip()

for i in range(len(alphabet)):
    c2 = alphabet[i]
    if c == c2:
        break

print(alphabet[i + 1])
