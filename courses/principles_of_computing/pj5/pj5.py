"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        return

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
        return

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        return

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for person in self._human_list:
            yield person

    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        visited = poc_grid.Grid(poc_grid.Grid.get_grid_height(self), poc_grid.Grid.get_grid_width(self))
        product = poc_grid.Grid.get_grid_height(self)*poc_grid.Grid.get_grid_width(self)
        distance_field = [[product for _ in range(poc_grid.Grid.get_grid_width(self))] for _ in range(poc_grid.Grid.get_grid_height(self))]
        boundary = poc_queue.Queue()
        # initialize related variables
        if entity_type == ZOMBIE:
            lst = self._zombie_list
        elif entity_type == HUMAN:
            lst = self._human_list
        else:
            raise ValueError("The entity_type should be either ZOMBIE or HUMAN -- COMPUTE_DISTANCE_FIELD")

        for item in lst:
            boundary.enqueue(item)
            visited.set_full(item[0], item[1])
            distance_field[item[0]][item[1]] = 0
        # perform BFS
        while len(boundary) != 0:
            cell = boundary.dequeue()
            neighbors = self.four_neighbors(cell[0], cell[1])
            for neighbor in neighbors:
                # omit any visited cell and only check the passable cells
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    # BES only visit each cell once
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = \
                        min(distance_field[neighbor[0]][neighbor[1]], distance_field[cell[0]][cell[1]]+1)
        return distance_field

    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        result = []
        for person in self._human_list:
            neighbors = self.eight_neighbors(person[0], person[1])
            moves = [person]
            max_distance = zombie_distance[person[0]][person[1]]
            for cell in neighbors:
                if zombie_distance[cell[0]][cell[1]] > max_distance:
                    max_distance = zombie_distance[cell[0]][cell[1]]
                    moves = [cell]
                elif zombie_distance[cell[0]][cell[1]] == max_distance:
                    moves.append(cell)
            result.append(moves[random.randrange(len(moves))])
        self._human_list = result
        return

    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        result = []
        for zombie in self._zombie_list:
            neighbors = self.four_neighbors(zombie[0], zombie[1])
            moves = [zombie]
            min_distance = human_distance[zombie[0]][zombie[1]]
            for cell in neighbors:
                if human_distance[cell[0]][cell[1]] < min_distance:
                    min_distance = human_distance[cell[0]][cell[1]]
                    moves = [cell]
                elif human_distance[cell[0]][cell[1]] == min_distance:
                    moves.append(cell)
            result.append(moves[random.randrange(len(moves))])
        self._zombie_list = result
        return

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Zombie(30, 40))

