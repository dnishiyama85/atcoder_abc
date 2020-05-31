n = int(input())
as_ = list(map(int, input().strip().split()))

partition = 1
trend = None
ind = 0
import pdb; pdb.set_trace()
while ind < n:
    if trend is None:
        ind += 1
        prev = as_[ind - 1]
        cur = as_[ind]
        if prev >= cur:
            trend = 'Dec'
        else:
            trend = 'Inc'
    else:
        prev = as_[ind - 1]
        cur = as_[ind]
        if trend == 'Dec':
            if prev < cur:
                trend = None
                partition += 1
        else:
            if prev > cur:
                trend = None
                partition += 1
        ind += 1

print(partition)
