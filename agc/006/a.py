n = int(input())
s = input()
t = input()

if s == t:
    print(len(s))
    exit(0)

ind = 0
mx = min(len(s), len(t))
mx_len = 0
while ind < mx:
    pre_i = s[-(ind + 1):]
    suf_i = t[:(ind + 1)]
    if pre_i == suf_i:
        mx_len = ind + 1

    ind += 1

ans = len(s) + len(t) - mx_len
print(ans)
