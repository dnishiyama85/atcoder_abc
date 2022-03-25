n = int(input())
as_ = list(map(int, input().strip().split()))

num_balls = 0
stack = []

for i, a in enumerate(as_):
    num_balls += 1
    if len(stack) == 0:
        stack.append([a, 1])
    else:
        # いま入れた玉で最上段が消えるかどうかを見る
        last_a, last_count = stack[-1]
        if a == last_a:
            # 前と同じ玉が入った
            if last_count + 1 == a:
                # 消える
                num_balls -= a
                stack.pop()
            else:
                # 個数が足りないので残る
                stack[-1][1] += 1
        else:
            # 前とは違う玉が入った
            stack.append([a, 1])

    print(num_balls)
