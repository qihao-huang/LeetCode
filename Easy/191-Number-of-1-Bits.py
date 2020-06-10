# Write a function that takes an unsigned integer and 
# return the number of '1' bits it has (also known as the Hamming weight).

# Runtime: 32 ms, faster than 37.41% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            last = n & 1
            if last == 1:
                ans += 1
            n >>= 1
        return ans

# n = "00000000000000000000000000001011"
# n = "00000000000000000000000000001011" # 3
# n = "00000000000000000000000010000000" # 1
n = 11111111111111111111111111111101 # 31
ret = Solution().hammingWeight(n)
print(ret)