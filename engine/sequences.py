# defines the winning sequence, chosen from the matrix
# to be matched with the player's buffer
import random
from engine.matrix import Matrix


def trace_path(matrix: Matrix, path_length: int) -> list[tuple[int, int]]:
    """Traverse a matrix to find a path of (row, col) coordinates"""

    # start on a random cell in the top row
    row, col = (0, random.randrange(matrix.size))
    path = []
    selecting_from_column = True

    for _ in range(path_length):
        path.append((row, col))

        if len(path) == path_length:
            break

        if selecting_from_column:
            options = [r for r in range(matrix.size) if (r, col) not in path]
            row = random.choice(options)
        else:
            options = [c for c in range(matrix.size) if (row, c) not in path]
            col = random.choice(options)

        # rotate column/row selection for next coordinates
        selecting_from_column = not selecting_from_column

    return path


def generate_sequences(matrix: Matrix, buffer_size: int, sequence_count: int = 1) -> list[str]:
    """Utilize trace_path to generate a winning sequence"""

    path = trace_path(matrix, buffer_size)
    return [matrix.get_cell(row, col) for row, col in path]
