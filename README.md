# RMIT AI - Connect4

<p align="center">
  <img src="https://github.com/Alfo5123/Connect4/blob/master/img/game_example.gif" width="350"/>  
</p>

## About The Game

Connect 4 is a two-player game in which the players take turns dropping colored discs from the top into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the next available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

## Game Basics - Configuration, CLI, GUI

### Run

1. `git clone https://github.com/thundergolfer/rmit-connectfour.git`
2. `cd rmit-connectfour`
3. `pipenv install && pipenv shell`
4. `python -m connectfour.game` (default configuration will be run)

### Configuration and CLI

Currently this game allows only for the specification of particular player types for each player. This is done with the `--player-one XXX` and `--player-two YYY` options. The currently available player types are:

* `HumanPlayer` - Player is controlled by user via GUI **[DEFAULT OPTION]**
* `RandomAgent` - Player is controlled by computer and just chooses random valid columns to place token
* `MonteCarloAgent` - Player is controlled by computer and uses Monte Carlo Tree Search to find a good move

As an example, we can run:

`python -m connectfour.game --player-one RandomAgent --player-two HumanPlayer`

To have a `RandomAgent` play against yourself.

## Setup

### Prerequisites

The code was written in **Python 3.6** In order to display the game's GUI, we used [Tkinter](https://docs.python.org/3/library/tkinter.html) module, which is the standard Python interface to the Tk GUI toolkit. Although you don't need to download Tkinter since it is an integral part of all Python distributions. In any case, you can find more details about Tkinter installation [here](http://ftp.ntua.gr/mirror/python/topics/tkinter/download.html).

### Installation

1. Project dependencies are managed by [`pipenv`](https://github.com/pypa/pipenv). Do `pipenv install --skip-lock --dev` to install everything. (currently `--skip-lock` is used because Pipenv is failing to handle `black`)
2. Ensure Tkinter has correctly installed (follow instructions in link in 'Prerequisites' section)

### Testing

Run `pipenv run python -m pytest tests/` (You can omit `pipenv run` if you're in a `pipenv shell`)

### Linting and Code Formatting

This project uses [`black`](https://github.com/ambv/black) to keep code neat and standardised. It should already have been installed during project installation (see [Installation](#installation) section).

Run `black` with: `pipenv run black connectfour tests` g(You can omit `pipenv run` if you're in a `pipenv shell`)
