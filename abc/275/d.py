n = int(input())

memo = {}

def f(k):
    global memo
    if k == 0:
        return 1
    if k in memo:
        return memo[k]

    ans = f(k//2) + f(k//3)
    memo[k] = ans
    return ans

print(f(n))
