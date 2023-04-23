# Unscramble-A-Word-Game
This a puzzle game that requires the player to use a number of simple moves to reconstruct a scrambled word.

Game Mechanics

In the game, the player is presented with the scrambled version of a
string. The original string has been scrambled by first splitting it into a
number of sections, each with the same length, and then rearranging
each section in a random fashion. The player's objective
is to unscramble the word using as few moves as they can. The player
has three moves available: Swap, Shift, and Check. The moves can
only be applied to the string one section at a time.

The sections in the string are numbered 1 to N, where N is the number
of sections. The section length is fixed for the game, and each section
will have the same length. For example, given the string 'treerocklake'
and a section length of 4, section 2 would be 'rock'.
The Shift move is a circular shift of the string to the left, while the
Swap move exchanges the positions of the first and last characters of
the string. 

The Check move is the only move that does not modify the game's
state. It is used to check if a given section is correctly arranged.
The game allows for 3 modes: Normal, Hint, and Test. The Normal
mode involves playing the game as we have described it above, while
Hint mode allows the player to receive hints on what sections and
moves to choose each round. Enabling Test mode causes the program
to reveal the final answer before the game begins.

Game play

When the game begins, the player is first asked to choose a game
mode. Then, the player is repeatedly asked to provide:
1. The section number of the section they want to manipulate/check.
2. The move they would like to apply to the selected section.
If the player is playing in Hint mode, they will be offered the chance to
get a hint for a section to choose, or to make a move on a particular
section. Getting a hint also counts towards the player's total number of
moves.

The game continues until the player has unscrambled the string. We
will use the phrase game state to refer to the current state of the
string the player is trying to unscramble. When the game is over, the
player's total number of moves is reported.
