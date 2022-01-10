X, K, D = map(int, input().strip().split())

init_distance = abs(X)
max_travel = K * D
if max_travel < init_distance:
    ans = init_distance - max_travel
else:
    num_travel = (init_distance + D - 1) // D
    nearest = abs(init_distance - num_travel * D)
    rest = K - num_travel
    if rest % 2 == 0:
        ans = nearest
    else:
        ans = abs(nearest - D)

print(ans)
