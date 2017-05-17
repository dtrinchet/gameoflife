# Game of Life

 In 1970 the British Mathematician John Conway designed a game to simulate the evolution of certain population, he called it the "Game of Life".
 
 The game is based on a set of rules that mimics the chaotic yet patterned growth of a colony of biological organisms. The "game" takes place on a two-dimensional grid consisting of "living" and "dead" cells, and the rules to step from generation to generation are simple:

* Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
* Stasis: if a living cell is surrounded by two or three living cells, it survives.
* Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
* Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.


# Python implementation

The script provided at this repository is a simple implementation of the game in Python.