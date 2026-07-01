class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])
        visited = set()
        numIsland = 0

        def isIsland(r,c):
            if r < 0 or c < 0 or  r >= row or c >= col or (r,c) in visited or grid[r][c] == "0": 
                return 

            visited.add((r,c))
            isIsland(r + 1, c)
            isIsland(r - 1, c)
            isIsland(r, c + 1)
            isIsland(r, c - 1)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    isIsland(r, c)
                    numIsland += 1
                
        return numIsland 

