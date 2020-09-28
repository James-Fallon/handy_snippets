
def mine_sweeper(bombs, num_rows, num_columns):

    board = [[0 for _ in range(num_columns)] for __ in range(num_rows)]

    for bomb in bombs:
        (bomb_row, bomb_column) = bomb
        board[bomb_row][bomb_column] = -1

        for i in range(bomb_row - 1, bomb_row + 2):
            for j in range(bomb_column -1, bomb_column + 2):
                if 0 <= i < num_rows and 0 <= j < num_columns and board[i][j] != -1:
                    board[i][j] += 1

    return board


def pretty(table):
    for row in table:
        print(" | ".join([str(k) if k != -1 else 'B' for k in row]))


if __name__ == '__main__':
    bombs_ahoy = [(0, 0), (1, 1), (1, 3), (3, 3)]

    pretty(mine_sweeper(bombs_ahoy, 4, 5))
    '''
    9 | 2 | 2 | 1 | 1
    2 | 9 | 2 | 9 | 1
    1 | 1 | 3 | 2 | 2
    0 | 0 | 1 | 9 | 1
    '''