"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def right_number(self, row, col):
        """
        Check if the position has the right number.
        """
        return self.get_number(row, col) == self.get_width()*row+col

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # Tile zero is positioned at (i,j).
        if self.get_number(target_row, target_col) != 0:
            return False
        # All tiles in rows i+1 or below are positioned at their solved location.
        start_col = (target_col if target_row==0 else 0)
        for row in range(target_row+1, self.get_height()):
            for col in range(start_col, self.get_width()):
                if not self.right_number(row, col):
                    return False
        # All tiles in row i to the right of position (i,j) are positioned at
        # their solved location.
        for col in range(target_col+1, self.get_width()):
            if not self.right_number(target_row, col):
                return False
        return True

    def move_tile(self, target_row, target_col, val):
        """
        helper function only calculates the movements
        """
        # a little bit twisted here for the use of both solve_interior_tile and solve_col0_tile
        solved_row, solved_col = self.current_position(0, val)
        movements = ""
        #print solved_row, solved_col, target_row, target_col, val
        if solved_row == target_row and solved_col == target_col:
            return ""
        if solved_row == target_row:
            if target_col > solved_col:
                movements = "l"*(target_col-solved_col)+"urrdl"*(target_col-solved_col-1)
            else:
                movements = "r"*(solved_col-target_col)+"ulldr"*(solved_col-target_col-1)+"ulld"
        elif solved_col == target_col:
            movements = "u"*(target_row-solved_row)+"lddru"*(target_row-solved_row-1)+"ld"
        elif solved_col < target_col:
            if solved_col == 0:
                movements = "l"*(target_col-solved_col)+"u"*(target_row-solved_row)+"rddlu"*(target_row-solved_row-1)+"rdl"+"urrdl"*(target_col-solved_col-1)
            else:
                movements = "l"*(target_col-solved_col)+"u"*(target_row-solved_row)+"lddru"*(target_row-solved_row-1)+"rd"+"urrdl"*(target_col-solved_col-1)
        elif solved_col > target_col:
            if solved_row == 0:
                movements = "u"*(target_row-solved_row)+"r"*(solved_col-target_col)+"dllur"*(solved_col-target_col-1)+"dlu"+"lddru"*(target_row-solved_row-1)+"ld"
            else:
                movements = "u"*(target_row-solved_row)+"r"*(solved_col-target_col)+"ulldr"*(solved_col-target_col-1)+"ullddru"+"lddru"*(target_row-solved_row-1)+"ld"
        #print "In interior:", movements
        return movements

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        movements = self.move_tile(target_row, target_col, target_row*self.get_width()+target_col)
        self.update_puzzle(movements)
        return movements

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        solved_row, solved_col = self.current_position(target_row, 0)
        movements = ""
        if solved_row == target_row-1 and solved_col == 0:
            movements = "u"
        else:
            local_board = self.clone()
            local_board.update_puzzle("ur")
            movements = "ur" + local_board.move_tile(target_row-1, 1, target_row*self.get_width()) + "ruldrdlurdluurddlu"
        movements += "r"*(self.get_width()-1)
        #print movements
        self.update_puzzle(movements)
        return movements

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        return self.lower_row_invariant(0, target_col)

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        return self.lower_row_invariant(1, target_col)

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

import poc_simpletest

