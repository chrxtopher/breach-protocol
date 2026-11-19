# defines the winning sequence, chosen from the matrix
# to be matched with the player's buffer
import random
from engine.matrix import Matrix


def generate_sequences(matrix: Matrix, buffer_size: int) -> list[str]:
    """Traverses a given Matrix grid and selects a winning sequence equal to a given buffer size"""
    # start on a random cell in the top row
    row, col = (0, random.randrange(matrix.size))
    used = set()
    winning_path = []
    selecting_from_column = True

    for _ in range(buffer_size):
        winning_path.append(matrix.get_cell(row, col))
        used.add((row, col))

        if selecting_from_column:
            options = [r for r in range(matrix.size) if (r, col) not in used]
            row = random.choice(options)
        else:
            options = [c for c in range(matrix.size) if (c, row) not in used]
            col = random.choice(options)

        selecting_from_column = not selecting_from_column

    return winning_path
