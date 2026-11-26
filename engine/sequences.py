# defines the winning sequence, chosen from the matrix
# to be matched with the player's buffer
import random
from engine.matrix import Matrix


def trace_path(matrix: Matrix, path_length: int) -> list[tuple[int, int]]:
    """Traverse a matrix to find a path of (row, col) coordinates"""

    if path_length > matrix.size * 2:
        raise ValueError("Path length is too long for this grid")

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


def assign_sequence_lengths(
    path_length: int, sequence_count: int, max_length: int, min_shared: int
) -> list[int]:
    """Determines the length of each target sequence"""

    while True:
        lengths = [max_length] + [
            random.randint(2, max_length) for _ in range(sequence_count - 1)
        ]
        if sum(lengths) - path_length >= min_shared:
            return lengths


def assign_coordinate_positions(
    path: list[tuple[int, int]], sequence_lengths: list[int]
) -> list[list[int]]:
    """Determines which hex code coordinates belong to each target sequence"""

    # empty list of sets, one set for each sequence
    sequences = [set() for _ in sequence_lengths]

    # shuffled order of positions from 0 - (path length - 1)
    # used to give each sequence set a path coordinate index in a random order
    order = random.sample(range(len(path)), len(path))

    for position in order:
        has_room = [
            # i = index of a set within sequences
            i for i in range(len(sequences)) if len(sequences[i]) < sequence_lengths[i]
        ]
        sequences[random.choice(has_room)].add(position)

    return [sorted(sequence) for sequence in sequences]


def generate_sequences(matrix: Matrix, buffer_size: int) -> list[str]:
    """Utilize trace_path to generate a winning sequence"""

    path = trace_path(matrix, buffer_size)
    return [matrix.get_cell(row, col) for row, col in path]
