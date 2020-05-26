q, h, s, d = map(int, input().strip().split())
n = int(input())

sorted_list = sorted([(q, 4), (h, 2), (s, 1), (d, 0.5)],
                     key=lambda t: t[0] * t[1])

cheapest = sorted_list[0]
if cheapest[1] == 0.5:
    # 2リットルが最安の場合
    second = sorted_list[1]
    cost = cheapest[0] * (n // 2) + second[0] * (n % 2) * second[1]
else:
    cost = cheapest[0] * cheapest[1] * n

print(cost)
