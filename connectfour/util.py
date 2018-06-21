'''
Module to utility functionality to aid students in building
Connect Four playing agents.
'''


def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)
