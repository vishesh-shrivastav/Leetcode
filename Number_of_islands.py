# Problem number 200
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Algorithm - If cell is 1, do dfs
        # recursively to find adjacent 1s
        # Flip all ones to # for one chain of islands
        # Number of islands = number of such chains flipped
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    # Helper function for performing DFS
    def dfs(self, grid, i, j):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1'):
                return
        # Flip
        grid[i][j] = "#"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
