import sys
from random import choice
import time

MAX_UTILITY = 49
MIN_UTILITY = -149
TERMINATION_STEPS = 6  # Depth of MiniMax and AlphaBeta Search


# Checks if game is over
# Input: Game State
# Output: 0 - Game not over; 1 - Player 1 Wins; 2 - Player 2 Wins; 3 - Game Tied
def is_game_over(mancalaList):
    sideOne = 0
    sideTwo = 0
    for j in range(6):
        sideOne = int(sideOne) + int(mancalaList[j])
        sideTwo = int(sideTwo) + int(mancalaList[j + 7])

    if int(sideOne) == 0 or int(sideTwo) == 0:
        mancalaList[6] = int(mancalaList[6]) + int(sideOne)
        mancalaList[13] = int(mancalaList[13]) + int(sideTwo)
        for k in range(6):
            mancalaList[k] = 0
            mancalaList[k + 7] = 0

        if int(mancalaList[13]) < int(mancalaList[6]):
            return 1
        elif int(mancalaList[13]) > int(mancalaList[6]):
            return 2
        else:
            return 3

    else:
        return 0


# Returns the utility of a player, by determining how good likely is he/she/it to win the Game
# Input: Game State, Player Number (1 or 2)
# Output: Utility Value (higher the value, the more likely to win)
def utility(state, player):
    if player == 1:
        score = int(state[6]) - int(state[13])
        if max(state[0:6]) == 0:
            endscore = score - sum(state[7:13])
            if endscore < 0:
                return -100 + endscore
            elif endscore == 0:
                return -50 + endscore
            elif endscore > 0:
                return 100 + endscore
        return score
    elif player == 2:
        score = int(state[13]) - int(state[6])
        if max(state[7:13]) == 0:
            endscore = score - sum(state[0:6])
            if endscore < 0:
                return -100 + endscore
            elif endscore == 0:
                return -50 + endscore
            elif endscore > 0:
                return 100 + endscore
        return score


# A recurring function which returns the all the possible actions a player has in a given state
# Input: Game State, Player Number (1 or 2)
# Output: List of List of possible actions
def valid_actions(mancalaList, player, recurring=False):
    action = []
    if player == 1:
        for i in range(6):
            binAmount = int(mancalaList[i])
            # Bonus move case
            if i + binAmount == 6:
                action += [[i] + x for x in valid_actions(perform_action(mancalaList, [i]), 1, True)]
            elif binAmount != 0:
                action.append([i])
    elif player == 2:
        for i in range(7, 13):
            binAmount = int(mancalaList[i])
            # Bonus move case
            if i + binAmount == 13:
                action += [[i] + x for x in valid_actions(perform_action(mancalaList, [i]), 2, True)]
            elif binAmount != 0:
                action.append([i])
    if recurring:
        if len(action) == 0:
            action.append([])
    return action


# Runs the given actions on the given state
# Input: Game State (list), Actions (list)
# Output: New State (list)
def perform_action(state, moves):
    firstPlayer = True if int(moves[0]) < 6 else False

    takePit = -1
    finalPit = -1
    mancalaList = state[:]

    for move in moves:

        if int(move) >= 0:
            takePit = mancalaList[move]
            mancalaList[move] = 0
        # firstPlayer = not(firstPlayer)

        recipient = move + 1

        while int(takePit) > 0:
            if firstPlayer and int(recipient) == 13:
                recipient = 0
            if not firstPlayer and int(recipient) == 6:
                recipient = 7
            mancalaList[recipient] = int(mancalaList[recipient]) + 1
            takePit = int(takePit) - 1
            # recipient =int(recipient) +1

            if int(takePit) == 0:
                finalPit = recipient
            else:
                recipient = int(recipient) + 1
                if int(recipient) > 13:
                    recipient = 0
        #  firstPlayer= not(firstPlayer)
        # display_state(mancalaList)
        if int(mancalaList[finalPit]) == 1:
            if int(mancalaList[12 - finalPit]) != 0:
                if firstPlayer and 0 <= int(finalPit) < 6:
                    mancalaList[6] += int(mancalaList[12 - int(finalPit)]) + 1
                    mancalaList[finalPit] = 0
                    mancalaList[12 - int(finalPit)] = 0
                elif not firstPlayer and 6 < int(finalPit) < 13:
                    mancalaList[13] += int(mancalaList[12 - int(finalPit)]) + 1
                    mancalaList[finalPit] = 0
                    mancalaList[12 - int(finalPit)] = 0

    return mancalaList


