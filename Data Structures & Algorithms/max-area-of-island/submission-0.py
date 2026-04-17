class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()

        def backtrack(r, c):
            # Boundary and base case
            if (
                r < 0 or r >= row or
                c < 0 or c >= col or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))

            # Explore all four directions
            return (
                1 +
                backtrack(r + 1, c) +
                backtrack(r - 1, c) +
                backtrack(r, c + 1) +
                backtrack(r, c - 1)
            )

        island = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    island = max(island, backtrack(r, c))

        return island
