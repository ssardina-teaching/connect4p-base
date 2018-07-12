import argparse

from connectfour.gui import start_game
from connectfour.board import Board
from connectfour.agents.computer_player import MonteCarloAgent, RandomAgent
from connectfour.agents.agent_XXXXXX import AgentXXXXXX
from connectfour.agents.agent import HumanPlayer

MAX_GAME_WIDTH = MAX_GAME_HEIGHT = 100
MIN_GAME_WIDTH = MIN_GAME_HEIGHT = 4

PLAYER_TYPE_MAP = {
    'HumanPlayer': HumanPlayer,
    'RandomAgent': RandomAgent,
    'MonteCarloAgent': MonteCarloAgent,
    'AgentXXXXXX': AgentXXXXXX
}


class Game:
    """
    Manages the players of the Game
    """

    PLAYER_ONE_ID = 1
    PLAYER_TWO_ID = 2

    def __init__(self, player_one, player_two, board_height, board_width, fast_play=False):
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = self.player_one
        self.player_one.id = self.PLAYER_ONE_ID
        self.player_two.id = self.PLAYER_TWO_ID
        self.board = Board(height=board_height, width=board_width)
        self.fast_play = fast_play

    def change_turn(self):
        if self.current_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one

    def reset(self):
        self.board = Board(height=self.board.height, width=self.board.width)
        self.current_player = self.player_one


def main():
    parser = argparse.ArgumentParser(description="Set up the game.")
    parser.add_argument(
        "--player-one",
        dest="player_one",
        action="store",
        default="HumanPlayer",
        help="Set the agent for player one of the game",
    )
    parser.add_argument(
        "--player-two",
        dest="player_two",
        action="store",
        default="HumanPlayer",
        help="Set the agent for player two of the game",
    )
    parser.add_argument(
        "--board-height",
        dest="board_height",
        action="store",
        default=None,
        type=int,
        choices=range(MIN_GAME_HEIGHT, MAX_GAME_HEIGHT),
        metavar="[{}-{}]".format(MIN_GAME_HEIGHT, MAX_GAME_HEIGHT),
        help="Set the number of rows in the board",
    )
    parser.add_argument(
        "--board-width",
        dest="board_width",
        action="store",
        default=None,
        type=int,
        choices=range(MIN_GAME_WIDTH, MAX_GAME_WIDTH),
        metavar="[{}-{}]".format(MIN_GAME_WIDTH, MAX_GAME_WIDTH),
        help="Set the number of columns in the board",
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="disables the delay between computer moves, making the game much faster.",
    )

    args = parser.parse_args()

    if args.player_one not in PLAYER_TYPE_MAP:
        raise RuntimeError("'{}' is not a valid player type".format(args.player_one))
    else:
        player_one = PLAYER_TYPE_MAP[args.player_one]("Player 1")

    if args.player_two not in PLAYER_TYPE_MAP:
        raise RuntimeError("'{}' is not a valid player type".format(args.player_two))
    else:
        player_two = PLAYER_TYPE_MAP[args.player_two]("Player 2")

    g = Game(
        player_one,
        player_two,
        args.board_height,
        args.board_width,
        args.fast,
    )
    start_game(g)


if __name__ == "__main__":
    main()
