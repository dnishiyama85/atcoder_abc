n = int(input())
as_ = list(map(int, input().strip().split()))
q = int(input())
ms = list(map(int, input().strip().split()))

# 可能な数字を全て挙げておく？
possible = set()


def dfs(s, depth):
    if depth == n:
        return

    a = as_[depth]
    possible.add(s)
    possible.add(s + a)

    return dfs(s, depth + 1) or dfs(s + a, depth + 1)


dfs(0, 0)
for m in ms:
    if m in possible:
        print('yes')
    else:
        print('no')
