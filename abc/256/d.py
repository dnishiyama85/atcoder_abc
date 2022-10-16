from typing import List
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    l, r = map(int, input().strip().split())
    data.append([l, r])

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

solution = Solution()
sol = solution.merge(data)

for l, r in sol:
    print(f"{l} {r}")

