# Othello Python Game

This is a Python implementation of an Othello game using the Processing
development environment to render the game graphics on the monitor. 

## Getting Started:

1. Download Processing 3 from the Github link:
    https://github.com/processing/processing/releases/tag/processing-0270-3.5.4

2. Run Processing 3 and once the screen appears, set it to Python mode with
the mode adjuster in the top right corner of the screen.

3. Open the pythonGame directory within Processing 3, click on othello_game.pyde file
within that directory, and run the program by clicking the play arrow in 
the top left corner of the screen.

4. Enter you player information, indicate whether you would like user hints
and select your game difficulty. Please read AI.txt for a full description of
the different game difficulties and the mechanics behind them.

## Gameplay

1. Black always moves first.

2. If on your turn you cannot outflank and flip at least one opposing disk, your turn is forfeited and your opponent moves
again. However, if a move is available to you, you may not forfeit your turn. 

3. Players may not skip over their own colour disk(s) to outflank an opposing disk.

4. Disk(s) may only be outflanked as a direct result of a move and must fall in the direct line of the disk placed down.

5. All disks outflanked in any one move must be flipped, even if it is to the player's advantage not to flip them at all. 

6. Once a disk is placed on a square, it can never be moved to another square later in the game. 

7. When it is no longer possible for either player to move, the game is over. Disks are counted and the player with the majority of their colour showing is the winner.

Note: It is possible for a game to end before all 64 squares are filled.

## Game Board

![image](https://user-images.githubusercontent.com/58372262/175492458-dc37d0a8-6d4d-4ff6-99a7-28a7478933e2.png)

## AI Implementation

The AI in this Othello game operates on three separate difficult levels: easy,
intermediate, and hard. This section details the move selection criteria of
each difficulty level:

### Easy
The easy AI difficult selects a random move from the list of legal moves presented to the move selection function of the Computer class. This represents the most basic selection criteria, not using any type of critera for selecting a particular move except for random chance.
    
### Intermediate 
The intermediate AI selects a move based on a greedy algorithm implementation. This algorithm examines each legal move available to the computer AI on a given turn and identifies the move that flips the most tiles of the human player. Once the legal move with the highest flips is identified, that move is selected and executed.
        
### Hard
The hard AI implements a type of minimax algorithm that attempts to maximize the end-game tiles of the computer while minimizing the end game tiles of the player. It accomplishes this by implementing a mutally recursive algorithm that examines all possible game boards produced by all possible legal moves to a pre-determined recursive-depth that is set based on available computation time. At each level of recursion, the algorithm selects a 'best move' based on several criteria further detailed in ai.txt 
            
After the existence of each condition is identified, the legal move's associated move_value attribute is adjusted accordingly based on floating point values assigned to each condition. These values subsequently adjust the overall move_value attribute of the legal move. The legal move is then compared with every other legal move that exists at that respective recursion depth and the 'best move' is returned. The best legal move is then compared to the other best legal moves at a higher recursion depth where the best_move variable is further calibrated. Once the recursion is complete, a final best_move is returned and executed by the computer AI.
