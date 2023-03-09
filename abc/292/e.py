n, m = map(int, input().strip().split())
children = [set() for _ in range(n)]
parents = [set() for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().strip().split())
    u -= 1
    v -= 1
    children[u].add(v)
    parents[v].add(u)

count = 0

def search(k):
    global count
    checked = set([k])
    stack = [k]
    while len(stack) > 0:
        k2 = stack.pop()
        for c in children[k2]:
            if k not in parents[c]:
                count += 1
            if c not in checked:
                checked.add(c)
                stack.append(c)


for k in range(n):
    search(k)


print(count)

