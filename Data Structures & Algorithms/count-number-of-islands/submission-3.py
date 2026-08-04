class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        island = 0 
        

        def backtrack(r,c):
            if r < 0 or c < 0 or c >= COL or r >= ROW or (r,c) in visited or grid[r][c] == "0":
                return 
            
            visited.add((r,c))
            backtrack(r + 1, c)
            backtrack(r -1, c)
            backtrack(r, c + 1)
            backtrack(r, c - 1)


        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] ==  '1' and (row,col) not in visited:
                    backtrack(row,col)
                    island += 1
                    
                    
                
        return island