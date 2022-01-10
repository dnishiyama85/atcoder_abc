n = int(input())
edges = [list(map(int, input().strip().split())) for _ in range(n - 1)]
a = [e[0] - 1 for e in edges]
b = [e[1] - 1 for e in edges]
q = int(input())
queries = [list(map(int, input().strip().split())) for _ in range(q)]

# 出発点の頂点はどれか？ → b に登場しないやつ
a_check = [0] * n
b_check = [0] * n
for _a, _b in zip(a, b):
    a_check[_a] = 1
    b_check[_b] = 1

start = -1
print("b_check =", b_check)
for i in range(n):
    if b_check[i] == 0:
        start = i

# 木を構成する。
# 次の頂点がどこかのリスト
next_vertex = [-1] * n
for _a, _b in zip(a, b):
    next_vertex[_a] = _b

print("start =", start)
print("next_vertex = ", next_vertex)
# 木のn番目の頂点のIDがなにかを引くリスト
v_to_id = [0] * n
id_to_v = [0] * n
id = start
for i in range(n):
    v_to_id[i] = id
    id_to_v[id] = i
    if i < n - 1:
        id = next_vertex[id]

imos_data = [0] * n
# クエリを処理する
print(id_to_v)
for t, e, x in queries:
    e = e - 1
    if t == 1:
        base_id = a[e]
        boundary_id = b[e]
    else:
        base_id = b[e]
        boundary_id = a[e]

    base_v = id_to_v[base_id]
    boundary_v = id_to_v[boundary_id]
    if base_v < boundary_v:
        left = base_v
        right = boundary_v
    else:
        left = boundary_v
        right = base_v

    print("left = ", left, ", right =", right, ", x =",  x)
    imos_data[left] += x
    imos_data[right] -= x


results = [0] * n
now = 0
print(imos_data)
for i in range(n):
    now += imos_data[i]
    results[i] = now

c = [0] * n
for i in range(n):
    c[v_to_id[i]] = results[i]

for i in range(n):
    print(c[i])
