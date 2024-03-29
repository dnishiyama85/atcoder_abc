# Union-Find
n, q = map(int, input().strip().split())

parents = [i for i in range(n)]


def find(x):
    """
    自分が親であるときは自分の番号を返し、
    それ以外のときはもう一度 find を行うことで親を探すと同時に、
    自分を親に直接つなぎ直す（経路圧縮）。
    戻り値は結局、自分の親の番号である。
    """
    if parents[x] == x:
        return x

    p = parents[x]
    root = find(p)
    # 繋ぎ直し
    parents[x] = root
    return root


def unite(x, y):
    """
    x と y が異なる親を持つとき、同じグループにまとめる。
    ここでは、y の親を x の親につなげる。
    """
    root_of_x = find(x)
    root_of_y = find(y)
    if root_of_y == root_of_x:
        return

    # つなげる。
    parents[root_of_y] = root_of_x


def same(x, y):
    """
    x と y が同じ親を持つ（= 同じグループに属する）かどうかを判定する。
    """
    return find(x) == find(y)


for _ in range(q):
    com, x, y = map(int, input().strip().split())
    if com == 0:  # unite
        unite(x, y)
    else:  # same
        if same(x, y):
            print(1)
        else:
            print(0)
