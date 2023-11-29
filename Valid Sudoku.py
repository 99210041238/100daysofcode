class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            column = []
            box = []

            for j in range(9):
                # Check each row
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])

                # Check each column
                if board[j][i] != ".":
                    if board[j][i] in column:
                        return False
                    column.append(board[j][i])

                # Check each 3x3 box
                box_row, box_col = 3 * (i // 3), 3 * (i % 3)
                if board[box_row + j // 3][box_col + j % 3] != ".":
                    if board[box_row + j // 3][box_col + j % 3] in box:
                        return False
                    box.append(board[box_row + j // 3][box_col + j % 3])

        return True