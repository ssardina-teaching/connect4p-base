import copy
import random

dx = [1, 1, 1, 0]
dy = [1, 0, -1, 1]


class Board(object):
    DEFAULT_WIDTH = 7
    DEFAULT_HEIGHT = 6

    def __init__(self, board=None, last_move=[None, None]):
        self.board = board if board is not None else self._empty_board()
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.last_move = last_move

    def tryMove(self, move):
        """
        Takes the current board and a possible move specified
        by the column. Returns the appropiate row where the
        piece will be located. If it's not found it returns -1.
        """
        if move < 0 or move >= self.width or self.board[0][move] != 0:
            return -1

        for i in range(len(self.board)):
            if self.board[i][move] != 0:
                return i - 1
        return len(self.board) - 1

    def validMove(self, row, col):
        """
        Take a row, col position on the board and returns whether
        that row value is the bottom-most empty position in the column.

        Args:
            row: int value for row position on Board
            col: int value for column position on Board

        Returns: True is move is valid. False, otherwise
        """
        return row >= 0 and self.tryMove(col) == row

    def terminal(self):
        """
        Returns true when the game is finished, otherwise false.
        """
        for i in range(len(self.board[0])):
            if self.board[0][i] == 0:
                return False
        return True

    def legal_moves(self):
        """
        Returns the full list of legal moves that for next player.
        """
        legal = []
        for i in range(len(self.board[0])):
            if self.board[0][i] == 0:
                legal.append(i)

        return legal

    def next_state(self, turn):
        aux = copy.deepcopy(self)
        moves = aux.legal_moves()
        if len(moves) > 0:
            ind = random.randint(0, len(moves) - 1)
            row = aux.tryMove(moves[ind])
            aux.board[row][moves[ind]] = turn
            aux.last_move = [row, moves[ind]]
        return aux

    def _empty_board(self):
        board = []
        for i in range(self.DEFAULT_HEIGHT):
            row = []
            for j in range(self.DEFAULT_WIDTH):
                row.append(0)
            board.append(row)
        return board

    def winner(self):
        """
        Takes the board as input and determines if there is a winner.
        If the game has a winner, it returns the player number (Player One = 1, Player Two = -1).
        If the game is still ongoing, it returns zero.
        """

        x = self.last_move[0]
        y = self.last_move[1]

        if x is None:
            return 0

        for d in range(4):

            h_counter = 0
            c_counter = 0

            u = x - 3 * dx[d]
            v = y - 3 * dy[d]

            for k in range(-3, 4):

                u = x + k * dx[d]
                v = y + k * dy[d]

                if u < 0 or u >= 6:
                    continue

                if v < 0 or v >= 7:
                    continue

                if self.board[u][v] == -1:
                    c_counter = 0
                    h_counter += 1
                elif self.board[u][v] == 1:
                    h_counter = 0
                    c_counter += 1
                else:
                    h_counter = 0
                    c_counter = 0

                if h_counter == 4:
                    return -1

                if c_counter == 4:
                    return 1

        return 0
