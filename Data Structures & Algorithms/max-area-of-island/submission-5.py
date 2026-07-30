class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        island = 0 
        seen = set()


        def numIsland(r,c):
            if r >= ROW or r < 0 or c >= COL or c < 0 or (r,c) in seen or grid[r][c] == 0:
                return 0 

            seen.add((r,c))

            return 1 + numIsland(r + 1, c) + numIsland(r - 1, c) + numIsland(r, c - 1) + numIsland(r, c + 1)




        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    val = numIsland(r,c)
                    island = max(island, val)
                
        
        return island 
