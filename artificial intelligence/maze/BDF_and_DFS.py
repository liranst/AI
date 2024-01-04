import numpy as np
from matplotlib import pyplot as plt


class Maze_RUNING:
    """
    Class for generating and solving a maze using a specified search algorithm.
    """

    def __init__(self, size_maze, start, gold, search_algorithm):
        """
        Initialize the maze solver.

        Args:
        - size_maze (int): Size of the maze.
        - start (list): Starting position in the maze.
        - gold (list): Goal position in the maze.
        - search_algorithm (str): Search algorithm to be used ('DFS' or 'BDF').
        """
        self.search_algorithm = search_algorithm
        self.size_maze = size_maze
        self.start = start
        self.gold = gold
        self.maze = self.create_maze()
        self.frontier = [[start]]
        self.explored = set()

    def create_maze(self):
        """
        Create a random maze using numpy with boundaries and start/goal positions marked.

        Returns:
        - maze (numpy.ndarray): Randomly generated maze.
        """
        self.maze = np.random.binomial(1, 0.25, size=(self.size_maze + 2, self.size_maze + 2))
        for i in range(self.size_maze + 2):
            self.maze[-1, i] = self.maze[0, i] = self.maze[i, -1] = self.maze[i, 0] = 1
            self.maze[1, 1] = self.maze[-2, -2] = 0
        return self.maze

    def get_actions(self, node):
        """
        Get possible actions from a given node.

        Args:
        - node (list): Current node in the maze.

        Returns:
        - children (list): List of possible child nodes from the given node.
        """
        children = []
        moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for move in moves:
            new_i = node[-1][0] + move[0]
            new_j = node[-1][1] + move[1]
            if 0 < new_i < len(self.maze) and 0 < new_j < len(self.maze) and self.maze[new_i][new_j] != 1:
                children.append(node + [[new_i, new_j]])
        return children

    def maze_running(self):
        """
        Run the selected search algorithm to solve the maze.

        Returns:
        - solution (list): Path from start to goal (if found).
        - explored (set): Set of explored nodes during the search.
        """
        dict_search_algorithm = {"BDF": 0, "DFS": -1}
        self.search_algorithm = dict_search_algorithm[self.search_algorithm]

        while self.frontier:
            current_path = self.frontier.pop(self.search_algorithm)
            current_node = current_path[-1]

            if current_node == self.gold:
                return current_path, self.explored

            if tuple(current_node) not in self.explored:
                self.explored.add(tuple(current_node))

                for child_path in self.get_actions(current_path):
                    child_node = child_path[-1]
                    if tuple(child_node) not in self.explored:
                        self.frontier.append(child_path)
        return [], self.explored

    def visualize_maze(self, solution=None, E=None):
        """
        Visualize the maze, marking the start, goal, explored path, and solution path.

        Args:
        - solution (list): Path from start to goal (if found).
        - E (set): Explored nodes during the search.
        """
        maze_copy = np.array(self.maze)
        maze_copy[self.start[0], self.start[1]] = 4
        maze_copy[self.gold[0], self.gold[1]] = 4
        if solution:
            for step in E:
                maze_copy[step[0], step[1]] = 2

        if solution:
            for step in solution:
                maze_copy[step[0], step[1]] = 4
        plt.imshow(maze_copy, cmap='gist_gray')
        plt.title('Maze')
        plt.axis()
        plt.show()


if __name__ == "__main__":
    # Example usage:
    n = 50
    maze_solver = Maze_RUNING(n, start=[1, 1], gold=[n, n], search_algorithm="BDF")
    solution, y = maze_solver.maze_running()
    maze_solver.visualize_maze(solution, y)
