import numpy as np

n, x = map(int, input().strip().split())
data = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    data.append((a, b))

data = np.array(data)

memo = {}
def dfs(depth, position):
    if (depth, position) in memo:
        return memo[(depth, position)]

    # n回ジャンプしたけど届かなかったとき
    if depth >= n:
        memo[(depth, position)] = False
        return False

    # まだジャンプが残っているとき
    next_a, next_b = data[depth]
    # ちょうどn回目のジャンプで到達？
    if depth == n - 1:
        if position + next_a == x or position + next_b == x:
            memo[(depth, position)] = True
            return True
        else:
            memo[(depth, position)] = False
            return False

    # 枝刈り：途中で越えてしまうとき
    if position + next_a > x and position + next_b > x:
        memo[(depth, position)] = False
        return False

    # 次のジャンプを探索
    ret_a = dfs(depth + 1, position + next_a)
    ret_b = dfs(depth + 1, position + next_b)
    result = ret_a or ret_b
    memo[(depth, position)] = result
    return result


ret = dfs(0, 0)
ans = 'Yes' if ret else 'No'

print(ans)
