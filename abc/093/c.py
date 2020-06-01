sorted_list = list(map(int, input().strip().split()))

count = 0
while True:
    sorted_list = sorted(sorted_list, reverse=True)
    if sorted_list[0] == sorted_list[1] and sorted_list[1] == sorted_list[2]:
        break

    count += 1
    if sorted_list[0] > sorted_list[1]:
        sorted_list[1] += 1
        sorted_list[2] += 1
    else:
        sorted_list[2] += 2


print(count)
