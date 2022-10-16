n = int(input())
data = []
for _ in range(n):
    s, t = input().strip().split()
    data.append((s, int(t)))

originals = {}
for i, (s, t) in enumerate(data):
    if s not in originals:
        originals[s] = (t, i)

original_list = originals.values()
sorted_list = sorted(original_list, key=lambda x: (x[0], -x[1]), reverse=True)

print(sorted_list[0][1] + 1)
