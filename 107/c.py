n, k = map(int, input().strip().split())
xs = list(map(int, input().strip().split()))


def min_for_interval(left, right):
    if left < 0:
        if right < 0:
            return abs(left)
        else:
            l_r = 2 * abs(left) + abs(right)
            r_l = 2 * abs(right) + abs(left)
            return min(l_r, r_l)
    else:
        return right


min_time = 1e9
for i in range(0, n - k + 1):
    left = xs[i]
    right = xs[i + k - 1]
    min_time = min(min_for_interval(left, right), min_time)

print(min_time)
