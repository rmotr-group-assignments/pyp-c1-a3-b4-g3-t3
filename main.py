"""File to play the tic tac toe game."""

#Class definition for board.

import random

class Board(object):
    """Defintion for the board based on requirement, i.e columns as A, B, C and
    rows as 1, 2, 3."""
    def __init__(self):
        """Initialise the board."""
        self.board = {("A", "1") : None, ("B", "1") : None, ("C", "1") : None,
                      ("A", "2") : None, ("B", "2") : None, ("C", "2") : None,
                      ("A", "3") : None, ("B", "3") : None, ("C", "3") : None}

    @property    
    def empty_slots(self):
        """Return the empty slots as a list of tuples. Each tuple has the column
        and row."""
        #Check if issue because same name as method.
        empty_slots = []
        for key, val in self.board.iteritems():
            if not val:
                empty_slots.append(key)
        return empty_slots
    
    def display_board(self):
        """Display the board in the required format."""
        for row in ["1","2","3"]:
            for col in list("ABC"):
                print self.board[(col, row)], 
            print "\n"
    
    def set_mark(self, mark, position):
        """Set the mark on the board given the mark. The position is in the form
        of a string with column and row values."""
        #Ex: mark : A1, A3, B3
        #if tuple(position) in self.board.keys():
        self.board[tuple(position)] = mark
        #    return True
        #print "Enter a valid position."
        #return False
    
    def game_is_done(self):
        """Check if the game is done and return True or False."""
        #game ends when all rows/columns/diagnols have same mark
        #Check for each column
        for col in list("ABC"):
            marks = []
            for row in list("123"):
                if self.board[(col, row)]:
                    marks.append(self.board[(col, row)])
            if len(set(marks)) == 1 and len(marks) == 3:
                return True
        #Check for each row
        for row in list("123"):
            marks = []
            for col in list("ABC"):
                if self.board[(col, row)]:
                    marks.append(self.board[(col, row)])
            if len(set(marks)) == 1 and len(marks) == 3:
                return True
        #Check for diagnols
        if self.board[("A","1")] == self.board[("B", "2")] and \
        self.board[("B", "2")] == self.board[("C", "3")] and \
        self.board[("B", "2")]:
            return True
        if self.board[("A","3")] == self.board[("B", "2")] and \
        self.board[("B", "2")] == self.board[("C", "1")] and \
        self.board[("B", "2")]:
            return True
        return False
        
    def game_is_draw(self):
        """Check if the game has ended in a draw"""
        if len(self.empty_slots) == 0:
            return True
        return False
        
        
class Player(object):
    def __init__(self, mark):
        """Initialize the player object"""
        self.mark = mark
    
    def get_move(self, board):
        """Get the player input and check if the move is valid"""
        while True:
            position = raw_input("It's player {}'s turn, Enter the position: ".format(self.mark))
            if self.valid_move(position, board):
                board.set_mark(self.mark, position)
                #if len(board.empty_slots) > 0:
                #    print "Player {0} won the game.".format(self.mark)
                break
            print "Please enter a valid position."
           
    def valid_move(self, position, board):
        if tuple(position) in board.empty_slots:
            return True
        return False


def tic_tac_toe_engine():
    """The function which runs the game."""
    b = Board()
    p1 = Player("X")
    p2 = Player("O")
    
    print "Please pick the marks either X or O."
    
    players = [p1, p2]
    random.shuffle(players)
    print "The player with {0} mark, starts the game.".format(players[0].mark)
    count  = 0
    while True: #not b.game_is_done():
        curr_player = players[(count % 2)]
        curr_player.get_move(b)
        if b.game_is_done():
            print "Player {} has won the game".format(curr_player.mark)
            break
        if b.game_is_draw():
            print "The game has ended in a draw"
            break
        b.display_board()
        count += 1
        
    
def main():
    """
    p1 = Player("X")
    b = Board()
    print b.empty_slots
    p1.get_move(b)
    
    b.display_board()
    p1.get_move(b)


    print b.empty_slots
    b.display_board()
    
    print b.game_is_done()
    """
    tic_tac_toe_engine()
    
    
main()