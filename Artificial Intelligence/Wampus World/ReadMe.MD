Argument interactive specifies that the program runs in interactive mode.
Argument [input_file] specifies an input file that contains an initial board state. This way we can start the program from a non-empty board state. If the input file does not exist, the program should just create an empty board state and start again from there.
Argument [computer-first/human-first] specifies whether the computer should make the next move or the human.
Argument [depth] specifies the number of moves in advance that the computer should consider while searching for its next move. In other words, this argument specifies the depth of the search tree. Essentially, this argument will control the time takes for the computer to make a move.
After reading the input file, the program gets into the following loop:
If computer-next, goto 2, else goto 5.
Print the current board state and score. If the board is full, exit.
Choose and make the next move.
Save the current board state in a file called computer.txt (in same format as input file).
Print the current board state and score. If the board is full, exit.
Ask the human user to make a move (make sure that the move is valid, otherwise repeat request to the user).
Save the current board state in a file called human.txt (in same format as input file).
Goto 2.
