from random import randint 

class Game_board:
    """
    Main Game board class. Sets board sise, number of ships, the players name and board type 
    has methos for printing board, guesses, adding shhips and checking all ships have sunk.
    """
    def __init__(self,size,num_ships,name,type):
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
        self.guesses.append((x,y))
        self.board[x][y] = "x"

        if(x,y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self,x,y, type = "computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x,y))
            if self.type == "player":
                self.board[x][y] = "@"
    def all_ships_sunk(self):
        return all(ship in self.guesses for ship in self.ships)
        
def random_point(board):
    """
    helper function to randomise cords on the game board
    """
    x = randint(0, board.size -1)
    y = randint(0, board.size -1)
    return (x,y)

def populate_board(board):
    """
    function to place ships at random points on the board 
    """
    while len(board.ships) < board.num_ships:
        x,y = random_point(board)
        board.add_ship(x,y)

def valid_coordinates(board,row,col):
    """
    function to check if coordinates are within the game board and have not been already guessed.
    """
    if (row,col) not in board.guesses:
        result = board.guess(row,col)
        print(result)

def make_guess(board):
    """
    function to guess ship coords 
    """
    if board.type == "Computer":
        row,col = int(input("Enter Row: ")) , int(input("Enter Colum: ")) 
    valid_coordinates(board,row,col) 

def play_game(computer_board,player_board):
    """
    function to handle game flow or loop
    """
    while True:
        #player goes first
        print(f"{player_board.name}'s turn")
        make_guess(computer_board)
        if computer_board.all_ships_sunk():
            print(f"{player_board.name} Wins!!")
            break
        computer_board.print()
        #then computer
    
player_board = Game_board(5,9,"test101",type="Player")
computer_board = Game_board(5,10,"test101",type="Computer")
populate_board(player_board)
populate_board(computer_board)
play_game(computer_board,player_board)