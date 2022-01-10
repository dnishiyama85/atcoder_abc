from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
ss = [input().strip() for _ in range(n)]

count = defaultdict(int)
for s in ss:
    count[s] += 1

print('AC x {}'.format(count['AC']))
print('WA x {}'.format(count['WA']))
print('TLE x {}'.format(count['TLE']))
print('RE x {}'.format(count['RE']))
