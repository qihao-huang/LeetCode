# Runtime: 28 ms, faster than 76.22% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
# Memory Usage: 13.8 MB, less than 64.41% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.

import math 

class Solution:
    def pathInZigZagTree(self, label):
        label_path = []
        n = label
        while n != 1:
            label_path.append(n)
            level = math.floor(math.log2(n))
            
            if level % 2 == 0:
                n = (2 ** level - 1) - (n // 2 - 2 ** (level - 1))
            else:
                n = 2 ** level + (2 ** (level + 1) - 1 - n)
                n = n // 2 
        
        label_path.append(1)

        return label_path[::-1]

label = 14
ret = Solution().pathInZigZagTree(label)
print(ret)
