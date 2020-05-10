s = input().strip()
list_s = list(s)


def judge(s):
    if s[0] != 'A':
        return False
    list_s[0] = 'a'
    count = 0
    for idx, c in enumerate(s):
        if 2 <= idx and idx <= len(s) - 2 and c == 'C':
            count += 1
            list_s[idx] = 'c'

    if count != 1:
        return False

    return ''.join(list_s) == s.lower()


if judge(s):
    print('AC')
else:
    print('WA')
