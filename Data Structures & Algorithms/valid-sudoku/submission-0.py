class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for i in range(0,9):
            rowSet = set()
            nums = 0
            for j in range(0,9):
                if board[i][j] != ".":
                    nums += 1
                    rowSet.add(board[i][j])
            if nums != len(rowSet):
                return False

        #col check
        for j in range(0,9):
            colSet = set()
            nums = 0
            for i in range(0,9):
                if board[i][j] != ".":
                    nums += 1
                    colSet.add(board[i][j])
            if nums != len(colSet):
                    return False
        # 3x3 check
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                boxSet = set()
                nums = 0
                for i in range(3):
                    for j in range(3):
                        val = board[boxRow + i][boxCol + j]
                        if val != ".":
                            nums += 1
                            boxSet.add(val)
                if nums != len(boxSet):
                    return False
        return True