x, y, a, b, c = map(int, input().strip().split())
ps = map(int, input().strip().split())
qs = map(int, input().strip().split())
rs = map(int, input().strip().split())

ps = sorted(ps)
qs = sorted(qs)
rs = sorted(rs)

p_sum = sum(ps)
q_sum = sum(qs)

score = 0
while True:
    if x == 0 and y == 0:
        break
    if len(rs) == 0:
        # 無色のりんごは残っていない
        if x > 0:
            p = ps[-1]
            ps.pop(-1)
            score += p
            x -= 1
            p_sum -= p
        if y > 0:
            q = qs[-1]
            qs.pop(-1)
            score += q
            y -= 1
            q_sum -= q

    else:
        if x > 0 and y == 0:
            # 緑は残っていない → 赤か無色を食べる
            p = ps[-1]
            r = rs[-1]
            x -= 1
            if r > p:
                rs.pop(-1)
                score += r
            else:
                ps.pop(-1)
                score += p
                p_sum -= p
        elif y > 0 and x == 0:
            # 赤は残っていない → 緑か無色を食べる
            q = qs[-1]
            r = rs[-1]
            y -= 1
            if r > q:
                rs.pop(-1)
                score += r
            else:
                qs.pop(-1)
                score += q
                q_sum -= q
        elif x > 0 and y > 0:
            # 赤も緑も無色もある。どれを食べるか。
            p = ps[-1]
            q = qs[-1]
            r = rs[-1]
            if r >= p and r >= q:
                # 無色を食べたほうが良い。残りの美味しさをなるべく多く残すほうが良い。
                rs.pop(-1)
                score += r
                if p_sum < q_sum:
                    # 赤にして食べる
                    x -= 1
                else:
                    # 緑にして食べる
                    y -= 1
            elif p > r:
                ps.pop(-1)
                score += p
                x -= 1
                p_sum -= p
            elif q > r:
                qs.pop(-1)
                score += q
                y -= 1
                q_sum -= q

print(score)
