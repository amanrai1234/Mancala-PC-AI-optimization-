UPDATE - WITH INCLUDED WINNING RATE (12/4/2021):

- We have included the winning rate of our algorithms in our new Report, which was 100% agains random choices and very good against humans.
- We have also created 2 new files called test.py & outcome_only.py, where outcome_only.py isjust another copy of play.py, but with all the print statements, except the end result of the game commented out.
- After extracting all the files in the .zip file to the same folder, either the play.py file can be run directly, or test.py file can be run for running a player configuration for more than one time.

Instruction for running the newly added test.py file:
- This test.py file can be used only for configuration that does not involve a human player (as it will only print the winner/outcome of each game).
- You can modify the PLAYER_1 & PLAYER_2 global variable to one of the following string values: "random" , "minimax" , "alphabeta"
- Finally the number of required tests can be set by modifying the NUM_TESTS global varaible and the file can be run.

THE FOLLOWING ARE THE README INSTRUCTIONS THAT WERE PRESENT IN THE LAST SUBMISSION:

Software Requirement:
The project is expected to run with any version of Python. It is fully tested with all the edge cases using Python 3.7

The entire project is containined in the 1 file in this folder, "play.py".

Procedure to run the code:
1) Open a terminal window.
2) Change directory to the directory containing the "play.py" file.
3) In order to run the default case of Player 1 being minimax Algorithm and Player 2 being a human, simply run the "python play.py" command and follow the directions.
4) In order to try out all/any of the 16 combinations, run the command "python play.py player1 player2" (do not type player1 or player2, instead replace them with below values)
		where the player1, player2 parameters can take any of the following 4 values,
											human
											random
											minimax
											alphabeta
Example Command: python play.py alphabeta random

Additional Note: The value of "TERMINATION_STEPS" global variable in the top of the "play.py" file can be altered to adjust the Depth of the minimax and alphabeta Search. It's value (depth) is to 5 by default.


Author Details:

Name: Babu Aman Rai Saxena
UR NetID: bsaxena@ur.rochester.edu
UR Student ID: 32103519

Name: Deepak Subramani Velumani
UR NetID: dsubrama@ur.rochester.edu
UR Student ID: 32132007