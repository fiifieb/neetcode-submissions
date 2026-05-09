class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [0, 3, 6]
        def traverse_boxes(row, col):
            sett = set()
            for x in range(row, row + 3):
                for y in range(col, col + 3):
                    if board[x][y] != '.':
                        if board[x][y] in sett:
                            return False 
                        sett.add(board[x][y])
            return True
        
        def traverse_row(row):
            sett = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in sett:
                        return False 
                    sett.add(board[row][col])
            return True

        def traverse_col(col):
            sett = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in sett:
                        return False 
                    sett.add(board[row][col])
            return True

        ans = True
        for row in boxes:
            for col in boxes:
                ans = ans and traverse_boxes(row, col)
        for i in range(9):
            ans = ans and traverse_row(i)
            ans = ans and traverse_col(i)

        return ans

            
