a, b, q = list(map(int, input().strip().split()))
s = []
t = []
for i in range(a):
    s.append(int(input()))

for i in range(b):
    t.append(int(input()))

def binsearch_left_index(x, s, l, r):
    min_s = s[0]
    max_s = s[-1]
    if x < min_s:
        return None

    if x > max_s:
        return -1

    if r - l <= 1:
        return l

    if s[l] == x:
        return l;

    c = (l + r) // 2
    if s[c] > x:
        return binsearch_left_index(x, s, l, c)
    else:
        return binsearch_left_index(x, s, c, r)

def binsearch_right_index(x, s, l, r):
    min_s = s[0]
    max_s = s[-1]
    if x < min_s:
        return 0

    if x > max_s:
        return None

    return binsearch_left_index(x, s, l, r) + 1

def search(x):
    l_shrine = binsearch_left_index(x, s, 0, len(s))
    l_temple = binsearch_left_index(x, t, 0, len(t))
    r_shrine = binsearch_right_index(x, s, 0, len(s))
    r_temple = binsearch_right_index(x, t, 0, len(t))
# 左左と行く場合
    if l_shrine is None or l_temple is None:
        ll = 1e20
    else:
        ll = max(abs(s[l_shrine] - x), abs(t[l_temple] - x))

# 左神社右寺と行く場合
    if l_shrine is None or r_temple is None:
        lr1 = 1e20
    else:
        lr1 = abs(s[l_shrine] - x) + abs(t[r_temple] - s[l_shrine])

# 左寺右神社と行く場合
    if l_temple is None or r_shrine is None:
        lr2 = 1e20
    else:
        lr2 = abs(t[l_temple] - x) + abs(s[r_shrine] - l_temple)

# 右神社左寺と行く場合
    if r_shrine is None or l_temple is None:
        rl1 = 1e20
    else:
        rl1 = abs(s[r_shrine] - x) + abs(t[l_temple] - s[r_shrine])

# 右寺左神社と行く場合
    if l_shrine is None or r_temple is None:
        rl2 = 1e20
    else:
        rl2 = abs(t[r_temple] - x) + abs(s[l_shrine] - t[r_temple])

# 右右と行く場合
    if r_shrine is None or r_temple is None:
        rr = 1e20
    else:
        rr = max(abs(s[r_shrine] - x), abs(t[r_temple] - x))


    ans = min(ll, lr1, lr2, rl1, rl2, rr)
    return ans

for i in range(q):
    x = int(input())
    print(search(x))

