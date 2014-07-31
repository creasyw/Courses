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
        for row in range(target_row+1, self.get_height()):
            for col in range(self.get_width()):
                if not self.right_number(row, col):
                    return False
        # All tiles in row i to the right of position (i,j) are positioned at
        # their solved location.
        for col in range(target_col+1, self.get_width()):
            if not self.right_number(target_row, col):
                return False
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        solved_row, solved_col = self.current_position(target_row, target_col)
        movements = ""
        if solved_row == target_row and solved_col == target_col:
            return ""
        if solved_row == target_row:
            movements = "l"*(target_col-solved_col)+"urrdl"*(target_col-solved_col-1)
        elif solved_col == target_col:
            movements = "u"*(target_row-solved_row)+"lddru"*(target_row-solved_row-1)+"ld"
        elif solved_col < target_col:
            movements = "l"*(target_col-solved_col)+"u"*(target_row-solved_row)+"lddru"*(target_row-solved_row-1)+"rd"+"urrdl"*(target_col-solved_col-1)
        elif solved_col > target_col:
            movements = "u"*(target_row-solved_row)+"r"*(solved_col-target_col)+"dllur"*(solved_col-target_col-1)+"dlu"+"lddru"*(target_row-solved_row-1)+"ld"
        self.update_puzzle(movements)
        return movements

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

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

test_lower_row_invariant()
