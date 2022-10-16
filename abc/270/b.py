x, y, z = map(int, input().strip().split())

def solve(x, y, z):
    if x < 0:
        if x < y < 0:
            # 壁が途中にある
            if z < y:
                # ハンマーを拾えない
                return -1
            else:
                if z < 0:
                    # ついでにハンマーを拾える
                    return abs(x)
                else:
                    # 拾いに戻る必要あり
                    return abs(z) + abs(z - x)
        else:
            # 壁は途中にない
            return abs(x)
    else:
        if 0 < y < x:
            # 壁が途中にある
            if y < z:
                return -1
            else:
                if 0 < z:
                    return abs(x)
                else:
                    return abs(z) + abs(z - x)
        else:
            # 壁は途中にない
            return abs(x)

print(solve(x, y, z))
