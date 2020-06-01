n, m = map(int, input().strip().split())

if m // 2 < n:
    # S が余っている
    ans = m // 2
else:
    # c が余っている
    ans = n
    # 余った c は 4つずつで Scc にできる
    ans += (m - 2 * n) // 4

print(ans)
