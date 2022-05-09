from os import system

PLAYER_1 = "alphabeta"
PLAYER_2 = "random"
NUM_TESTS = 100

print("-------------------------------- PLAYER MODES -----------------------------------------")
print("Player 1:", PLAYER_1)
print("Player 2:", PLAYER_2)
print("------------------------------------------------------------------------------------")
command = "python outcome_only.py " + PLAYER_1 + " " + PLAYER_2

for i in range(10):
    print("Run", i+1, "/", NUM_TESTS, ":")
    system(command)
