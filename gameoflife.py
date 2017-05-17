from time import sleep
from random import sample

# size of the grid
GRID_SIZE = 4
# time in seconds
TIME_BETWEEN_STEPS = 2
# amount of generations
AMOUNT_OF_GENERATIONS = 5


class LifeEmulation(object):

    def __init__(self, size):
        self.size = size
        self._generate_grid()

    def _generate_grid(self):
        """Generate the random population."""
        self.grid = [
            [
                sample([1, 0], 1)[0]
                for _ in range(self.size)
            ]
            for _ in range(self.size)
        ]

    def _step(self):
        """Create the new generation."""
        new_generation = [
            [0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)
        ]
        # generate a new step
        for p in range(self.size):
            for q in range(self.size):
                # Count the amount of neighbours
                neighs = self._neighbours(p,q)
                # keep alive
                if self.grid[p][q]:
                    if neighs == 2 or neighs == 3:
                        new_generation[p][q] = 1
                # or become a live cell
                elif neighs == 3:
                    new_generation[p][q] = 1
        return new_generation

    def _neighbours(self, x, y):
        """Tell how many alive neighbours the cell (x, y) has."""
        neighs = 0
        for a in range(max(0, x-1), min(self.size, x + 2)):
            for b in range(max(0, y-1), min(self.size, y + 2)):
                if (a, b) != (x, y) and self.grid[a][b]:
                    neighs += 1
        return neighs

    def run_simulation(self):
        """Run the entire simulation."""
        # print the initial grid
        print('Initial generation')
        self.print_grid()
        # simulate and print evolution
        for generation in range(AMOUNT_OF_GENERATIONS):
            # sleep for a while
            sleep(TIME_BETWEEN_STEPS)
            # generate the new grid
            self.grid = self._step()
            # print the new generation
            print('Generation {}'.format(generation + 1))
            self.print_grid()

    def print_grid(self):
        """Print the generation."""
        for row in self.grid:
            print(row)
        print('\n')


if __name__ == '__main__':
    grid = LifeEmulation(GRID_SIZE)
    grid.run_simulation()
