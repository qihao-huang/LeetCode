
# Runtime: 24 ms, faster than 94.40% of Python3 online submissions for Plus One.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Plus One.

class Solution:
    def plusOne(self, digits):
        sum_all = 0
        for dg in digits:
            sum_all = sum_all*10 + dg

        # print(sum_all)
        sum_out = sum_all+1
        tmp = list(str(sum_out))
        return [int(x) for x in tmp]

# digits = [1,2,3] # [1,2,4]
digits = [4,3,2,1] # [4,3,2,2]
ret = Solution().plusOne(digits)
print(ret)