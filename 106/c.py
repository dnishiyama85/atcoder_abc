s = input().strip()
k = int(input())

found = False
# 最初の1でない数字がどこに現れるか
for i in range(len(s)):
    if s[i] != '1':
        found = True
        break

if found:
    if k <= i:
        print(1)
    else:
        print(s[i])
else:
    print(s[0])
