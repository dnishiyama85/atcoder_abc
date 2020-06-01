n = int(input())
s = input().strip()

comibinations = [
    ['R', 'G', 'B'],
    ['R', 'B', 'G'],
    ['G', 'R', 'B'],
    ['G', 'B', 'R'],
    ['B', 'R', 'G'],
    ['B', 'G', 'R'],
]


# ind 番目以降
def search(ind, chars, indices):
    first = chars[0]
    rests = chars[1:]
    total = 0
    if len(rests) > 0:
        for k in range(ind, n):
            if s[k] == first:
                total += search(k + 1, rests, indices + [k])
    else:
        for k in range(ind, n):
            i, j = indices
            if s[k] == first and j - i != k - j:
                total += 1
            else:
                total += 0

    return total


total = 0
for chars in comibinations:
    total += search(0, chars, [])


print(total)
