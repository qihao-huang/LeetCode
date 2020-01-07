# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

# FIXME: 

# Approach 1: Brute Force
# -[ ] Approach 2: HashMap 
# Approach 3: Sorting
# Approach 4: Randomization
# Approach 5: Divide and Conquer
# Approach 6: Boyer-Moore Voting Algorithm

# Runtime: 176 ms, faster than 71.85% of Python3 online submissions for Majority Element.
# Memory Usage: 14.2 MB, less than 97.62% of Python3 online submissions for Majority Element.

class Solution:
    def majorityElement(self, nums):
        import collections
        counts = collections.Counter(nums)

        return max(counts.keys(), key=counts.get)

# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
ret = Solution().majorityElement(nums)
print(ret)