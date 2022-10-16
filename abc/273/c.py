n = int(input())
as_ = list(map(int, input().strip().split()))

sorted_as = sorted(list(set(as_)))
all_kind = len(sorted_as)

number_of_kind = [0] * n

index_map = {}

for i, a in enumerate(sorted_as):
    index_map[a] = i

for a in as_:
    ind_a = index_map[a]
    kind = all_kind - (ind_a + 1)
    number_of_kind[kind] += 1

for m in number_of_kind:
    print(m)


