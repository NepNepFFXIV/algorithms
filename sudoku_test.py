import unittest
from sudoku import SudokuValidator, Sudoku

class SudokuValidatorTest(unittest.TestCase):
    def setUp(self):
        self.line01 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.line02 = [3, 4, 6, 1, 2, 7, 9, 5, 8]
        self.line03 = [0, 0, 0, 0, 0, 0, 0, 0, 0]        
        self.line04 = [1, 0, 0, 0, 0, 0, 0, 0, 1]
        self.line05 = [0, "a", 1, 0, 0, 0, 0, 0, 0]
        self.line06 = [0, 2, 0, 0, 11, 0, 3, 0, 0]
        self.line07 = [0, 0, 0, 0, 0, 0, 0, 0]
        self.line08 = [0, [], 4, 0, 0, 0, 0, 0, 0]
        self.line09 = [0, 0, None, 0, 2, 0, 0, 0, 0]

        # Good input
        self.puzzle01 = [   [0, 0, 6, 1, 0, 0, 0, 0, 8], 
                            [0, 8, 0, 0, 9, 0, 0, 3, 0], 
                            [2, 0, 0, 0, 0, 5, 4, 0, 0], 
                            [4, 0, 0, 0, 0, 1, 8, 0, 0], 
                            [0, 3, 0, 0, 7, 0, 0, 4, 0], 
                            [0, 0, 7, 9, 0, 0, 0, 0, 3], 
                            [0, 0, 8, 4, 0, 0, 0, 0, 6], 
                            [0, 2, 0, 0, 5, 0, 0, 8, 0], 
                            [1, 0, 0, 0, 0, 2, 5, 0, 0]]
        
        # Good solution
        self.puzzle02 = [   [5, 3, 4, 6, 7, 8, 9, 1, 2],
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 6, 1, 5, 3, 7, 2, 8, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

        # Bad Inputs
        self.puzzle03 = [   [1, 1, 3, 4, 5, 6, 7, 8, 9],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]

        self.puzzle04 = [   [1, 1, 3, 4, 5, 6, 7, 8, 9],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]

        self.puzzle05 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        self.puzzle06 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 1, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        self.puzzle07 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5]]
       
        self.puzzle08 = [   [1, 2, 3, 4, 5, 6, 7, 8],
                            [4, 0, 6, 7, 8, 9, 1, 2],
                            [7, 8, 9, 1, 2, 3, 4, 5],
                            [2, 3, 4, 5, 6, 7, 8, 9],
                            [5, 6, 7, 8, 9, 1, 2, 3],
                            [8, 9, 1, 2, 3, 4, 5, 6],
                            [3, 4, 5, 6, 7, 8, 9, 1],
                            [6, 7, 8, 9, 1, 2, 3, 4],
                            [9, 1, 2, 3, 4, 5, 6, 7]]
        
        self.puzzle09 = [   [1, 2, 3, 4, 5, 6, 7, 8, 'a'],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        self.puzzle10 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        
        self.puzzle11 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [4, 5, 6, 7, 8, 9, 1, 2, 3],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        # Unsolvable
        self.puzzle12 = [   [0, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 5, 6, 7, 8, 9, 0, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]

        self.puzzle13 = [   [0, 9, 6, 5, 0, 4, 0, 7, 1],
                            [0, 2, 0, 1, 0, 0, 0, 0, 0],
                            [0, 1, 4, 0, 9, 0, 6, 2, 3],
                            [0, 0, 3, 0, 6, 0, 0, 8, 0],
                            [0, 0, 8, 0, 5, 0, 4, 0, 0],
                            [9, 0, 0, 4, 1, 0, 0, 0, 5],
                            [7, 0, 0, 0, 0, 9, 0, 0, 0],
                            [0, 0, 1, 0, 7, 5, 3, 4, 9],
                            [2, 3, 0, 0, 4, 8, 1, 0, 7]]

        self.puzzle20 = [   [1, 2, 3, 4, 5, 6, 7, 8, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [0, 0, 0, 0, 0, 0, 0, 0, 3],
                            [0, 0, 0, 0, 0, 0, 0, 0, 4],
                            [0, 0, 0, 0, 0, 0, 0, 0, 5],
                            [0, 0, 0, 0, 0, 0, 0, 0, 6],
                            [0, 0, 0, 0, 0, 0, 0, 0, 7],
                            [0, 0, 0, 0, 0, 0, 0, 0, 8],
                            [0, 0, 0, 0, 0, 0, 0, 0, 9]]

        # Valid Solution
        self.puzzle14 = [   [5, 3, 4, 6, 7, 8, 9, 1, 2],
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 6, 1, 5, 3, 7, 2, 8, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

        self.puzzle15 = [   [1, 3, 2, 5, 7, 9, 4, 6, 8],
                            [4, 9, 8, 2, 6, 1, 3, 7, 5],
                            [7, 5, 6, 3, 8, 4, 2, 1, 9],
                            [6, 4, 3, 1, 5, 8, 7, 9, 2],
                            [5, 2, 1, 7, 9, 3, 8, 4, 6],
                            [9, 8, 7, 4, 2, 6, 5, 3, 1],
                            [2, 1, 4, 9, 3, 5, 6, 8, 7],
                            [3, 6, 5, 8, 1, 7, 9, 2, 4],
                            [8, 7, 9, 6, 4, 2, 1, 5, 3]]

        # Invalid Solution
        self.puzzle16 = [   [5, 3, 4, 6, 7, 8, 9, 1, 2],
                            [6, 7, 2, 1, 9, 0, 3, 4, 9],
                            [1, 0, 0, 3, 4, 2, 5, 6, 0],
                            [8, 5, 9, 7, 6, 1, 0, 2, 0],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 0, 1, 5, 3, 7, 2, 1, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 0, 0, 4, 8, 1, 1, 7, 9]]

        self.puzzle17 = [   [1, 3, 2, 5, 7, 9, 4, 6, 8],
                            [4, 9, 8, 2, 6, 1, 3, 7, 5],
                            [7, 5, 6, 3, 8, 4, 2, 1, 9],
                            [6, 4, 3, 1, 5, 8, 7, 9, 2],
                            [5, 2, 1, 7, 9, 3, 8, 4, 6],
                            [9, 8, 7, 4, 2, 6, 5, 3, 1],
                            [2, 1, 4, 9, 3, 5, 6, 8, 7],
                            [3, 6, 5, 8, 1, 7, 9, 2, 4],
                            [8, 7, 9, 6, 4, 2, 1, 3, 5]]

        self.puzzle18 = [   [1, 3, 2, 5, 7, 9, 4, 6, 8],
                            [4, 9, 8, 2, 6, 0, 3, 7, 5],
                            [7, 0, 6, 3, 8, 0, 2, 1, 9],
                            [6, 4, 3, 1, 5, 0, 7, 9, 2],
                            [5, 2, 1, 7, 9, 0, 8, 4, 6],
                            [9, 8, 0, 4, 2, 6, 5, 3, 1],
                            [2, 1, 4, 9, 3, 5, 6, 8, 7],
                            [3, 6, 0, 8, 1, 7, 9, 2, 4],
                            [8, 7, 0, 6, 4, 2, 1, 3, 5]]

        self.puzzle19 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [4, 5, 6, 7, 8, 9, 1, 2, 3],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]


    def tearDown(self):
        pass

    def test_valid_line_input(self):        
        self.assertTrue(SudokuValidator._valid_line_input(self.line01))
        self.assertTrue(SudokuValidator._valid_line_input(self.line02))
        self.assertTrue(SudokuValidator._valid_line_input(self.line03))

        self.assertFalse(SudokuValidator._valid_line_input(self.line04))
        self.assertFalse(SudokuValidator._valid_line_input(self.line05))
        self.assertFalse(SudokuValidator._valid_line_input(self.line06))
        self.assertFalse(SudokuValidator._valid_line_input(self.line07))
        self.assertFalse(SudokuValidator._valid_line_input(self.line08))
        self.assertFalse(SudokuValidator._valid_line_input(self.line09))

    def test_valid_line_solution(self):
        self.assertTrue(SudokuValidator._valid_line_solution(self.line01))
        self.assertTrue(SudokuValidator._valid_line_solution(self.line02))

        self.assertFalse(SudokuValidator._valid_line_solution(self.line03))
        self.assertFalse(SudokuValidator._valid_line_solution(self.line04))
        self.assertFalse(SudokuValidator._valid_line_solution(self.line05))
        self.assertFalse(SudokuValidator._valid_line_solution(self.line06))
        self.assertFalse(SudokuValidator._valid_line_solution(self.line07))
        self.assertFalse(SudokuValidator._valid_line_solution(self.line08))
        self.assertFalse(SudokuValidator._valid_line_solution(self.line09))

    def test_is_valid_input(self):
        self.assertTrue(SudokuValidator.is_valid_input(self.puzzle01))
        self.assertTrue(SudokuValidator.is_valid_input(self.puzzle02))
        self.assertTrue(SudokuValidator.is_valid_input(self.puzzle20))

        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle03))
        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle04))
        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle05))
        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle06))
        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle07))
        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle08))
        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle09))
        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle10))
        self.assertFalse(SudokuValidator.is_valid_input(self.puzzle11))
        
    def test_is_valid_solution(self):
        self.assertTrue(SudokuValidator.is_valid_solution(self.puzzle02))
        self.assertTrue(SudokuValidator.is_valid_solution(self.puzzle14))
        self.assertTrue(SudokuValidator.is_valid_solution(self.puzzle15))

        self.assertFalse(SudokuValidator.is_valid_solution(self.puzzle16))
        self.assertFalse(SudokuValidator.is_valid_solution(self.puzzle17))
        self.assertFalse(SudokuValidator.is_valid_solution(self.puzzle18))
        self.assertFalse(SudokuValidator.is_valid_solution(self.puzzle19))
        self.assertFalse(SudokuValidator.is_valid_solution(self.puzzle20))