# Displays the state of the game in a graphical format
# Input: Game State
# Output: Prints the state on the Console Output Screen
def display_state(state):
    mancalaList = state[:]
    i = 0
    for element in mancalaList:

        mancalaList[i] = int(mancalaList[i])
        if int(mancalaList[i]) < 10:
            mancalaList[i] = " " + str(mancalaList[i])
        else:
            mancalaList[i] = str(mancalaList[i])
        i = i + 1

    # print("        a      b      c      d      e     f")

    print("+----+----+----+----+----+----+----+----+----+----+")
    print("|    |  " + mancalaList[12] + " |  " + mancalaList[11] + "  |" + mancalaList[10] + "    |" + mancalaList[
        9] + "    | " + mancalaList[8] + "   |  " + mancalaList[7] + " |    |")
    print("| " + mancalaList[13] + " |--------------+----+----+----+---------| " + mancalaList[6] + " |")
    print("|    |  " + mancalaList[0] + " |  " + mancalaList[1] + "  |" + mancalaList[2] + "    |" + mancalaList[
        3] + "    | " + mancalaList[4] + "   |  " + mancalaList[5] + " |    |")
    print("+----+----+----+----+----+----+----+----+----+----+")

    # print("        f      e      d      c      b     a")


def human_move(state, player):
    mancalaList = state[:]
    firstPlayer = True if player == 1 else False
    actions = []
    code = 0

    while True:
        repeat = False

        if firstPlayer and code == 0:
            print("PLAYER 1 TURN.")
        elif not firstPlayer and code == 0:
            print("PLAYER 2 TURN.")
        elif firstPlayer and code == -2:
            print("Invalid input. Try again, player 1")
        elif not firstPlayer and code == -2:
            print("Invalid input. Try again, player 2")
        elif firstPlayer and code == -1:
            print("Invalid input. Try again, player 2")
        elif not firstPlayer and code == -1:
            print(" DUDE SELECT ANOTHER MOVE ITS AN EMPTY BIN ")

        code = 0

        mList = mancalaList[:]

        i = 0
        for element in mList:

            mList[i] = int(element)
            if int(element) < 10:
                mList[i] = " " + str(element)
            else:
                mList[i] = str(element)
            i = i + 1

        print("        a      b      c      d      e     f")

        print("+----+-----+------+------+------+------+-----+----+")
        print("|    |  " + mList[12] + " |  " + mList[11] + "  |" + mList[10] + "    |" + mList[
            9] + "    | " + mList[8] + "   |  " + mList[7] + " |    |")
        print("| " + mList[13] + " |-----+------+------+------+------+-----| " + mList[6] + " |")
        print("|    |  " + mList[0] + " |  " + mList[1] + "  |" + mList[2] + "    |" + mList[
            3] + "    | " + mList[4] + "   |  " + mList[5] + " |    |")
        print("+----+-----+------+------+------+------+-----+----+")

        print("        f      e      d      c      b     a")

        playerChoice = input("CHOOSE THE OPERATION (A,B,C,D,E,F) TO BE PERFORMED OR enter q to quit the game: ").lower()

        if playerChoice == "q":
            return None
        elif firstPlayer and playerChoice == "a":
            move = 5
        elif firstPlayer and playerChoice == "b":
            move = 4
        elif firstPlayer and playerChoice == "c":
            move = 3
        elif firstPlayer and playerChoice == "d":
            move = 2
        elif firstPlayer and playerChoice == "e":
            move = 1
        elif firstPlayer and playerChoice == "f":
            move = 0
        elif not firstPlayer and playerChoice == "a":
            move = 12
        elif not firstPlayer and playerChoice == "b":
            move = 11
        elif not firstPlayer and playerChoice == "c":
            move = 10
        elif not firstPlayer and playerChoice == "d":
            move = 9
        elif not firstPlayer and playerChoice == "e":
            move = 8
        elif not firstPlayer and playerChoice == "f":
            move = 7
        else:
            move = -1
            code = -2
            continue

        if int(move) >= 0:
            takePit = mancalaList[move]
            if int(takePit) <= 0:
                code = -1

        actions.append(move)

        if firstPlayer:
            if move + int(mancalaList[move]) == 6:
                repeat = True
        else:
            if move + int(mancalaList[move]) == 13:
                repeat = True

        if not repeat:
            break
        else:
            mancalaList = perform_action(mancalaList, [move])
            if firstPlayer:
                if max(mancalaList[0:6]) == 0:
                    break
            else:
                if max(mancalaList[7:13]) == 0:
                    break

    return actions

# Returns the starting state of the same
# Input: Nothing
# Output: Starting State (list)
def init_state():
    return [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]


# -------------------- MIN-MAX FUNCTIONS --------------------------

# Runs minimax Algorithm and returns the best actions for a player for the given state
# Input: Game State, Player (1 or 2)
# Output: Best Action (according to minimax)
def minimax_decision(state, player):
    max_v = MIN_UTILITY
    best_action = None
    opponent = 2 if player == 1 else 1
    for a in valid_actions(state, player):
        v = min_value(perform_action(state, a), opponent, TERMINATION_STEPS - 1, player)
        if v > max_v:
            max_v = v
            best_action = a
    return best_action


# Max Value function of the minimax Algorithm
def max_value(state, player, term_steps, util_player):
    if is_game_over(state) > 0 or term_steps == 0:
        return utility(state, util_player)
    term_steps -= 1
    v = MIN_UTILITY
    opponent = 2 if player == 1 else 1
    for a in valid_actions(state, player):
        v = max(v, min_value(perform_action(state, a), opponent, term_steps, util_player))
    return v


