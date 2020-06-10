# The count-and-say sequence is the 
# sequence of integers with the first five terms as following:

# 1.  1
# 2.  11
# 3.  21
# 4.  1211
# 5.  111221

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Input: 4
# Output: "1211"
# Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1",
# "2" can be read as "12" which means frequency = 1 and value = 2, 
# the same way "1" is read as "11", 
# so the answer is the concatenation of "12" and "11" which is "1211".

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
# You can do so recursively, in other words from the previous member read off the digits, 
# counting the number of digits in groups of the same digit.

# Runtime: 28 ms, faster than 91.69% of Python3 online submissions for Count and Say.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Count and Say.

class Solution:
    def countAndSay(self, n: int) -> str:
        # recursively
        res = ""
        if n==1:
            return "1"

        lastN = self.countAndSay(n-1)

        k = 0
        while True:
            i = k
            if i > len(lastN)-1:
                break
            val = lastN[k]
            while True:
                i += 1
                if i > len(lastN)-1:
                    break
                if lastN[i] != val:
                    break
            diff = i-k
            k = i
            res = res + str(diff) + str(val)

        return res
        
n = 10
# n = 1
ret = Solution().countAndSay(n)
print(ret)

#  1.  1
#  2.  11
#  3.  21
#  4.  1211
#  5.  111221 
#  6.  312211
#  7.  13112221
#  8.  1113213211
#  9.  31131211131221
# 10.  13211311123113112211