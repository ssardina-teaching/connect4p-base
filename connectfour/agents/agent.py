class Agent():
    def __init__(self, name):
        self.name = name

    def get_move(board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """
        # TODO: an agent should return a move, not a whole new board
        raise NotImplementedError

    def __repr__(self):
        return self.name


class HumanPlayer():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
