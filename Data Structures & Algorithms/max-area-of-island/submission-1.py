class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row , col = len(grid), len(grid[0])


        found = set()
        def backtrack(r,c):

            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0 or ((r,c)) in found:
                return 0

            found.add((r,c)) 
            return 1 + backtrack(r + 1, c) + backtrack(r - 1, c) + backtrack(r, c+ 1) + backtrack(r, c- 1)



        island = 0 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and ((r,c)) not in found: 
                    island = max(island, backtrack(r, c))

        return island 
                    
            

        



        



