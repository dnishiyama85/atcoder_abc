n, k = map(int, input().strip().split())
data = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    data.append((a, b))

data = sorted(data)

money = k
position = 0
for a, b in data:
    cost_to_next = a - position
    if cost_to_next > money:
        # 次の村にたどり着けない。
        break
    else:
        position = a
        money -= cost_to_next
        money += b

# 最後に金の続く限り進む。
position += money

print(position)
