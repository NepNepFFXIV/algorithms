# Helper function used to time the solution
def time_elapsed(func):
    import time
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished in {(time.perf_counter() - start_time):.5f}s")
        return result
    return wrapper

from collections import Counter, deque
import itertools
import copy
import math

class Sudoku:
    def __init__(self, puzzle):
        if SudokuValidator.is_valid_input(puzzle):
            self.puzzle = Sudoku._parse_puzzle(puzzle)
            self.board = puzzle
            self.solution = puzzle
            self.num_of_solutions = 1 if SudokuValidator.is_valid_solution(puzzle) else 0
        else:
            raise Exception("Invalid Grid")
    
    def solve(self):
        next_x, next_y = Sudoku._next_empty_cell(self.board)
        if next_x == -1:
            return True

        for i in self.puzzle[next_x][next_y]:
            if Sudoku._is_valid_move(self.board, i, next_x, next_y):
                self.board[next_x][next_y] = i
                
                if self.num_of_solutions < 2 and self.solve():
                    self.num_of_solutions += 1
                    self.solution = copy.deepcopy(self.board)
                
                self.board[next_x][next_y] = 0
        return False

    @staticmethod
    def _is_valid_move(board, num, x, y):
        for i in range(9):
            if board[x][i] == num: return False
            if board[i][y] == num: return False
        
        x = (x//3)*3
        y = (y//3)*3
        for i in range(3):
            for j in range(3):
                if board[i+x][j+y] == num:
                    return False
        return True

    @staticmethod
    def _next_empty_cell(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return (-1, -1)

    # Parse the valid puzzle into a 2D list of size 9x9   
    # Each index holds the possible numbers for that index
    @staticmethod
    def _parse_puzzle(puzzle):
        nums_given = 0
        board = []
        for row in puzzle:
            new_row = []
            for cell in row:
                if cell != 0:
                    nums_given += 1
                    new_cell = {cell}
                else:
                    new_cell = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                new_row.append(new_cell)
            board.append(new_row)
        
        # Prune the possible numbers
        board = Sudoku._filter_bad_nums(board)
        news_nums = Sudoku._check(board)
        while news_nums > nums_given:
            nums_given = news_nums
            board = Sudoku._filter_bad_nums(board)
            news_nums = Sudoku._check(board) 
        return board

    @staticmethod
    def _check(board):
        nums = 0
        for row in board:
            for cell in row:
                if len(cell) == 1:
                    nums += 1
        return nums

    # Main function to filter out bad numbers for each unsolved cell
    @staticmethod
    def _filter_bad_nums(board):
        # Rule 1: Using Sudoku definition
        board = Sudoku._filter_rows(board)
        board = Sudoku._filter_columns(board)
        board = Sudoku._filter_regions(board)
        
        # Rule 2: A certain value is allowed in no other cell in the same region
        # Hidden Singles technique for regions
        board = Sudoku._rule_2(board)

        # Rule 3: A certain value is allowed in no other cell in the same row or column
        # Hidden Singles technique for row and col
        board = Sudoku._rule_3(board)

        # Rule 4: A certain value is allowed only on one column or row inside a region, 
        # thus we can eliminate this value from that row or column in the other regions
        board = Sudoku._rule_4(board)

        # Rule 5: Naked Pair https://www.thonky.com/sudoku/naked-pairs-triples-quads
        board = Sudoku._rule_5(board)

        return board

    @staticmethod
    def _rule_2(board):
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                # flatten a region into a list
                temp = [board[i][j] for i in range(row, row+3) for j in range(column, column+3)]
                unique_nums = Sudoku._unique(temp)
                for num in unique_nums:
                    for i in range(9):
                        if num in temp[i]:
                            temp[i] = {num}
                temp = deque(temp)
                for i in range(row, row+3):
                    for j in range(column, column+3):
                        board[i][j] = temp.popleft()
        return board

    @staticmethod
    def _rule_3(board):
        # Column. This will create copy
        board = [list(row) for row in zip(*board)]
        for row in board:
            unique_nums = Sudoku._unique(row)
            for num in unique_nums:
                for i in range(9):
                    if num in row[i]:
                        row[i] = {num}
        board = [list(row) for row in zip(*board)]

        # Row
        for row in board:
            unique_nums = Sudoku._unique(row)
            for num in unique_nums:
                for i in range(9):
                    if num in row[i]:
                        row[i] = {num}
        return board

    @staticmethod
    def _rule_4(board):
        # Might not worth it
        # result = {}        
        # for j in range(0,9,3):
        #     for i in range(0,9,3):
        #         line1 = set.union(*(a for a in board[i][j:j+3] if len(a) > 1))
        #         line2 = set.union(*(a for a in board[i+1][j:j+3] if len(a) > 1))
        #         line3 = set.union(*(a for a in board[i+2][j:j+3] if len(a) > 1))

        #         nums = [line1-line2-line3,
        #                 line2-line1-line3,
        #                 line3-line1-line2]

        #         for row,num in enumerate(nums):
        #             if num:
        #                 for k in num:
        #                     result[k] = row + i
        return board

    @staticmethod
    def _rule_5(board):
        # Check naked pair in columns
        board = [list(row) for row in zip(*board)]
        for row in board:
            Sudoku._naked_pair(2, row)
            # Sudoku._naked_pair(3, row)
            # Sudoku._naked_pair(4, row)
        board = [list(row) for row in zip(*board)]

        # Check naked pair in row
        for row in board:
            Sudoku._naked_pair(2, row)   
            # Sudoku._naked_pair(3, row)
            # Sudoku._naked_pair(4, row)
        
        # Not worth checking regions
        # for row in range(0, 9, 3):
        #     for column in range(0, 9, 3):
        #         # flatten a region into a list
        #         temp = [board[i][j] for i in range(row, row+3) for j in range(column, column+3)]
        #         Sudoku._naked_pair(2, temp)
        #         temp = deque(temp)
        #         for i in range(row, row+3):
        #             for j in range(column, column+3):
        #                 board[i][j] = temp.popleft()
        return board

    # Helper function for rule 5
    # n indicates pairs, triplets, or quads
    @staticmethod
    def _naked_pair(n, row):
        if 2 <= n <= 4:
            c = Counter([tuple(i) for i in row if len(i) == n])
            pair = None
            for k,v in c.items():
                if v > n-1:
                    pair = set(k)
            if pair:
                for i in range(9):
                    if row[i] != pair:
                        row[i] -= pair

    # This function will return a set of unique numbers on a row
    @staticmethod
    def _unique(row):
        result = set() 
        for _ in row: 
            result |= row[0] - set.union(*row[1:]) 
            row = row[-1:] + row[:-1]  # shift the list of sets
        return result
        # c = Counter(itertools.chain.from_iterable(row))
        # return {k for k,v in c.items() if v==1}

    @staticmethod
    def _filter_rows(board):
        return [Sudoku._filter_helper(row) for row in board]

    @staticmethod
    def _filter_columns(board):
        board = [list(row) for row in zip(*board)]
        board = [Sudoku._filter_helper(row) for row in board]
        board = [list(row) for row in zip(*board)]
        return board

    @staticmethod
    def _filter_regions(board):
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                # flatten a region into a list
                temp = [board[i][j] for i in range(row, row+3) for j in range(column, column+3)]
                temp = deque(Sudoku._filter_helper(temp))
                for i in range(row, row+3):
                    for j in range(column, column+3):
                        board[i][j] = temp.popleft()
        return board

    @staticmethod
    def _filter_helper(row):
        not_nums = {i for cell in row for i in cell if len(cell) == 1}
        return [i-not_nums if len(i)!= 1 else i for i in row]


class SudokuValidator:   
    @staticmethod
    def is_valid_input(puzzle):
        if len(puzzle) != 9:
            return False
        
        # Check if each row is valid
        for row in puzzle:
            if not SudokuValidator._valid_line_input(row):
                return False

        # Check if each column is valid
        for col in zip(*puzzle[::-1]):
            if not SudokuValidator._valid_line_input(col):
                return False

        # Check if each region is valid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                line = puzzle[i][j:j+3] + puzzle[i+1][j:j+3] + puzzle[i+2][j:j+3]
                if not SudokuValidator._valid_line_input(line):
                    return False

        return True

    @staticmethod
    def _valid_line_input(line):
        if len(line) != 9:
            return False

        for num in line:
            if not isinstance(num, int): 
                return False # not int

        counter = Counter((i for i in line if i != 0))
        for k,v in counter.items():            
            if k < 1 or k > 9: return False         # not in range 1-9
            if v > 1: return False                  # number appears more than 1
        
        return True

    @staticmethod
    def is_valid_solution(puzzle):
        # Check if each row is valid
        for row in puzzle:
            if not SudokuValidator._valid_line_solution(row):
                return False

        # Check if each column is valid
        for col in zip(*puzzle[::-1]):
            if not SudokuValidator._valid_line_solution(col):
                return False

        # Check if each region is valid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                line = puzzle[i][j:j+3] + puzzle[i+1][j:j+3] + puzzle[i+2][j:j+3]
                if not SudokuValidator._valid_line_solution(line):
                    return False

        return True

    @staticmethod
    def _valid_line_solution(line):
        return set([str(i) for i in line]) == set("123456789")


@time_elapsed
def sudoku_solver(puzzle):
    game = Sudoku(puzzle)
    game.solve()
    if game.num_of_solutions == 0:
        raise Exception("No Solution")
    if game.num_of_solutions == 2:
        raise Exception("Multiple Solutions")
    return game.solution

# Print out a 9x9 board in a viewable way
def print_board(board):
    for i in range(9):
        if i % 3 == 0:
            print("-------------------------")
        print("| ", end = "")
        for j in range(9):
            if j % 3 == 2:
                print(board[i][j], end = " | ")
            else:
                print(board[i][j], end = " ")
        print()
    print("-------------------------")        


if __name__=="__main__":
    sample_puzzle_0 = [         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # 27 given
    sample_puzzle_easy = [      [0, 0, 6, 1, 0, 0, 0, 0, 8], 
                                [0, 8, 0, 0, 9, 0, 0, 3, 0], 
                                [2, 0, 0, 0, 0, 5, 4, 0, 0], 
                                [4, 0, 0, 0, 0, 1, 8, 0, 0], 
                                [0, 3, 0, 0, 7, 0, 0, 4, 0], 
                                [0, 0, 7, 9, 0, 0, 0, 0, 3], 
                                [0, 0, 8, 4, 0, 0, 0, 0, 6], 
                                [0, 2, 0, 0, 5, 0, 0, 8, 0], 
                                [1, 0, 0, 0, 0, 2, 5, 0, 0]]

    # 23 given
    sample_puzzle_medium = [    [8, 0, 0, 4, 0, 6, 0, 0, 3],
                                [0, 0, 9, 0, 0, 0, 0, 2, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                                [0, 0, 0, 8, 0, 0, 4, 0, 0],
                                [0, 6, 0, 0, 0, 0, 0, 1, 0],
                                [0, 0, 3, 0, 0, 2, 0, 0, 9],
                                [7, 0, 2, 0, 3, 0, 0, 0, 0],
                                [0, 4, 0, 0, 0, 0, 5, 0, 0],
                                [5, 0, 0, 7, 0, 9, 0, 0, 8]]

    # 21 given
    sample_puzzle_hard = [      [8, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 3, 6, 0, 0, 0, 0, 0], 
                                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                                [0, 5, 0, 0, 0, 7, 0, 0, 0], 
                                [0, 0, 0, 0, 4, 5, 7, 0, 0], 
                                [0, 0, 0, 1, 0, 0, 0, 3, 0], 
                                [0, 0, 1, 0, 0, 0, 0, 6, 8], 
                                [0, 0, 8, 5, 0, 0, 0, 1, 0], 
                                [0, 9, 0, 0, 0, 0, 4, 0, 0]] 

    solution = sudoku_solver(sample_puzzle_medium)
    print_board(solution)