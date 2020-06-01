n = int(input())
a = list(map(int, input().strip().split()))

students = []

for i in range(n):
    students.append((i + 1, a[i]))

students = sorted(students, key=lambda s: s[1])
ids = [str(s[0]) for s in students]

print(' '.join(ids))
