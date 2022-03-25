import numpy as np

n = int(input())

if n * np.log(2) > 2 * np.log(n):
    print('Yes')
else:
    print('No')

