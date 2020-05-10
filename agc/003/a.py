s = input().strip()

counts = {
    'N': 0, 'W': 0, 'S': 0, 'E': 0
}

for c in s:
    counts[c] += 1


def judge():
    if counts['N'] > 0 or counts['S'] > 0:
        if counts['N'] * counts['S'] == 0:
            return False

    if counts['W'] > 0 or counts['E'] > 0:
        if counts['W'] * counts['E'] == 0:
            return False

    return True


if judge():
    print('Yes')
else:
    print('No')