class SudokuTest(unittest.TestCase):
    def setUp(self):
        # Good input
        self.puzzle01 = [   [0, 0, 6, 1, 0, 0, 0, 0, 8], 
                            [0, 8, 0, 0, 9, 0, 0, 3, 0], 
                            [2, 0, 0, 0, 0, 5, 4, 0, 0], 
                            [4, 0, 0, 0, 0, 1, 8, 0, 0], 
                            [0, 3, 0, 0, 7, 0, 0, 4, 0], 
                            [0, 0, 7, 9, 0, 0, 0, 0, 3], 
                            [0, 0, 8, 4, 0, 0, 0, 0, 6], 
                            [0, 2, 0, 0, 5, 0, 0, 8, 0], 
                            [1, 0, 0, 0, 0, 2, 5, 0, 0]]
        
        # Good solution
        self.puzzle02 = [   [5, 3, 4, 6, 7, 8, 9, 1, 2],
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 6, 1, 5, 3, 7, 2, 8, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

        # Bad Inputs
        self.puzzle03 = [   [1, 1, 3, 4, 5, 6, 7, 8, 9],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]

        self.puzzle04 = [   [1, 1, 3, 4, 5, 6, 7, 8, 9],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]

        self.puzzle05 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        self.puzzle06 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 1, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        self.puzzle07 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5]]
       
        self.puzzle08 = [   [1, 2, 3, 4, 5, 6, 7, 8],
                            [4, 0, 6, 7, 8, 9, 1, 2],
                            [7, 8, 9, 1, 2, 3, 4, 5],
                            [2, 3, 4, 5, 6, 7, 8, 9],
                            [5, 6, 7, 8, 9, 1, 2, 3],
                            [8, 9, 1, 2, 3, 4, 5, 6],
                            [3, 4, 5, 6, 7, 8, 9, 1],
                            [6, 7, 8, 9, 1, 2, 3, 4],
                            [9, 1, 2, 3, 4, 5, 6, 7]]
        
        self.puzzle09 = [   [1, 2, 3, 4, 5, 6, 7, 8, 'a'],
                            [4, 0, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        self.puzzle10 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        
        self.puzzle11 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [4, 5, 6, 7, 8, 9, 1, 2, 3],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        # Unsolvable
        self.puzzle12 = [   [0, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 5, 6, 7, 8, 9, 0, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]

        self.puzzle13 = [   [0, 9, 6, 5, 0, 4, 0, 7, 1],
                            [0, 2, 0, 1, 0, 0, 0, 0, 0],
                            [0, 1, 4, 0, 9, 0, 6, 2, 3],
                            [0, 0, 3, 0, 6, 0, 0, 8, 0],
                            [0, 0, 8, 0, 5, 0, 4, 0, 0],
                            [9, 0, 0, 4, 1, 0, 0, 0, 5],
                            [7, 0, 0, 0, 0, 9, 0, 0, 0],
                            [0, 0, 1, 0, 7, 5, 3, 4, 9],
                            [2, 3, 0, 0, 4, 8, 1, 0, 7]]

        self.puzzle20 = [   [1, 2, 3, 4, 5, 6, 7, 8, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [0, 0, 0, 0, 0, 0, 0, 0, 3],
                            [0, 0, 0, 0, 0, 0, 0, 0, 4],
                            [0, 0, 0, 0, 0, 0, 0, 0, 5],
                            [0, 0, 0, 0, 0, 0, 0, 0, 6],
                            [0, 0, 0, 0, 0, 0, 0, 0, 7],
                            [0, 0, 0, 0, 0, 0, 0, 0, 8],
                            [0, 0, 0, 0, 0, 0, 0, 0, 9]]

        # Valid Solution
        self.puzzle14 = [   [5, 3, 4, 6, 7, 8, 9, 1, 2],
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 6, 1, 5, 3, 7, 2, 8, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

        self.puzzle15 = [   [1, 3, 2, 5, 7, 9, 4, 6, 8],
                            [4, 9, 8, 2, 6, 1, 3, 7, 5],
                            [7, 5, 6, 3, 8, 4, 2, 1, 9],
                            [6, 4, 3, 1, 5, 8, 7, 9, 2],
                            [5, 2, 1, 7, 9, 3, 8, 4, 6],
                            [9, 8, 7, 4, 2, 6, 5, 3, 1],
                            [2, 1, 4, 9, 3, 5, 6, 8, 7],
                            [3, 6, 5, 8, 1, 7, 9, 2, 4],
                            [8, 7, 9, 6, 4, 2, 1, 5, 3]]

        # Invalid Solution
        self.puzzle16 = [   [5, 3, 4, 6, 7, 8, 9, 1, 2],
                            [6, 7, 2, 1, 9, 0, 3, 4, 9],
                            [1, 0, 0, 3, 4, 2, 5, 6, 0],
                            [8, 5, 9, 7, 6, 1, 0, 2, 0],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 0, 1, 5, 3, 7, 2, 1, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 0, 0, 4, 8, 1, 1, 7, 9]]

        self.puzzle17 = [   [1, 3, 2, 5, 7, 9, 4, 6, 8],
                            [4, 9, 8, 2, 6, 1, 3, 7, 5],
                            [7, 5, 6, 3, 8, 4, 2, 1, 9],
                            [6, 4, 3, 1, 5, 8, 7, 9, 2],
                            [5, 2, 1, 7, 9, 3, 8, 4, 6],
                            [9, 8, 7, 4, 2, 6, 5, 3, 1],
                            [2, 1, 4, 9, 3, 5, 6, 8, 7],
                            [3, 6, 5, 8, 1, 7, 9, 2, 4],
                            [8, 7, 9, 6, 4, 2, 1, 3, 5]]

        self.puzzle18 = [   [1, 3, 2, 5, 7, 9, 4, 6, 8],
                            [4, 9, 8, 2, 6, 0, 3, 7, 5],
                            [7, 0, 6, 3, 8, 0, 2, 1, 9],
                            [6, 4, 3, 1, 5, 0, 7, 9, 2],
                            [5, 2, 1, 7, 9, 0, 8, 4, 6],
                            [9, 8, 0, 4, 2, 6, 5, 3, 1],
                            [2, 1, 4, 9, 3, 5, 6, 8, 7],
                            [3, 6, 0, 8, 1, 7, 9, 2, 4],
                            [8, 7, 0, 6, 4, 2, 1, 3, 5]]

        self.puzzle19 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [4, 5, 6, 7, 8, 9, 1, 2, 3],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]

        self.board01 = Sudoku(self.puzzle01)
        self.board02 = Sudoku(self.puzzle02)

        self.board12 = Sudoku(self.puzzle12)
        self.board13 = Sudoku(self.puzzle13)
        self.board20 = Sudoku(self.puzzle20)

    def test_constructor(self):
        Sudoku(self.puzzle01)
        Sudoku(self.puzzle02)
        Sudoku(self.puzzle20)

        self.failUnlessRaises(Exception, Sudoku, self.puzzle03)
        self.failUnlessRaises(Exception, Sudoku, self.puzzle04)
        self.failUnlessRaises(Exception, Sudoku, self.puzzle05)
        self.failUnlessRaises(Exception, Sudoku, self.puzzle06)
        self.failUnlessRaises(Exception, Sudoku, self.puzzle07)
        self.failUnlessRaises(Exception, Sudoku, self.puzzle08)
        self.failUnlessRaises(Exception, Sudoku, self.puzzle09)
        self.failUnlessRaises(Exception, Sudoku, self.puzzle10)
        self.failUnlessRaises(Exception, Sudoku, self.puzzle11)

    # Only Testing number of results here
    def test_solve(self):
        self.board01.solve()
        self.board02.solve()
        self.board12.solve()
        self.board13.solve()
        self.board20.solve()

        self.assertEqual(self.board01.num_of_solutions, 1)
        self.assertEqual(self.board02.num_of_solutions, 1)
        self.assertEqual(self.board12.num_of_solutions, 0)
        self.assertEqual(self.board13.num_of_solutions, 0)
        self.assertEqual(self.board20.num_of_solutions, 0)



if __name__=="__main__":
    unittest.main()