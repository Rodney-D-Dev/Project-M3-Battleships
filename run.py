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
    helper function to randomise cords for computer
    """
    x = randint(0, board.size -1)
    y = randint(0, board.size -1)
    return (x,y)

def valid_coordinates():
    pass

def populate_board():
    pass

def make_guess():
    pass

def play_game():
    pass
