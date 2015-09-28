"""
Zombie Apocalypse mini-project
Click "Mouse click" button to toggle items added by mouse clicks
Zombies have four way movement, humans have eight way movement

Modified GUI with auto pursuit option
"""

import simplegui

# Global constants
EMPTY = 0
FULL = 1
HAS_ZOMBIE = 2
HAS_HUMAN = 4
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"
CELL_COLORS = {EMPTY: "White",
               FULL: "Black",
               HAS_ZOMBIE: "Red",
               HAS_HUMAN: "Green",
               HAS_ZOMBIE | HAS_HUMAN: "Purple"}

# GUI constants
CELL_SIZE = 10
LABEL_STRING = "Mouse click: Add "


class ZombieGUI:
    """
    Container for interactive content
    """

    def __init__(self, simulation):
        """ 
        Create frame and timers, register event handlers
        """
        self._simulation = simulation
        self._grid_height = self._simulation.get_grid_height()
        self._grid_width = self._simulation.get_grid_width()
        self._frame = simplegui.create_frame("Zombie Apocalypse simulation",
                                             self._grid_width * CELL_SIZE,
                                             self._grid_height * CELL_SIZE)
        self._frame.set_canvas_background("White")
        self._frame.add_button("Clear all", self.clear, 200)
        self._item_type = OBSTACLE
        self._item_label = self._frame.add_button(
            LABEL_STRING + self._item_type, self.toggle_item, 200)
        self._frame.add_button("Humans flee", self.flee, 200)
        self._frame.add_button("Zombies stalk", self.stalk, 200)
        self._frame.add_button("Auto Flee (toggle)", self.auto_flee, 200)
        self._frame.add_button("Auto Stalk (toggle)", self.auto_stalk, 200)
        self._frame.add_button("Full Pursuit (toggle stalk and flee)",
                               self.full_pursuit, 200)
        self._frame.set_mouseclick_handler(self.add_item)
        self._frame.set_draw_handler(self.draw)
        self._stalk_on = False
        self._flee_on = False

    def start(self):
        """
        Start frame
        """
        self._frame.start()

    def clear(self):
        """ 
        Event handler for button that clears everything
        """
        self._simulation.clear()

    def flee(self):
        """ 
        Event handler for button that causes humans to flee zombies by one cell
        Diagonal movement allowed
        """
        zombie_distance = self._simulation.compute_distance_field(ZOMBIE)
        self._simulation.move_humans(zombie_distance)

    def stalk(self):
        """ 
        Event handler for button that causes zombies to stack humans by one cell
        Diagonal movement not allowed
        """
        human_distance = self._simulation.compute_distance_field(HUMAN)
        self._simulation.move_zombies(human_distance)

    def auto_stalk(self):
        """
        Toggles auto stalk flag
        """
        self._stalk_on = not self._stalk_on

    def auto_flee(self):
        """
        Toggles auto flee flag
        """
        self._flee_on = not self._flee_on

    def full_pursuit(self):
        """
        Toggles auto flee and auto stalk flags
        """
        self._flee_on = not self._flee_on
        self._stalk_on = not self._stalk_on

    def toggle_item(self):
        """ 
        Event handler to toggle between new obstacles, humans and zombies
        """
        if self._item_type == OBSTACLE:
            self._item_type = ZOMBIE
            self._item_label.set_text(LABEL_STRING + ZOMBIE)
        elif self._item_type == ZOMBIE:
            self._item_type = HUMAN
            self._item_label.set_text(LABEL_STRING + HUMAN)
        elif self._item_type == HUMAN:
            self._item_type = OBSTACLE
            self._item_label.set_text(LABEL_STRING + OBSTACLE)

    def add_item(self, click_position):
        """ 
        Event handler to add new obstacles, humans and zombies
        """
        row, col = self._simulation.get_index(click_position, CELL_SIZE)
        if self._item_type == OBSTACLE:
            if not self.is_occupied(row, col):
                self._simulation.set_full(row, col)
        elif self._item_type == ZOMBIE:
            if self._simulation.is_empty(row, col):
                self._simulation.add_zombie(row, col)
        elif self._item_type == HUMAN:
            if self._simulation.is_empty(row, col):
                self._simulation.add_human(row, col)

    def is_occupied(self, row, col):
        """
        Determines whether the given cell contains any humans or zombies
        """
        cell = (row, col)
        return (cell in self._simulation.zombies()) or (
            cell in self._simulation.humans())

    def draw_cell(self, canvas, row, col, color="Cyan"):
        """
        Draw a cell in the grid
        """
        upper_left = [col * CELL_SIZE, row * CELL_SIZE]
        upper_right = [(col + 1) * CELL_SIZE, row * CELL_SIZE]
        lower_right = [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE]
        lower_left = [col * CELL_SIZE, (row + 1) * CELL_SIZE]
        canvas.draw_polygon(
            [upper_left, upper_right, lower_right, lower_left
             ], 1, "Black", color)

    def draw_grid(self, canvas, grid):
        """
        Draw entire grid
        """
        for col in range(self._grid_width):
            for row in range(self._grid_height):
                color = CELL_COLORS[grid[row][col]]
                if color != "White":
                    self.draw_cell(canvas, row, col, color)

    def draw(self, canvas):
        """
        Handler for drawing obstacle grid, human queue and zombie queue
        """
        grid = [[EMPTY if self._simulation.is_empty(dummy_row, dummy_col) else FULL \
                        for dummy_col in range(self._grid_width)] \
                        for dummy_row in range(self._grid_height)]
        for row, col in self._simulation.humans():
            grid[row][col] |= HAS_HUMAN
        for row, col in self._simulation.zombies():
            grid[row][col] |= HAS_ZOMBIE
        if self._flee_on:
            self.flee()
        if self._stalk_on:
            self.stalk()
        self.draw_grid(canvas, grid)


# Start interactive simulation
def run_gui(sim):
    """
    Encapsulate frame
    """
    gui = ZombieGUI(sim)
    gui.start()
