from connectfour.agents.agent import Agent


class AgentXXXXXX(Agent):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board):
        return self._find_best_move(board)

    def _find_best_move(self, board):
        """
        Selects which column to place a token in by evaluating the score
        of each (x, y) move.
        """
        best_move = None

        for row, col in board.valid_moves():
            score = self._score_move(board, row, col)
            if not best_move:
                best_move = (score, (row, col))
            else:
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

    def _get_max_board(self, board):
        """
        Loop throuth the board to get the max line numbers
        """
        max_ = i = j = 0
        for i in range(board.width):
            for j in range(board.height):
                line = board.winning_zones[i][j]
                for num in line:
                    max_ = max(num, max_)
        return max_

    def _super_cool_Xheuristic_a(self, board, x, y):
        i = score = max_ = 0
        max_ = self._get_max_board(board)
        other = 2 if self.id is 1 else 2

        for i in range(max_):
            # if enemy has 2 and we have 0 in the same line.*/
            if (
                (board.score_array[other-1][i] == board.num_to_connect-2) and
                (board.score_array[self.id-1][i] == 0)
            ):
                score -= 4
            elif (
                (board.score_array[other-1][i] == board.num_to_connect-1) and
                (board.score_array[self.id-1][i] == 0)
            ):
                score -= 10
            elif (
                (board.score_array[other-1][i] == board.num_to_connect-3) and
                (board.score_array[self.id-1][i] == 0)
            ):
                score -= 1
        return score / max_

    def _super_cool_Xheuristic_b(self, board, x, y):
        i = score = 0
        max_ = self._get_max_board(board)
        other = 2 if self.id is 1 else 2
        for i in range(max_):
            # if we have 2 and enemy have 0 in the same line.*/
            if(
                (board.score_array[self.id-1][i] == 2) and
                (board.score_array[other-1][i] == 0)
            ):
                score += 3
            elif (
                (board.score_array[self.id-1][i] == 3) and
                (board.score_array[other-1][i] == 0)
            ):
                score += 8
            elif (
                (board.score_array[self.id-1][i] == 1) and
                (board.score_array[other-1][i] == 0)
            ):
                score += 1

        return score / max_
