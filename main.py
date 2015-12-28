"""File to play the tic tac toe game."""

#Class definition for board.

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
        if tuple(position) in self.board.keys():
            self.board[tuple(position)] = mark
            return True
        print "Enter a valid position."
        return False
    
    def game_is_done(self):
        """Check if the game is done and return True or False."""
        #game ends when all rows/columns/diagnols have same mark. or if the 
        #board is full
        #Check for each column
        for col in list("ABC"):
            marks = []
            for row in list("123"):
                if self.board[(col, row)]:
                    marks.append(self.board[(col, row)])
            if len(set(marks)) == 1 and len(marks) == 3:
                return True
        for row in list("123"):
            marks = []
            for col in list("ABC"):
                if self.board[(col, row)]:
                    marks.append(self.board[(col, row)])
            if len(set(marks)) == 1 and len(marks) == 3:
                return True
        if self.board[("A","1")] == self.board[("B", "2")] and \
        self.board[("B", "2")] == self.board[("C", "3")] and \
        self.board[("B", "2")]:
            return True
        if self.board[("A","3")] == self.board[("B", "2")] and \
        self.board[("B", "2")] == self.board[("C", "1")] and \
        self.board[("B", "2")]:
            return True
        return False
        
class Player(object):
    def __init__(self, mark):
        """Initialize the player object"""
        self.mark = mark
    
    def get_input(self, board):
        """Get the player input and check if the move is valid"""
        while True:
            position = raw_input("Enter the position: ")
            if self.valid_move(position, board):
                board.set_mark(self.mark, position)
                break
            print "Please enter a valid position."
           
    def valid_move(self, position, board):
        if tuple(position) in board.empty_slots:
            return True
        return False

def main():
    
    p1 = Player("X")
    b = Board()
    print b.empty_slots
    p1.get_input(b)
    
    b.display_board()
    p1.get_input(b)


    print b.empty_slots
    b.display_board()
    
    print b.game_is_done()

main()