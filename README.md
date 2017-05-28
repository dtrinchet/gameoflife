# Game of Life

 In 1970 the British Mathematician John Conway designed a game to simulate the evolution of certain population, he called it the "Game of Life".
 
 The game is based on a set of rules that mimics the chaotic yet patterned growth of a colony of biological organisms. The "game" takes place on a two-dimensional grid consisting of "living" and "dead" cells, and the rules to step from generation to generation are simple:

* Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
* Stasis: if a living cell is surrounded by two or three living cells, it survives.
* Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
* Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.


# Python implementation

The script provided in this repository is a simple implementation of the game in Python.


# How to run

As you can see in the help of the script:

    $ ./gameoflife.py -h
    usage: gameoflife.py [-h] [-s int] [-g int] [-t int]

    optional arguments:
      -h, --help            show this help message and exit
      -s int, --size int    Size of the grid
      -g int, --generations    int Amount of generations
      -t int, --time int    Time between generations (in seconds)
      
You can run the script passing the size of the grid, the amount of generations and the time between generations. 

    $ ./gameoflife.py -s 8 -g 10  # 8x8 grid, with 10 generations.
    
    Initial generation
    [1, 1, 0, 0, 0, 0, 0, 0]
    [1, 1, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 1, 1, 0, 1]
    [1, 1, 1, 1, 0, 1, 0, 1]
    [1, 1, 1, 0, 1, 1, 1, 0]
    [1, 1, 0, 1, 1, 0, 1, 0]
    [0, 1, 0, 1, 1, 0, 0, 1]
    [0, 0, 0, 0, 0, 1, 0, 1]
    
    
    Generation 1
    [1, 1, 0, 0, 0, 0, 0, 0]
    [1, 1, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 1, 1, 1, 0, 0]
    [1, 0, 0, 0, 0, 0, 0, 1]
    [0, 0, 0, 0, 0, 0, 0, 1]
    [0, 0, 0, 0, 0, 0, 1, 1]
    [1, 1, 0, 1, 0, 0, 0, 1]
    [0, 0, 0, 0, 1, 0, 1, 0]
    
    Generation 2
    [1, 1, 0, 0, 0, 0, 0, 0]
    [1, 1, 1, 0, 1, 0, 0, 0]
    [1, 1, 0, 0, 1, 0, 0, 0]
    [0, 0, 0, 0, 1, 0, 1, 0]
    [0, 0, 0, 0, 0, 0, 0, 1]
    [0, 0, 0, 0, 0, 0, 1, 1]
    [0, 0, 0, 0, 0, 1, 0, 1]
    [0, 0, 0, 0, 0, 0, 0, 0]
    ...
