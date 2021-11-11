startingBoard = []
for place in range(9):
    startingBoard.append(place)
currentBoard = startingBoard.copy()


def board():
    items = [item for item in currentBoard]
    print(f"  {items[0]} ║ {items[1]} ║ {items[2]}")
    print(f"════╬═══╬════")
    print(f"  {items[3]} ║ {items[4]} ║ {items[5]}")
    print(f"════╬═══╬════")
    print(f"  {items[6]} ║ {items[7]} ║ {items[8]}")


def is_valid_input(input_: str):
    return len(input_) == 1 and input_.isnumeric()


def is_win(player, current_board: list):
    for i in range(3):
        j = i * 3
        if len([i for i in [current_board[j], current_board[j + 1], current_board[j + 2]] if i == player]) == 3:
            return True
        if len([i for i in [current_board[i], current_board[i + 3], current_board[i + 6]] if i == player]) == 3:
            return True
    if len([i for i in [current_board[0], current_board[4], current_board[8]] if i == player]) == 3:
        return True
    if len([i for i in [current_board[2], current_board[4], current_board[6]] if i == player]) == 3:
        return True


def is_draw(current_board):
    return not [i for i in current_board if isinstance(i, int)]


def get_player(turn):
    if turn % 2:
        return "o"
    else:
        return "x"


def board_evaluation(board_):
    if is_win("x", board_):
        return -1
    if is_win("o", board_):
        return 1
    if is_draw(board_):
        return 0


def possible_boards(board_: list, player) -> list:
    tree = []
    for i in possible_plays(board_):
        new_board = board_.copy()
        new_board[i] = player
        tree.append(new_board)
    return tree


def minimax(board_, player_="o"):
    if board_evaluation(board_) is None:
        if player_ == "x":
            pos_bo = possible_boards(board_, player_)
            tic = [minimax(i, "o") for i in pos_bo]
            best_outcome = min([i[0] for i in tic])
            return [[i[0], pos_bo[tic.index(i)]] for i in tic if i[0] == best_outcome][0]
        elif player_ == "o":
            pos_bo = possible_boards(board_, player_)
            tic = [minimax(i, "x") for i in pos_bo]
            best_outcome = max([i[0] for i in tic])
            return [[i[0], pos_bo[tic.index(i)]] for i in tic if i[0] == best_outcome][0]
    else:
        return [board_evaluation(board_), board_]


def possible_plays(board_):
    possible_plays_ = []
    for i in board_:
        if isinstance(i, int):
            possible_plays_.append(i)
    return possible_plays_


TURN = 0
while True:
    Player = get_player(TURN)

    board()
    spot = input(f"Enter a spot number to place your {Player}:")

    if not is_valid_input(spot):
        continue
    if int(spot) not in currentBoard:
        continue

    currentBoard.pop(int(spot))
    currentBoard.insert(int(spot), Player)

    if is_win(Player, currentBoard):
        print(f"{Player} player won!")
        board()
        break

    if is_draw(currentBoard):
        print("Draw")
        board()
        break

    currentBoard = minimax(currentBoard)[1]

    if is_win(Player, currentBoard):
        print(f"{Player} player won!")
        board()
        break

    if is_draw(currentBoard):
        print("Draw")
        board()
        break
