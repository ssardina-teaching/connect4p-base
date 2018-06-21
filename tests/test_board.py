from connectfour.board import Board


class TestBoard:
    def test_try_move_on_valid_column(self):
        board = Board()

        for i in range(board.width):
            col = board.tryMove(i)
            # expected position is bottom of board
            assert col == board.height - 1

    def test_try_move_on_invalid_column(self):
        board = Board()
        column_to_fill = 1

        for i in range(board.height):
            board.board[i][column_to_fill] = 1

        # Placement in column should now fail
        assert board.tryMove(column_to_fill) == -1
        # Other columns should still be valid
        assert board.tryMove(column_to_fill + 1) >= 0

    def test_valid_move_on_valid_move(self):
        board = Board()

        col = 2
        # at start, a peice should be placed on the bottom
        assert board.validMove(board.height - 1, col)
        assert not board.validMove(board.height - 2, col)

    def test_terminal_on_finished_game(self):
        board = Board()

        # A connect four game is considered finished when all columns
        # are full. In the Board class, this is indicated by non-zero values
        # in the first row
        for i in range(board.width):
            board.board[0][i] = 1
        assert board.terminal()

    def test_terminal_on_unfinished_game(self):
        board = Board()
        assert not board.terminal()

        board.board[1][1] = 1
        assert not board.terminal()

    def test_legal_moves(self):
        board = Board()

        # fill rows 0, 3, and 5
        for i in range(board.height):
            board.board[i][0] = board.board[i][3] = board.board[i][5] = 1

        legal_columns = board.legal_moves()

        expected = [1, 2, 4, 6]
        for i, col in enumerate(legal_columns):
            assert expected[i] == col

    def test_winner(self):
        grid = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, -1],
            [1, 1, 1, 0, 0, 0, -1],
        ]

        board = Board(grid)
        # TODO: Currently winner check relies on knowing last move of game
        board.last_move = [3, 6]

        assert -1 == board.winner()
