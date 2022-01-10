t = int(input())
data = [list(map(int, input().strip().split())) for _ in range(t)]

# 辺の長さが m の正方形内に自由に辺の長さがそれぞれ x, y の
# 正方形を置くやり方
def free(m, x, y):
    return (m - x + 1) ** 2 * (m - y + 1) ** 2


for n, a, b in data:
    ans = free(n, a, b) - free(a + b - 1, a, b) * (n - (a + b - 1) + 1) ** 2
    print(ans)
