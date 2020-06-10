# Runtime: 484 ms, faster than 39.80% of Python3 online submissions for Fair Candy Swap.
# Memory Usage: 16 MB, less than 51.75% of Python3 online submissions for Fair Candy Swap.

class Solution:
    def fairCandySwap(self, A, B):
        sum_A = sum(A)
        sum_B = sum(B)
        set_B = set(B)

        average = (sum(A) + sum(B))/2

        for a in A:
            b = average - (sum_A-a)
            if b in set_B:
                return [a,b]

A = [1,1]
B = [2,2]
# Output: [1,2]

# A = [1,2]
# B = [2,3]
# Output: [1,2]

# A = [2]
# B = [1,3]
# Output: [2,3]

# A = [1,2,5]
# B = [2,4]
# Output: [5,4]

ret = Solution().fairCandySwap(A, B)
print(ret)