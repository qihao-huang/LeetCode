# Runtime: 816 ms, faster than 30.26% of Python3 online submissions for Two Sum.
# Memory Usage: 13.8 MB, less than 75.81% of Python3 online submissions for Two Sum.

import json

class Solution:
    def twoSum(self, nums, target):
        for i, i_value in enumerate(nums):
            j_value = target-i_value
            if  j_value in nums:
                j = nums.index(j_value)
                if i!=j:
                    return [i,j]

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

# input
# [2, 7, 11, 15]
# 9
# output
# [0,1]
