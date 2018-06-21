from connectfour import util


def test_manhattan_distance():
    assert 0 == util.manhattan_distance((0, 0), (0, 0))
    assert 1 == util.manhattan_distance((0, 0), (0, 1))
    assert 1 == util.manhattan_distance((0, 0), (1, 0))
    assert 4 == util.manhattan_distance((0, 0), (2, 2))
