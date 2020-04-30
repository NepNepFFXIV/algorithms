def time_elapsed(func):
    import time
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} finished in {(end_time - start_time):.5f}s")
        return result
    return wrapper

class Queens:
    def __init__(self, n=8):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def backtrack(self):
        next_row = self._next_empty_row()
        if next_row == -1:
            return True

        for next_col in range(self.n):
            if self._is_safe(next_row, next_col):
                self.board[next_row][next_col] = 1

                if self.backtrack():
                    return True

                self.board[next_row][next_col] = 0
        return False

    def solve(self, func=backtrack):
        func(self)        

    def place_queen(self, x, y):
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            raise Exception("Location is not on board")

        if self._is_safe(x, y):
            self.board[x][y] = 1
            return True
        return False

    def _next_empty_row(self):
        for i,row in enumerate(self.board):
            if 1 not in row:
                return i
        return -1

    def _is_safe(self, x, y):
        return (self._col_safe(x, y)
            and self._diag_1_safe(x, y)
            and self._diag_2_safe(x, y))

    def _col_safe(self, x, y):
        for i in range(self.n):
            if self.board[i][y] == 1:
                return False
        return True

    # Check the diagonal from Top Right to Bottom Left
    def _diag_1_safe(self, x, y):
        for i, j in zip(range(x, self.n), range(y, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(x, -1, -1), range(y, self.n)):
            if self.board[i][j] == 1:
                return False
        return True
    
    # Check the diagonal from Top Left to Bottom Right
    def _diag_2_safe(self, x, y):
        for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(x, self.n), range(y, self.n)):
            if self.board[i][j] == 1:
                return False
        return True

def print_board(board):
    size = len(board)
    print(' ---' * size)
    for row in board:
        print("|", end="")
        for cell in row:
            print(" Q |" if cell else "   |", end="")         
        print()
        print(' ---' * size) 

@time_elapsed
def n_queen(n=8):
    game = Queens(n)
    game.solve()
    print_board(game.board)

if __name__=="__main__":
    n_queen(15)