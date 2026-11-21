import pytest

from engine.matrix import Matrix, generate_code_pool


def test_code_pool_length() -> None:
    """Correct number of hex codes is generated"""
    assert len(generate_code_pool(10)) == 10


def test_no_duplicates_in_code_pool() -> None:
    """Code pool does not contain duplicate hex codes"""
    pool = generate_code_pool(150)
    assert len(pool) == len(set(pool))


def test_generate_256_codes() -> None:
    """Generate all 2-digit hex codes (0-256 — 00-FF)"""
    assert len(generate_code_pool(256)) == 256


def test_error_when_generating_257_codes() -> None:
    """ValueError is raised when generating more than 256 codes"""
    with pytest.raises(ValueError):
        generate_code_pool(257)


def test_matrix_correct_size() -> None:
    """Matrix is a square of the correct size"""
    matrix = Matrix(10)
    grid = matrix.get_grid()
    assert len(grid) == 10  # checks number of rows
    for row in grid:
        assert len(row) == 10  # checks number of columns


def test_each_cell_is_in_code_pool() -> None:
    """Every cell in the Matrix comes from the code pool"""
    matrix = Matrix(6)
    cells = {code for row in matrix.get_grid() for code in row}
    assert cells <= set(matrix.code_pool)
