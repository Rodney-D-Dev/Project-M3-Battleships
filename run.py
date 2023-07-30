from random import randint

scores = {"Computer": 0, "Player": 0}


class Game_board:
    """
    Main Game board class. Sets board sise, number of ships,
    the players name and board type
    has methos for printing board, guesses,
    adding shhips and checking all ships have sunk.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.ships = []
        self.guesses = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "x"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit!"

        else:
            return "Miss!"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "Player":
                self.board[x][y] = "@"

    def all_ships_sunk(self):
        return all(ship in self.guesses for ship in self.ships)


def random_point(board):
    """
    helper function to randomise cords on the game board
    """
    x = randint(0, board.size - 1)
    y = randint(0, board.size - 1)
    return (x, y)


def populate_board(board):
    """
    function to place ships at random points on the board
    """
    while len(board.ships) < board.num_ships:
        x, y = random_point(board)
        board.add_ship(x, y)


def valid_coordinates(board, row, col):
    """
    function to check if coordinates are within the game board
    and have not been already guessed.
    """
    if (row, col) not in board.guesses:
        global result
        result = board.guess(row, col)
        if result == "Hit!":
            print(result)
            return True
        else:
            print(result)
            return False
    elif (row, col) in board.guesses:
        print(f"You have alredy guessed {row} and {col}!")
        make_guess(board)
    return result


def make_guess(board):
    """
    function to guess ship coords if the board
    is a computer board asks for user input
    else picks random point on board
    """
    add_score = False

    if board.type == "Computer":
        while True:
            try:
                row, col = int(input("Enter Row: ")), int(input("Enter Colum: "))
                if row > (board.size - 1) or col > (board.size - 1):
                    raise ValueError
                break
            except ValueError:
                print(f"Invalid Input. Please enter number in the rage of 0 to {board.size - 1}.")

    elif board.type == "Player":
        row, col = random_point(board)
    if valid_coordinates(board, row, col):
        add_score = True
    return add_score


def play_game(computer_board, player_board):
    """
    function to handle game flow or loop handles playing turn
    and prints info to show whats happening and
    handles win condition
    """
    while True:

        print(f"{player_board.name}'s Board")
        player_board.print()
        print("_" * 60)
        print(f"{computer_board.name}'s Board")
        computer_board.print()

        print(f"{player_board.name}'s turn")
        print("_" * 60)
        if make_guess(computer_board):
            scores["Player"] += 1
        if computer_board.all_ships_sunk():
            print(f"{player_board.name} Wins!!")
            print("Final Scores:")
            print("Player:", scores["Player"], "Computer:", scores["Computer"])
            game_start()

        print("_" * 60)
        print(f"{computer_board.name}'s turn")
        print("_" * 60)
        if make_guess(player_board):
            scores["Computer"] += 1
        if player_board.all_ships_sunk():
            print(f"{computer_board.name} Wins!!")
            print("Final Scores:")
            print("Player:", scores["Player"], "Computer:", scores["Computer"])
            game_start()

        print("_" * 60)
        print("Scores:")
        print(f"{player_board.name}", scores["Player"])
        print(f"{computer_board.name}", scores["Computer"])


def game_start():
    """
    function to handle game setup and start game with welcome message.
    """
    size = 5
    num_ships = 3
    scores["computer"] = 0
    scores["player"] = 0
    print("_" * 60)
    print("Welcome to BattleShips")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("_" * 60)
    player_name = input("Please enter your name:\n")
    print("_" * 60)

    computer_board = Game_board(size, num_ships, "Computer", type="Computer")
    player_board = Game_board(size, num_ships, player_name, type="Player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    play_game(computer_board, player_board)


game_start()
