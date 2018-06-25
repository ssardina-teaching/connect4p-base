"""
Module to utility functionality to aid students in building
Connect Four playing agents.
"""

import time


def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


def delay_move_execution(move_fn):
    max_execution_time_in_sec = 1

    def wrapper():
        start = time.time()
        move = move_fn()
        end = time.time()
        execution_time = end - start
        end_delay = max(max_execution_time_in_sec - execution_time, 0)
        time.sleep(end_delay)
        return move
    return wrapper
