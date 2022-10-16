s = input().strip()

length = len(s)

if length == 1:
    print(s + s + s + s + s + s)
elif length == 2:
    print(s + s + s)
else:
    print(s + s)
