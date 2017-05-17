import argparse
from time import sleep
from random import sample

# size of the grid
DEFAULT_GRID_SIZE = 4
# time in seconds
DEFAULT_GENERATIONS_TIME = 2
# amount of generations
DEFAULT_GENERATIONS_AMOUNT = 5


class LifeEmulation(object):

    def __init__(self, size, generations_amount, generations_time):
        self.grid_size = size
        self.generations_amount = generations_amount
        self.generations_time = generations_time
        self._generate_grid()

    def _generate_grid(self):
        """Generate the random population."""
        self.grid = [
            [
                sample([1, 0], 1)[0]
                for _ in range(self.grid_size)
            ]
            for _ in range(self.grid_size)
        ]

    def _step(self):
        """Create the new generation."""
        new_generation = [
            [0 for _ in range(self.grid_size)] for _ in range(self.grid_size)
            ]
        # generate a new step
        for p in range(self.grid_size):
            for q in range(self.grid_size):
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
        for a in range(max(0, x-1), min(self.grid_size, x + 2)):
            for b in range(max(0, y-1), min(self.grid_size, y + 2)):
                if (a, b) != (x, y) and self.grid[a][b]:
                    neighs += 1
        return neighs

    def run_simulation(self):
        """Run the entire simulation."""
        # print the initial grid
        print('Initial generation')
        self.print_grid()
        # simulate and print evolution
        for generation in range(self.generations_amount):
            # sleep for a while
            sleep(self.generations_time)
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
    """
    $ ./gameoflife.py -s 8 -g 5 -t 2
    """
    parser = argparse.ArgumentParser()
    size = parser.add_argument(
        '-s',
        '--size',
        metavar='int',
        type=int,
        default=DEFAULT_GRID_SIZE,
        help='Size of the grid'
    )
    parser.add_argument(
        '-g',
        '--generations',
        metavar='int',
        type=int,
        default=DEFAULT_GENERATIONS_AMOUNT,
        help='Amount of generations'
    )
    parser.add_argument(
        '-t', '--time',
        metavar='int',
        type=int,
        default=DEFAULT_GENERATIONS_TIME,
        help='Time between generations (in seconds)'
    )

    args = parser.parse_args()
    grid = LifeEmulation(
        size=args.size,
        generations_amount=args.generations,
        generations_time=args.time
    )
    grid.run_simulation()
