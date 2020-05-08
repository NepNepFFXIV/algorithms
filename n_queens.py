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

import random
import itertools
import copy

# Algorithm: https://pdfs.semanticscholar.org/79d2/fa13d4a5cfc02ff6936b6083bb620e4e0ce1.pdf
# Usable but not fully optimized
class Queens:
    def __init__(self, n=8):
        '''A solution is stored in a list. Each index represents a row.
        Each item represents the col index that has a queen.
        For example, solution[3] = 2 means that there is a queen at (row 3, col 2)
        '''
        self.n = n
        self.queen = [i for i in range(n)]
        # self.queen = [2, 1, 3, 0]        
        random.shuffle(self.queen)
        self.collisions = self._compute_collisions()

    def solve(self):
        while self.collisions != 0:
            for i in range(self.n):
                for j in range(self.n):
                    if self._swap_okay(i, j):
                        if self.collisions == 0:
                            return
            random.shuffle(self.queen)
            self.collisions = self._compute_collisions()
                        
        
    # A square in row i and column j is 
    # on a negative slope diagonal line 'dn' with index i + j and 
    # on a positive slope diagonal line 'dp' with index i - j
    def _compute_collisions(self):
        self.dn = [0 for _ in range(self.n*self.n)]
        self.dp = [0 for _ in range(self.n*self.n)]

        for i,j in enumerate(self.queen):
            self.dn[i+j] += 1
            self.dp[i-j] += 1

        return sum(i-1 for i in self.dn + self.dp if i != 0)

    def _compute_attacks(self):
        self.attack = set()
        for x in range(self.n):
            for col in range(x+1,self.n):
                if abs(x-col) == abs(self.queen[x] - self.queen[col]):
                    self.attack.add(x)
                    self.attack.add(col)
        return len(self.attack)

    # Check if swapping queens at col x and y will reduce collisions
    def _swap_okay(self, x, y):
        before = copy.deepcopy(self.collisions)        
        self._perform_swap(x, y)
        if self.collisions > before:
            self._perform_swap(x, y)
            return False
        return True

    def _perform_swap(self, i, j):
        self.queen[i], self.queen[j] = self.queen[j], self.queen[i]
        self.collisions = self._compute_collisions()

class QueensBackTrack:
    def __init__(self, n=8, count_solutions=False):
        self.n = n
        self.board = [False for _ in range(n*n)]        
        self.dn = [False for _ in range(n*n)]   # A cell (i, j) is on the negative diagonal with index i+j
        self.dp = [False for _ in range(n*n)]   # A cell (i, j) is on the negative diagonal with index i-j
        self.next_row = [i for i in range(n)]
        self.solutions = []
        self.num_solutions = 0
        self.count_solutions = count_solutions

    def solve(self): 
        self._backtrack()
        return self.solutions[0]

    def _backtrack(self):
        next_row = self._next_row()
        if next_row == -1:
            return True

        for next_col in range(self.n):
            if self._is_safe(next_row, next_col):
                self._place_queen(next_row, next_col)
                if self._backtrack():
                    if self.count_solutions:
                        self.solutions.append(self._convert(self.board))
                        self.num_solutions += 1
                    else:
                        self.solutions.append(self._convert(self.board))
                        return True
                self._unplace_queen(next_row, next_col)
        return False

    def _next_row(self):
        if self.next_row:
            return self.next_row[-1]
        return -1

    # Place a queen at (x, y)
    def _place_queen(self, x, y):
        self.board[x*self.n + y] = True
        self.dn[x+y] = True
        self.dp[x-y] = True
        self.next_row.remove(x)

    def _unplace_queen(self, x, y):
        self.board[x*self.n + y] = False
        self.dn[x+y] = False
        self.dp[x-y] = False
        self.next_row.append(x)

    def _is_safe(self, x, y):
        # Check if row is safe
        if set(self.board[x*self.n : x*self.n+self.n]) != {0}:
            return False

        # Check if column is safe:
        for i in range(y%self.n, self.n*self.n, self.n):
            if self.board[i] == True:
                return False
        
        # Check if negative diagonal is safe
        if self.dn[x+y] == True:
            return False

        # Check if possible diagonal is safe
        if self.dp[x-y] == True:
            return False

        return True

    def _convert(self, board):
        # Converting the board into more compact form
        # Board: [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]
        # Solution: [0, 2, 1, 3] means there is a queen at (0,0), (1,2), (2,1), and (3, 3)
        solution = [None for _ in range(self.n)]
        for i in range(self.n):
            solution[i] = board[i*self.n : i*self.n+self.n].index(True)
        return solution

def print_board(board):
    size = len(board)
    print(' ---' * size)
    for i in range(size):
        print("|", end="")
        for j in range(size):
            print(" Q |" if board[i] == j else "   |", end="")
        print()
        print(' ---' * size) 

def is_valid_solution(solution):      
    # Checking to see if any column has more than 1 queen
    if len(solution) != len(set(solution)):
        return False

    # Checking the diagonals
    # Algorithm: A queen at (x, y) is on the same diagonal as queen at (u, v)
    # when abs(x - u) == abs(y - v)
    for x in range(len(solution)):
        for col in range(x+1, len(solution)):
            if abs(x-col) == abs(solution[x] - solution[col]):
                return False
    return True

@time_elapsed
def n_queen(n=8, count_solutions=False):
    if n == 1: return [0]
    if n <= 3: return []

    game = QueensBackTrack(n, count_solutions)
    return game.solve()

    # game = Queens(n)
    # game.solve()
    # return game.queen

#https://en.wikipedia.org/wiki/Eight_queens_puzzle#Existence_of_solutions
@time_elapsed
def nQueen(n):
    if n == 1: return [0]
    if n <= 3: return []

    evens = [i for i in range(2, n+1, 2)]
    odds = [i for i in range(1, n+1, 2)]

    if n % 6 == 3:
        evens.remove(2)
        evens.append(2)
        odds.remove(1)
        odds.remove(3)
        odds.append(1)
        odds.append(3)
    elif n % 6 == 2:
        odds[0], odds[1] = 3, 1
        odds.remove(5)
        odds.append(5)

    return [a-1 for a in evens + odds]

if __name__=="__main__":
    nQueen(1000000)
    print_board(n_queen(10))