def test_lower_row_invariant():
    suite = poc_simpletest.TestSuite()
    print("test_lower_row_invariant():"),
    suite.run_test(Puzzle(4,4,[[3,4,2,1],[6,5,0,7],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(1, 2), True, "Test 0: Zero in the middle.")
    suite.run_test(Puzzle(4,4,[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(0, 0), True, "Test 1: Zero in the upper left.")
    suite.run_test(Puzzle(4,4,[[3,1,2,0],[4,5,6,7],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(0, 3), True, "Test 2: Zero in the upper right.")
    suite.run_test(Puzzle(4,4,[[3,4,2,1],[6,5,12,7],[8,9,10,11],[0,13,14,15]]).lower_row_invariant(3, 0), True, "Test 3: Zero in the bottom left.")
    suite.run_test(Puzzle(4,4,[[3,4,2,1],[6,5,15,7],[8,9,10,11],[12,13,14,0]]).lower_row_invariant(3, 3), True, "Test 4: Zero in the bottom right.")
    suite.run_test(Puzzle(4,4,[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(0, 3), False, "Test 5: Invalid.")
    suite.run_test(Puzzle(4,4,[[1,0,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(0, 0), False, "Test 6: Invalid.")
    suite.run_test(Puzzle(4,4,[[0,3,2,1],[4,5,6,7],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(0, 0), False, "Test 7: Invalid.")
    suite.report_results()

def test_solve_interior_tile():
    suite = poc_simpletest.TestSuite()
    print("test_solve_interior_tile():"),

    puzzle = Puzzle(4,4,[[2,11,12,13],[9,4,6,1],[5,7,8,3],[10,0,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 1), True, "Test 0.0:")
    puzzle.solve_interior_tile(3, 1)
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 0.1:")

    puzzle = Puzzle(4,4,[[2,11,12,10],[9,4,6,1],[5,7,8,3],[15,13,14,0]])
    suite.run_test(puzzle.lower_row_invariant(3, 3), True, "Test 1.0:")
    puzzle.solve_interior_tile(3, 3)
    suite.run_test(puzzle.lower_row_invariant(3, 2), True, "Test 1.1:")

    puzzle = Puzzle(4,4,[[2,11,12,10],[9,4,6,1],[5,7,8,3],[13,0,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 1), True, "Test 2.0:")
    puzzle.solve_interior_tile(3, 1)
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 2.1:")

    puzzle = Puzzle(4,4,[[13,11,12,2],[9,4,6,1],[5,7,8,3],[10,0,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 1), True, "Test 3.0:")
    puzzle.solve_interior_tile(3, 1)
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 3.1:")

    puzzle = Puzzle(4,4,[[3,11,12,2],[9,4,6,1],[5,7,8,13],[10,0,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 1), True, "Test 4.0:")
    puzzle.solve_interior_tile(3, 1)
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 4.1:")

    puzzle = Puzzle(4,4,[[3,13,12,2],[9,4,6,1],[5,7,8,11],[10,0,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 1), True, "Test 5.0:")
    puzzle.solve_interior_tile(3, 1)
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 5.1:")

    suite.report_results()

def test_solve_col0_tile():
    suite = poc_simpletest.TestSuite()
    print("test_solve_col0_tile():")

    puzzle = Puzzle(4,4,[[2,11,12,10],[9,4,6,1],[5,7,8,3],[0,13,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 0.0:")
    print puzzle
    puzzle.solve_col0_tile(3)
    print puzzle
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, "Test 0.1:")

    puzzle = Puzzle(4,4,[[2,11,3,10],[9,4,6,1],[5,7,8,12],[0,13,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 1.0:")
    print puzzle
    puzzle.solve_col0_tile(3)
    print puzzle
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, "Test 1.1:")

    puzzle = Puzzle(4,4,[[12,11,2,10],[9,4,6,1],[5,7,8,3],[0,13,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 2.0:")
    print puzzle
    puzzle.solve_col0_tile(3)
    print puzzle
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, "Test 2.1:")

    puzzle = Puzzle(4,4,[[10,11,2,12],[9,4,6,1],[5,7,8,3],[0,13,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 3.0:")
    print puzzle
    puzzle.solve_col0_tile(3)
    print puzzle
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, "Test 3.1:")

    puzzle = Puzzle(4,4,[[10,11,2,5],[9,4,6,1],[12,7,8,3],[0,13,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 4.0:")
    print puzzle
    puzzle.solve_col0_tile(3)
    print puzzle
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, "Test 4.1:")

    puzzle = Puzzle(4,4,[[10,11,2,5],[9,4,6,1],[7,12,8,3],[0,13,14,15]])
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, "Test 5.0:")
    print puzzle
    puzzle.solve_col0_tile(3)
    print puzzle
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, "Test 5.1:")

    puzzle = Puzzle(4,4,[[8,3,2,5],[7,4,6,1],[0,9,10,11],[12,13,14,15]])
    suite.run_test(puzzle.lower_row_invariant(2, 0), True, "Test 6.0:")
    print puzzle
    puzzle.solve_col0_tile(2)
    print puzzle
    suite.run_test(puzzle.lower_row_invariant(1, 3), True, "Test 6.1:")

    puzzle = Puzzle(4,4,[[1,3,2,5],[7,4,6,8],[0,9,10,11],[12,13,14,15]])
    suite.run_test(puzzle.lower_row_invariant(2, 0), True, "Test 7.0:")
    print puzzle
    puzzle.solve_col0_tile(2)
    print puzzle
    suite.run_test(puzzle.lower_row_invariant(1, 3), True, "Test 7.1:")

    suite.report_results()

def test_row1_invariant():
    suite = poc_simpletest.TestSuite()
    print "\n==========="
    print("test_row1_invariant():"),
    suite.run_test(Puzzle(4,4,[[3,4,2,1],[6,5,0,7],[8,9,10,11],[12,13,14,15]]).row1_invariant(2), True, "Test 0")
    suite.run_test(Puzzle(4,4,[[3,4,2,1],[6,5,7,0],[8,9,10,11],[12,13,14,15]]).row1_invariant(3), True, "Test 1")
    suite.run_test(Puzzle(4,4,[[3,4,2,1],[6,5,0,7],[8,9,10,11],[12,13,14,15]]).row1_invariant(3), False, "Test 2: Invalid.")
    suite.run_test(Puzzle(4,4,[[3,4,2,1],[6,5,7,0],[8,9,10,11],[15,13,14,12]]).row1_invariant(3), False, "Test 3: Invalid.")
    suite.report_results()

def test_row0_invariant():
    suite = poc_simpletest.TestSuite()
    print "\n==========="
    print("test_row0_invariant():"),
    suite.run_test(Puzzle(4,4,[[2,4,0,3],[5,1,6,7],[8,9,10,11],[12,13,14,15]]).row0_invariant(2), True, "Test 0")
    suite.run_test(Puzzle(4,4,[[3,4,2,0],[5,1,6,7],[8,9,10,11],[12,13,14,15]]).row0_invariant(3), True, "Test 1")
    suite.run_test(Puzzle(4,4,[[3,4,0,2],[5,1,6,7],[8,9,10,11],[12,13,14,15]]).row0_invariant(3), False, "Test 2: Invalid.")
    suite.run_test(Puzzle(4,4,[[3,4,2,0],[5,1,7,6],[8,9,10,11],[12,13,14,15]]).row0_invariant(3), False, "Test 3: Invalid.")
    suite.run_test(Puzzle(4,4,[[3,4,2,0],[5,1,6,7],[8,9,10,11],[12,13,15,14]]).row0_invariant(3), False, "Test 4: Invalid.")
    suite.report_results()

test_lower_row_invariant()
test_solve_interior_tile()
test_solve_col0_tile()
test_row1_invariant()
test_row0_invariant()
