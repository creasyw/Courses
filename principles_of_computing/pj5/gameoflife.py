"""
Game of Life demo
"""

import poc_grid
import poc_gol_gui

# constants
EMPTY = 0 
FULL = 1

class GameOfLife(poc_grid.Grid):
    """
    Extend Grid class to support Game of Life
    """
    
    def update_gol(self):
        """
        Function that performs one step of the Game of Life
        """
        
        updated_grid = [[self.update_cell(row, col) \
                            for col in range(self.get_grid_width())] \
                            for row in range(self.get_grid_height())]
        
        for col in range(self.get_grid_width()):
            for row in range(self.get_grid_height()):
                if updated_grid[row][col] == EMPTY:
                    self.set_empty(row, col)
                else:
                    self.set_full(row, col)
                    

    def update_cell(self, row, col):
        """
        Function that computes the update for one cell in the Game of Life
        """
        # compute number of living neighbors
        neighbors = self.eight_neighbors(row, col)
        living_neighbors = 0
        for neighbor in neighbors:
            if not self.is_empty(neighbor[0], neighbor[1]):
                living_neighbors += 1
            
        # logic for Game of life        
        if (living_neighbors == 3) or (living_neighbors == 2 and not self.is_empty(row, col)):
            return FULL
        else:
            return EMPTY
        
# run gui        
poc_gol_gui.run_gui(GameOfLife(30, 40))
