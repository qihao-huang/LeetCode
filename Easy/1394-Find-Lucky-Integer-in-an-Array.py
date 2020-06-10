# Runtime: 60 ms, faster than 53.08% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 13.7 MB, less than 92.49% of Python3 online submissions for Find Lucky Integer in an Array.

import collections

class Solution:
    def findLucky(self, arr):
        cnt = collections.Counter(arr)

        return max([k for k, v in cnt.items() if k == v] + [-1])

# arr = [1,2,2,3,3,3]
# arr = [5]
# arr = [2,2,2,3,3]
arr = [2,2,3,4]
ret = Solution().findLucky(arr)

out = str(ret)
print(out)