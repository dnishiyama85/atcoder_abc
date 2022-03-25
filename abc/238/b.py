n = int(input())
As = list(map(int, input().strip().split()))

now = 0
cuts = [0]

for a in As:
    cut = (now + (360 - a)) % 360
    now = cut
    cuts.append(cut)

cuts = sorted(cuts)
angles = []
for i in range(len(cuts) - 1):
    angle = cuts[i + 1] - cuts[i]
    angles.append(angle)

angles.append(360 - cuts[-1])
max_angle = max(angles)
print(max_angle)
