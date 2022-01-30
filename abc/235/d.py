a, n = map(int, input().strip().split())

# 幅優先探索をしてみる
queue = [(n, 0)]
visited = set()
visited.add(n)
ans = -1

while len(queue) > 0:
    v, d = queue.pop(0)
    if v % a == 0:
        next_v1 = v // a
        if next_v1 == 1:
            ans = d + 1
            break
        elif next_v1 not in visited:
            visited.add(next_v1)
            queue.append((next_v1, d + 1))
    if v >= 10:
        str_v = list(str(v))
        if str_v[1] != '0':
            next_v2_str = ''.join(str_v[1:]) + str_v[0]
            next_v2 = int(next_v2_str)
            if next_v2 == 1:
                ans = d + 1
                break
            elif next_v2 not in visited:
                visited.add(next_v2)
                queue.append((next_v2, d + 1))

print(ans)
