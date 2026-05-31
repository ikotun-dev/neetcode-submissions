class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c //3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True


                    

        # for i in board:
        #     seen = {}
        #     for j in board[i]:
        #         if j not in seen:
        #             seen[j] = 1 
        #         else:
        #             #Early return if the number is in that same line
        #             return False
                
            
                

        