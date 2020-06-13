def sudoku_checker(board):
    for i in range(len(board)):
        valid_col = set()
        valid_row = set()
        for j in range(len(board)):
            num_col = board[i][j]
            if num_col in valid_col:
                if num_col == 0:
                    continue
                return False
            valid_col.add(num_col)
            
            num_row = board[j][i]
            if num_row in valid_row:
                if num_row == 0:
                    continue
                return False
            valid_row.add(num_row)

    for i in range(0, len(board) - 3, 3):
        valid_square = set()
        for j in range(0, len(board) - 3, 3):
            for k in range(0,2):
                for l in range(0,2):
                    num = board[i+k][j+l]
                    if num in valid_square:
                        if num == 0:
                            continue
                        return False
                    valid_square.add(num)

    return True
