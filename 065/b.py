n = int(input())
as_ = [int(input()) - 1 for _ in range(n)]

visited = [0] * n

index = 0
num_push = 0
goal = False
while True:
    if visited[index] == 1:
        break

    visited[index] = 1
    if index == 1:
        goal = True
        break

    index = as_[index]
    num_push += 1

if goal:
    print(num_push)
else:
    print(-1)
