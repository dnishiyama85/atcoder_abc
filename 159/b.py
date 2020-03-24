s = input().strip()


def is_palindrome(string):
    return string == string[::-1]


def is_strong_palindrome(string):
    if not is_palindrome(string):
        return False
    n = len(string)
    if not is_palindrome(string[:(n - 1)//2]):
        return False
    if not is_palindrome(string[(n+3)//2 - 1:]):
        return False
    return True


if is_strong_palindrome(s):
    print('Yes')
else:
    print('No')
