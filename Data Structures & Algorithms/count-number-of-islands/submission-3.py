class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, cols = len(grid), len(grid[0])
        seen = set()


        def island(r,c):
            if r >= row or c >= cols or r < 0 or c < 0 or (r,c) in seen or grid[r][c] == "0":
                return 
            
            seen.add((r,c))

            island(r+1, c)
            island(r-1, c)
            island(r, c-1)
            island(r, c + 1)


        n = 0   
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    island(r,c)
                    n += 1

        
        return n
        
        