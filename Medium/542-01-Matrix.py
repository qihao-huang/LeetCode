# BFS / DFS / DP 

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # matrix        

        ret = []

        return ret



input = [[0,0,0],[0,1,0],[0,0,0]]

# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# --------------------
# input = [[0,0,0], [0,1,0], [1,1,1]]

# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]

ret = Solution().updateMatrix(input)
print(ret)