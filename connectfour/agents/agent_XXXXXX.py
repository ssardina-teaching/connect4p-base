from connectfour.agents.agent import Agent


class AgentXXXXXX(Agent):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board):
        return self.find_best_move(board)

    def _find_best_move(self, board):
        """
        Returns the best move using MonteCarlo Tree Search
        """
        best_move = None

        for row, col in board.valid_moves():
            score = self._score_move(board, row, col)
            if not best_move or score > best_move[0]:
                best_move = max([(score, (row, col)), best_move], key=lambda x: x[0])

        return best_move[1]

    def _score_move(self, board, x, y):
        winner = board.winner()
        if winner == self.id:
            return 1
        elif winner != 0:  # other player won
            return -1
        else:
            return (
                self._super_cool_Xheuristic_a(board, x, y) +
                self._super_cool_Xheuristic_b(board, x, y)
            )

    def _super_cool_Xheuristic_a(self, board, x, y):
        raise NotImplementedError  # TODO: Depends on other stuff being implemented

    def _super_cool_Xheuristic_b(self, board, x, y):
        raise NotImplementedError  # TODO: Depends on other stuff being implemented
