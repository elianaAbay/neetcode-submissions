class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()


        def backtrack(r,c,i):
            if i == len(word):
                return True 
            if r < 0 or c < 0 or r > row - 1 or c > col - 1 or (r,c) in visited or board[r][c] != word[i]:
                return False 

            visited.add((r,c))

            res = (backtrack(r + 1,c,i + 1) or backtrack(r -1,c,i + 1) or backtrack(r,c - 1,i + 1) or backtrack(r,c + 1,i + 1))
            visited.remove((r,c))
            
            return res

        for r in range(row):
            for c in range(col):
                if backtrack(r,c,0):
                    return True
        
        return False