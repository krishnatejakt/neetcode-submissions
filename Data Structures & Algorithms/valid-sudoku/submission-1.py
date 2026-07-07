import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        board = np.array(board)

        def clean(val):
            empty = []
            for v in val:
                if v!=".":
                    empty.append(v)
            if len(empty)!=len(set(empty)):
                return False
            return True

        for row in board:
            flag = clean(row)
            if flag == False:
                return flag
            
        for i in range(cols):
            flag = clean(board[:, i])
            if flag == False:
                return flag
        
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                result = []
                for k in range(i, i+3):
                    for w in range(j, j+3):
                        result.append(board[k][w])
                flag = clean(result)
                if flag == False:
                    return False
                
        return True
        