# https://leetcode-cn.com/problems/number-of-islands/


# DFS
# 将二维网格看成一个无向图，竖直或水平相邻的 1 之间有边相连。
# 为了求出岛屿的数量，我们可以扫描整个二维网格。如果一个位置为 1，则以其为起始节点开始进行深度优先搜索。
# 在深度优先搜索的过程中，每个搜索到的 1 都会被重新标记为 0。
# 最终岛屿的数量就是我们进行深度优先搜索的次数。

# 时间复杂度：O(MN)，其中 M 和 N 分别为行数和列数。

# 空间复杂度：O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 MN。


class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r-1,c), (r+1,c), (r,c-1), (r, c+1)]:
            if 0 <= x < nr and 0 <=y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0

        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands

# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] == "0"
                    neighbors = collections.deque([(r,c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            if 0 <= x < nr and 0 <= y< nc and grid[x][y] == "1":
                                neighbors.append((x,y))
                                grid[x][y] = 0

        return num_islands                      



# 并查集


