h1, h2, h3, w1, w2, w3 = map(int, input().strip().split())

# a b x
# c d y
# u v z
# a, b, c, d を全探索
count = 0

for a in range(1, 30):
    for b in range(1, 30):
        for c in range(1, 30):
            for d in range(1, 30):
                x = h1 - a - b
                y = h2 - c - d
                u = w1 - a - c
                v = w2 - b - d
                z = w3 - x - y
                if x > 0 and y > 0 and u > 0 and v > 0 and z > 0 and u + v + z == h3:
                    count += 1

print(count)
