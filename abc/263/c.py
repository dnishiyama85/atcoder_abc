n, m = map(int, input().strip().split())

# 深さ優先探索 (再帰呼び出し)
def dfs(a, s, length):
    if length == n:
        print(' '.join(map(str, s)))
        return

    candidates = range(a + 1, m + 1)
    for b in candidates:
        dfs(b, s + [b], length + 1)

dfs(0, [], 0)
