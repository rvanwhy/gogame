class Board:
    def __init__(self, n):
        ""
        self.board = list()
        self.dimension = n

        for i in range(n*n):
            self.board.append('.')

    def white_plays(self, i, j):
        """Places a white piece at space i,j

        Takes in the coordnates of the piece in matrix coordinates.
        Places a white stone at the position asked.

        Args:
          i: the row in which to place the stone
          j: the column in which to place the stone
        """
        self._place('W', i, j)

    def black_plays(self, i, j):
        """Places a white piece at space i,j

        Takes in the coordnates of the piece in matrix coordinates.
       Places a white stone at the position asked.

        Args:
          i: the row in which to place the stone
          j: the column in which to place the stone
        """

        self._place('B', i, j)
        

    def _place(self, symbol, i, j):
        """Places "symbol" at space i,j

        For internal use only. Although this can be used for 
        debugging purposes. i,j are matrix coordinates.

        Args:
          symbol: the symbol to place
          i: the row in which to place it
          j: the column in which to place it
        """

        self.board[i*self.dimension + j] = symbol
    
    def _evaluate_captures(self):
        """TODO: make this an actual go board
        """
        pass

    def display_board(self):
        """Displays the go board.

        Pretty Prints the go board. Can be used if game 
        is played via command line. For external application use
        use the serial version Board.board
        """
        print(self)

    def __str__(self):
        output = ""

        for num, stone in enumerate(self.board):
            if num != 0 and num % self.dimension == 0:
                output += '\n'

            output += stone + ' '

        output += '\n'

        return output
