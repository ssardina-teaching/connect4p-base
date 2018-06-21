import argparse

from connectfour.gui import start_game
from connectfour.agents.computer_player import MonteCarloAgent, RandomAgent
from connectfour.agents.agent import HumanPlayer


class Game():
    """
    Manages the players of the Game
    """
    PLAYER_ONE_ID = -1
    PLAYER_TWO_ID = 1

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = self.player_one
        self.player_one.id = self.PLAYER_ONE_ID
        self.player_two.id = self.PLAYER_TWO_ID

    def change_turn(self):
        if self.current_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one


def main():
    parser = argparse.ArgumentParser(description='Set up the game.')
    parser.add_argument('--player-one', dest='player_one', action='store',
                        default='HumanPlayer',
                        help='Set the agent for player one of the game')

    parser.add_argument('--player-two', dest='player_two', action='store',
                        default='HumanPlayer',
                        help='Set the agent for player two of the game')

    args = parser.parse_args()

    if args.player_one == 'HumanPlayer':
        print("using default")
        player_one = HumanPlayer('Player 1')
    elif args.player_two == 'RandomAgent':
        player_one = RandomAgent('Player 1')
    else:
        player_one = MonteCarloAgent('Player 1')

    if args.player_two == 'HumanPlayer':
        player_two = HumanPlayer('Player 2')
    elif args.player_two == 'RandomAgent':
        player_two = RandomAgent('Player 2')
    else:
        player_two = MonteCarloAgent('Player 2')

    start_game(Game(player_one, player_two))


if __name__ == '__main__':
    main()
