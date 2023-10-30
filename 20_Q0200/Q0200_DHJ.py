class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs (row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return
            # 현재 방문한 땅을 0으로
            grid[row][col] = '0'
            
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    num_islands += 1
                    dfs(row, col)
        
        return num_islands