import copy
import random

dx = [1, 1, 1, 0]
dy = [1, 0, -1, 1]


class Board(object):
    DEFAULT_WIDTH = 7
    DEFAULT_HEIGHT = 6

    def __init__(self, board=None, height=None, width=None, last_move=[None, None]):
        if board is not None and (height is not None or width is not None):
            raise RuntimeError('Cannot specify both a board and a board size value')

        self.board = board if board is not None else self._empty_board(height, width)
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

    def valid_moves(self):
        """
        Returns: A generator of all valid moves in the current board state
        """
        for col in self.width:
            for row in self.height:
                if self.valid_move(row, col):
                    yield (row, col)

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

    def _empty_board(self, height, width):
        if height is None:
            height = self.DEFAULT_HEIGHT
        if width is None:
            width = self.DEFAULT_WIDTH

        if height <= 0 or width <= 0:
            raise ValueError('height or width of board cannot be less than 1')

        board = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            board.append(row)
        return board

    def winner(self):
        """
        Takes the board as input and determines if there is a winner.
        If the game has a winner, it returns the player number (Player One = 1, Player Two = -1).
        If the game is still ongoing, it returns zero.
        """
        row_winner = self._check_rows()
        if row_winner:
            return row_winner
        col_winner = self._check_columns()
        if col_winner:
            return col_winner
        diag_winner = self._check_diagonals()
        if diag_winner:
            return diag_winner
        return 0  # no winner yet

    def _check_rows(self):
        for row in self.board:
            same_count = 1
            curr = row[0]
            for i in range(1, self.width):
                if row[i] == curr:
                    same_count += 1
                    if same_count == 4 and curr != 0:
                        return curr
                else:
                    same_count = 1
                    curr = row[i]
        return 0

    def _check_columns(self):
        for i in range(self.width):
            same_count = 1
            curr = self.board[0][i]
            for j in range(1, self.height):
                if self.board[j][i] == curr:
                    same_count += 1
                    if same_count == 4 and curr != 0:
                        return curr
                else:
                    same_count = 1
                    curr = self.board[j][i]
        return 0

    def _check_diagonals(self):
        boards = [
            self.board,
            [row[::-1] for row in copy.deepcopy(self.board)]
        ]

        for b in boards:
            for i in range(self.width - 4 + 1):
                for j in range(self.height - 4 + 1):
                    if i > 0 and j > 0:  # would be a redundant diagonal
                        continue

                    # (j, i) is start of diagonal
                    same_count = 1
                    curr = b[j][i]
                    k, m = j + 1, i + 1
                    while k < self.height and m < self.width:
                            if b[k][m] == curr:
                                same_count += 1
                                if same_count is 4 and curr != 0:
                                    return curr
                            else:
                                same_count = 1
                                curr = b[k][m]
                            k += 1
                            m += 1
        return 0
