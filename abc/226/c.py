import sys
sys.setrecursionlimit(220001)

n = int(input())
ti = []
ki = []
aij = []

for _ in range(n):
    row = list(map(int, input().strip().split()))
    ti.append(row[0])
    ki.append(row[1])
    aij.append(row[2:])

# 技 N を習得するための前提技のリストを作る
requirements = set()
requirements.add(n)
seen = set()

def dfs(m):
    if m in seen:
        return
    needed = aij[m - 1]
    for nd in needed:
        requirements.add(nd)
        dfs(nd)
    seen.add(m)

dfs(n)

time = sum([ti[i - 1] for i in requirements])

print(time)
