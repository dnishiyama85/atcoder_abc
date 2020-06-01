s = input().strip()
s = s[:-2]


def is_even_string(string):
    l = len(string)
    first = string[:l//2]
    last = string[l//2:]
    return first == last


while not is_even_string(s):
    s = s[:-2]

print(len(s))
