#!/usr/bin/env python

from connectfour.board import Board
from connectfour.agents.agent import HumanPlayer

from tkinter import Frame, Canvas, Tk, Label, NSEW, Button
import tkinter.font
import copy

LEFT_MOUSE_CLICK = '<Button-1>'


class Info(Frame):
    """
    Message in the top of screen
    """

    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100, bg="white")
        police = tkinter.font.Font(family="Arial", size=36, weight="bold")
        self.t = Label(self, text="Connect4 AI", font=police, bg="white")
        self.t.grid(sticky=NSEW, pady=20)


class Point(object):
    """
    Each one of the circles in the board
    """
    OUTLINE_COLOR = 'blue'
    RADIUS = 30

    def __init__(self, x, y, canvas, color="white"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.turn = 1
        self.r = self.RADIUS
        self.point = self.canvas.create_oval(
            self.x + 10,
            self.y + 10,
            self.x + 61,
            self.y + 61,
            fill=color,
            outline=self.OUTLINE_COLOR,
        )

    def setColor(self, color):
        self.canvas.itemconfigure(self.point, fill=color)
        self.color = color


class Terrain(Canvas):
    """
    Board visual representation
    """
    PLAYER_ONE_TOKEN_COLOR = 'yellow'
    PLAYER_TWO_TOKEN_COLOR = 'red'
    EMPTY_SLOT_COLOR = 'white'

    def __init__(self, game, info, master=None):
        """
        Args:
            game: An instance of `Game`, which contains player info and game state
            info: An info UI element that updates users on game state
            master: This represents the parent window. (required by Canvas superclass)
        """
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="blue")

        self.p = []
        self.game = game
        self.info = info
        self.winner = False

        board = []
        for i in range(6):
            row = []
            for j in range(7):
                row.append(0)
            board.append(row)

        self.b = Board()
        self.last_bstate = self.b

        for i in range(0, 340, int(400 / 6)):
            spots = []
            for j in range(0, 440, int(500 / 7)):
                spots.append(Point(j, i, self))

            self.p.append(spots)

        self.bind(LEFT_MOUSE_CLICK, self.action)

    def reloadBoard(self, i=None, j=None, val=None, bstate=None):
        """
        Reloads the board colors and content.
        Uses recursive upload for more complex cases (e.g. step back).
        [i,j,val] or [bstate] can be provided (but not simpultaneously).
        If no i, j, values or bstate are provided, it updates only colors.
        I bstate is present, updates the board values first and then colors.
        If i and j is present but no val, then updates the color of only one cell.
        If i and j and val are present, updates the matrix and the color.
        """
        if i is None:
            if bstate is not None:
                self.b = copy.deepcopy(bstate)
            for i in range(6):
                for j in range(7):
                    self.reloadBoard(i, j, val=None, bstate=None)
        elif val is None:
            if self.b.board[i][j] == -1:
                self.p[i][j].setColor(self.PLAYER_ONE_TOKEN_COLOR)
            elif self.b.board[i][j] == 1:
                self.p[i][j].setColor(self.PLAYER_TWO_TOKEN_COLOR)
            elif self.b.board[i][j] == 0:
                self.p[i][j].setColor(self.EMPTY_SLOT_COLOR)
        else:
            self.b.board[i][j] = val
            self.reloadBoard(i, j)

    def runComputerMove(self):
        row, col = self.game.current_player.get_move(self.b)
        assert self.b.validMove(row, col)
        self.b.last_move = [row, col]
        self.reloadBoard(row, col, self.game.current_player.id)

    def action(self, event):
        self.last_bstate = copy.deepcopy(self.b)

        # Human Action
        if not self.winner:
            col = int(event.x / 71)  # TODO: magic number here
            row = self.b.tryMove(col)

            if row == -1:
                return
            else:
                self.reloadBoard(row, col, self.game.current_player.id)

            self.b.last_move = [row, col]
            self.game.change_turn()
            self.setPostMoveState()
            self.update()

    def setPostMoveState(self):
        whos_turn_txt = '{}\'s Turn'.format(str(self.game.current_player))
        self.info.t.config(text=whos_turn_txt)

        result = self.b.winner()

        if result == self.game.PLAYER_ONE_ID:
            self.info.t.config(text="{} won!".format(self.game.player_one))
            self.winner = True
        elif result == self.game.PLAYER_TWO_ID:
            self.info.t.config(text="{} won!".format(self.game.player_two))
            self.winner = True
        elif self.b.terminal():
            self.info.t.config(text="Draw")
            self.winner = True

    def step_back(self):
        """
        Single human and computer step back
        """
        self.winner = False
        info.t.config(text="Your turn")
        self.reloadBoard(bstate=self.last_bstate)
        self.update()


def game_loop(root, game, terrain):
    def inner():
        # If current player is a Human Player, we just keep waiting for a
        # UI event to trigger the move
        if type(game.current_player) is not HumanPlayer:
            terrain.runComputerMove()
            game.change_turn()
            terrain.setPostMoveState()
            terrain.reloadBoard()
            terrain.update()

        if not terrain.winner and not terrain.b.terminal():
            root.after(100, inner)

    return inner


def start_game(game):
    root = Tk()
    root.geometry("500x550")
    root.title("Connect 4 AI Bot")
    root.configure(bg="white")
    root.minsize(500, 600)
    root.maxsize(500, 600)

    info = Info(root)
    info.grid(row=0, column=0)

    t = Terrain(game, info, root)
    t.grid(row=1, column=0)

    root.after(0, game_loop(root, game, t))

    def restart():
        global info
        info.t.config(text="")

        info = Info(root)
        info.grid(row=0, column=0)

        t = Terrain(root)
        t.grid(row=1, column=0)

    def step_back():
        global t
        t.step_back()

    def close():
        root.destroy()

    Button(root, text="Try again (?)", command=restart).grid(row=3, column=0, pady=5)
    Button(root, text="Step back", command=step_back).grid(row=2, column=0, pady=2)
    Button(root, text="Exit", command=close).grid(row=4, column=0, pady=2)

    root.mainloop()