# Min Value function of the minimax Algorithm
def min_value(state, player, term_steps, util_player):
    if is_game_over(state) > 0 or term_steps == 0:
        return utility(state, util_player)
    term_steps -= 1
    v = MAX_UTILITY
    opponent = 2 if player == 1 else 1
    for a in valid_actions(state, player):
        v = min(v, max_value(perform_action(state, a), opponent, term_steps, util_player))
    return v


# -----------------------------------------------------------------

# -------------- MIN-MAX FUNCTIONS (Alpha-Beta) -------------------

# Runs Alpha-Beta pruning Algorithm and returns the best actions for a player for the given state
# Input: Game State, Player (1 or 2)
# Output: Best Action (according to minimax/Alpha-Beta)
def alpha_beta_search(state, player):
    max_v = MIN_UTILITY
    best_action = None
    opponent = 2 if player == 1 else 1

    alpha = MIN_UTILITY
    beta = MAX_UTILITY

    for a in valid_actions(state, player):
        v = min_value_AB(perform_action(state, a), opponent, TERMINATION_STEPS - 1, player, alpha, beta)
        if v > max_v:
            max_v = v
            best_action = a
            alpha = max(alpha, v)
        if v >= beta:
            return best_action
    return best_action


# Max Value function of the AlphaBeta pruning Algorithm
def max_value_AB(state, player, term_steps, util_player, alpha, beta):
    if is_game_over(state) > 0 or term_steps == 0:
        return utility(state, util_player)
    term_steps -= 1
    v = MIN_UTILITY
    opponent = 2 if player == 1 else 1
    for a in valid_actions(state, player):
        v = max(v, min_value_AB(perform_action(state, a), opponent, term_steps, util_player, alpha, beta))
        alpha = max(alpha, v)
        if v >= beta:
            return v
    return v


# Mix Value function of the AlphaBeta pruning Algorithm
def min_value_AB(state, player, term_steps, util_player, alpha, beta):
    if is_game_over(state) > 0 or term_steps == 0:
        return utility(state, util_player)
    term_steps -= 1
    v = MAX_UTILITY
    opponent = 2 if player == 1 else 1
    for a in valid_actions(state, player):
        v = min(v, max_value_AB(perform_action(state, a), opponent, term_steps, util_player, alpha, beta))
        beta = min(beta, v)
        if v <= alpha:
            return v
    return v


# -----------------------------------------------------------------

# --------------------------- RANDOM ------------------------------

# Returns a random action for the given state
def random_move(state, player):
    return choice(valid_actions(state, player))


# -----------------------------------------------------------------

# Displays the Win/Loose/Tie States of the Players
def display_game_over(game_outcome):
    print("************************************************************************************")
    if game_outcome == 1 or game_outcome == 2:
        print(f"GAME OVER. PLAYER {game_outcome} WINS!!")
    elif game_outcome == 3:
        print(f"GAME OVER. MATCH TIED!!")
    print("************************************************************************************")


# -------------- MAIN PLAY LOOP -------------------

player1 = "minimax"
player2 = "human"

if len(sys.argv) == 3:
    player1 = sys.argv[1]
    player2 = sys.argv[2]

print("-------------------------------- GAME MODE -----------------------------------------")
print("Player 1:", player1)
print("Player 2:", player2)
print("------------------------------------------------------------------------------------")

state = init_state()

print("Initial State:")
display_state(state)

start_time = time.time()
step_count = 0
while True:
    step_count += 1
    print("------------------------------------------------------------------------------------")
    print("STEP:", step_count)
    print("------------------------------------------------------------------------------------")

    if player1 == "minimax":
        action = minimax_decision(state, 1)
    elif player1 == "alphabeta":
        action = alpha_beta_search(state, 1)
    elif player1 == "random":
        action = random_move(state, 1)
    elif player1 == "human":
        action = human_move(state, 1)
        if action is None:
            break

    print(f"Player 1 ({player1}) Chosen Action: {action}")
    state = perform_action(state, action)

    # DISPLAY THE NEW STATE HERE
    display_state(state)

    game_over = is_game_over(state)
    if game_over > 0:
        display_game_over(game_over)
        break

    if player2 == "minimax":
        action = minimax_decision(state, 2)
    elif player2 == "alphabeta":
        action = alpha_beta_search(state, 2)
    elif player2 == "random":
        action = random_move(state, 2)
    elif player2 == "human":
        action = human_move(state, 2)
        if action is None:
            break

    print(f"Player 2 ({player2}) Chosen Action: {action}")
    state = perform_action(state, action)

    # DISPLAY THE NEW STATE HERE
    display_state(state)

    game_over = is_game_over(state)
    if game_over > 0:
        display_game_over(game_over)
        break

time_taken = time.time() - start_time
print("Total Time Taken:", time_taken, "seconds")
print("Average time per step:", time_taken / step_count, "seconds")
