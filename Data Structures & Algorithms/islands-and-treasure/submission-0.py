class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #m x n with three possible values (-1, 0, INF) 
        #0 -> treasure chest, INF can be travered, -1 cannot be traversed.
        # nearest treasure chest(min), if not reachable must return INF
        #grid can move up down left or right.

        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()



        def bfs(r,c):
            q = deque([(r,c)])
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[r][c] = True 
            steps = 0 

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    if grid[row][col] == 0:
                        return steps 
                    
                    for dr, dc in directions:
                        nr , nc = row + dr, col + dc 

                        if (0 <= nr < ROWS and 0 <= nc < COLS) and not visit[nr][nc] and grid[nr][nc] != -1:
                            visit[nr][nc] = True 
                            q.append((nr,nc))
                    
                steps += 1
            return INF

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == INF:
                    grid[row][col] = bfs(row, col)

        


                    

        