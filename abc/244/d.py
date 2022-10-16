ss = input().strip()
ts = input().strip()

parity = {
    'R G B': 1,
    'G R B': -1,
    'G B R': 1,
    'R B G': -1,
    'B R G': 1,
    'B G R': -1,
}

p1 = parity[ss]
p2 = parity[ts]

if p1 == p2:
    print('Yes')
else:
    print('No')
