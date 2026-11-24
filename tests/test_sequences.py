import pytest

from engine.sequences import generate_sequences, trace_path
from engine.matrix import Matrix


# trace_path tests


def test_path_length() -> None:
    """Traces a path of the correct length"""
    matrix = Matrix()
    path = trace_path(matrix, 0)
    path2 = trace_path(matrix, 5)
    path3 = trace_path(matrix, 10)
    assert len(path) == 0
    assert len(path2) == 5
    assert len(path3) == 10


def test_error_if_path_too_long() -> None:
    """Error is raised if path is longer than matrix.size * 2"""
    matrix = Matrix(4)
    with pytest.raises(ValueError):
        trace_path(matrix, 10)


def test_first_path_code_is_in_row_0() -> None:
    """Path begins in first row of matrix"""
    matrix = Matrix()
    path = trace_path(matrix, 5)

    # unpack tuple in position 0 of path
    assert matrix.get_cell(*path[0]) in matrix.get_row(0)


def test_each_position_is_inside_grid() -> None:
    """All path coordinates fall within matrix bounds"""
    matrix = Matrix()
    path = trace_path(matrix, 5)
    for row, col in path:
        assert 0 <= row < matrix.size
        assert 0 <= col < matrix.size


def test_all_positions_are_unique() -> None:
    """Path contains no duplicates"""
    matrix = Matrix()
    path = trace_path(matrix, 5)
    assert len(set(path)) == len(path)


def test_row_col_rotation() -> None:
    """Path rotates row/column for each coordinate"""
    matrix = Matrix()
    path = trace_path(matrix, 5)

    # start loop at path[1] and store path[0] as prev
    for i in range(1, len(path)):
        prev, curr = path[i - 1], path[i]
        if i % 2 == 0:
            assert curr[0] == prev[0]  # checks row
        else:
            assert curr[1] == prev[1]  # checks column


# generate_sequence tests


def test_sequence_is_correct_length():
    matrix = Matrix()
    sequence = generate_sequences(matrix, 5)
    assert len(sequence) == 5


def test_each_sequence_code_is_in_code_pool():
    matrix = Matrix()
    sequence = generate_sequences(matrix, 5)
    for code in sequence:
        assert code in matrix.code_pool
