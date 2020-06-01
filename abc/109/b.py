n = int(input())
words = [input().strip() for _ in range(n)]

said = []
prev = ""
safe = True
for w in words:
    if prev == "":
        prev = w
        said.append(w)
        continue
    else:
        if prev[-1] != w[0]:
            safe = False
            break
        else:
            if w in said:
                safe = False
                break
            else:
                prev = w
                said.append(w)

if safe:
    print('Yes')
else:
    print('No')
