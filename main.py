# Creates the starting board in a list
Board = []  # Starting Board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for place in range(9):
    Board.append(place)

User = "x"
Ai = "o"


# Prints the board
def draw_board(board: list):
    board = board
    print(f"  {board[0]} ║ {board[1]} ║ {board[2]}")
    print(f"════╬═══╬════")
    print(f"  {board[3]} ║ {board[4]} ║ {board[5]}")
    print(f"════╬═══╬════")
    print(f"  {board[6]} ║ {board[7]} ║ {board[8]}")


# Returns True if the user's input is a single digit
def is_valid_input(input_: str):
    return len(input_) == 1 and input_.isnumeric()


# Returns True if the given player has won on the given board
def is_win(player, current_board: list):
    for i in range(3):

        # Checks the rows
        j = i * 3
        if len([i for i in [current_board[j], current_board[j + 1], current_board[j + 2]] if i == player]) == 3:
            return True

        # Checks the columns
        if len([i for i in [current_board[i], current_board[i + 3], current_board[i + 6]] if i == player]) == 3:
            return True

    # Checks the top left diagonal
    if len([i for i in [current_board[0], current_board[4], current_board[8]] if i == player]) == 3:
        return True

    # Checks the top right diagonal
    if len([i for i in [current_board[2], current_board[4], current_board[6]] if i == player]) == 3:
        return True


# Returns True if the given board is a Draw
def is_draw(current_board):
    return not [i for i in current_board if isinstance(i, int)]


# For the given board, return:
#   -1 if the User has won,
#   1 if the Ai has won,
#   0 if there is a draw
#   if none of the above apply, returns None
def board_evaluation(board_):
    if is_win(User, board_):
        return -1
    if is_win(Ai, board_):
        return 1
    if is_draw(board_):
        return 0


# Returns a list of the empty spots of a given board
def empty_spots(board_):
    possible_plays_ = []
    for i in board_:
        if isinstance(i, int):
            possible_plays_.append(i)
    return possible_plays_


# Returns a list of the boards obtained for every possible moves of a given player on a given board
def possible_boards(board_: list, player) -> list:
    tree = []
    for i in empty_spots(board_):
        new_board = board_.copy()
        new_board[i] = player
        tree.append(new_board)
    return tree


# Recursively checks a given board possible boards until it reaches a win or a draw and returns the best move for the Ai
# For more information on the minimax algorithm, search for "Minimax algorithm" on Internet
def minimax(board_, player_=Ai):
    if board_evaluation(board_) is None:
        if player_ == User:
            pos_bo = possible_boards(board_, player_)
            tic = [minimax(i, Ai) for i in pos_bo]
            best_outcome = min([i[0] for i in tic])
            return [[i[0], pos_bo[tic.index(i)]] for i in tic if i[0] == best_outcome][0]
        elif player_ == Ai:
            pos_bo = possible_boards(board_, player_)
            tic = [minimax(i, User) for i in pos_bo]
            best_outcome = max([i[0] for i in tic])
            return [[i[0], pos_bo[tic.index(i)]] for i in tic if i[0] == best_outcome][0]
    else:
        return [board_evaluation(board_), board_]


# Game Main Loop
while True:
    draw_board(Board)

    # User's Turn
    spot = input(f"Enter a spot number to place your {User}:")  # Ask for User input

    if not is_valid_input(spot):
        print(f"Your input most be one of the following digit: {[i for i in Board if isinstance(i, int)]}")
        continue
    if int(spot) not in Board:
        print(f"Your input most be one of the following digit: {[i for i in Board if isinstance(i, int)]}")

        continue

    # Inserts the User move in the Board
    Board.pop(int(spot))
    Board.insert(int(spot), User)

    if is_win(User, Board):
        print(f"{User} player won!")
        draw_board(Board)
        break

    if is_draw(Board):
        print("Draw")
        draw_board(Board)
        break

    # Ai's Turn
    Board = minimax(Board)[1]

    if is_win(User, Board):
        print(f"{User} player won!")
        draw_board(Board)
        break

    if is_draw(Board):
        print("Draw")
        draw_board(Board)
        break
