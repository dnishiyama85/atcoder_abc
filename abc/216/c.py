n = int(input())
bs = list(bin(n)[2:])
ops = []
for b in bs:
    if b == '1':
        ops.append('A')

    ops.append('B')

ops = ops[:-1]  # 最後のBを削除

ans = ''.join(ops)
print(ans)
