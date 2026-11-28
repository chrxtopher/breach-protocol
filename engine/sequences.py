import random
from engine.matrix import Matrix


def generate_sequences(
    matrix: Matrix,
    path_length: int,
    sequence_count: int,
    max_length: int,
    min_shared: int,
) -> list[list[str]]:
    """Generate solvable target sequences of hex codes, shortest first.

    Returns:
        list[list[str]] -- [list of hex codes]
    """

    path = trace_path(matrix, path_length)
    path_codes = [matrix.get_cell(row, col) for row, col in path]
    sequence_lengths = assign_sequence_lengths(
        path_length, sequence_count, max_length, min_shared
    )
    sequences_to_convert = assign_coordinate_indices_to_sequences(
        path_length, sequence_lengths
    )

    # convert all indices to their corresponding hex codes
    sequences = [
        [path_codes[coordinate_index] for coordinate_index in sequence]
        for sequence in sequences_to_convert
    ]

    # sorting sequences by length places shorter sequences before longer ones
    return sorted(sequences, key=len)


def trace_path(matrix: Matrix, path_length: int) -> list[tuple[int, int]]:
    """Traverse a matrix to find a solvable path of (row, col) coordinates

    Returns:
        list[tuple[int, int]] -- [(row, col)]
    """

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
    """Determines the length of each target sequence

    Returns:
        list[int] -- [length of each target sequence]
    """

    # guards to prevent looping forever
    if max_length < 2:
        raise ValueError("max_length must be at least 2")
    if max_length >= path_length:
        raise ValueError("max_length must be shorter than the path")
    if min_shared < 1:
        raise ValueError("min_shared must be at least 1")
    if sequence_count * max_length - path_length < min_shared:
        raise ValueError("min_shared is too high for these sequences")

    while True:
        lengths = [max_length] + [
            random.randint(2, max_length) for _ in range(sequence_count - 1)
        ]
        if sum(lengths) - path_length >= min_shared:
            return lengths


def assign_coordinate_indices_to_sequences(
    path_length: int, sequence_lengths: list[int]
) -> list[list[int]]:
    """Deals indices of coordinates within the path to one or more target sequences.

    Every index goes to at least one sequence, so the whole path is needed for each
    solution.

    Effectively determines the contents of each target sequence, derived from the
    whole path.

    Returns:
        list[list[int]] -- [[indices of coordinates within the path]]
    """

    sequences = [set() for _ in sequence_lengths]

    # shuffled index order of coordinates
    # used to deal an index to each sequence in a random order
    shuffled_order = random.sample(range(path_length), path_length)

    for coordinate_index in shuffled_order:
        # store indices of sequences that have room for more coordinates
        has_room = [
            sequence_index
            for sequence_index in range(len(sequences))
            if len(sequences[sequence_index]) < sequence_lengths[sequence_index]
        ]

        sequences[random.choice(has_room)].add(coordinate_index)

    # top up any sequences that are still shorter than their target length
    # added indices are unique to that sequence, but shared with another
    for sequence_index, sequence in enumerate(sequences):
        missing_count = sequence_lengths[sequence_index] - len(sequence)
        options = [
            coordinate_index
            for coordinate_index in range(path_length)
            if coordinate_index not in sequence
        ]

        sequence.update(random.sample(options, missing_count))

    # sorts each sequence of coordinate indices back into path order
    # sorting preserves solvability
    return [sorted(sequence) for sequence in sequences]


def sequence_progress(buffer_contents: list[str], sequence: list[str]) -> int:
    """Count how many codes of the target sequence that have been selected, in order

    Returns:
        int -- count of codes that the player has selected
    """
    curr_index = 0
    for code in buffer_contents:
        if curr_index < len(sequence) and sequence[curr_index] == code:
            curr_index += 1

    return curr_index


def is_sequence_complete(buffer_contents: list[str], sequence: list[str]) -> bool:
    """Determines if all codes within a target sequence have been selected.

    Returns:
        bool -- True if all codes within a target sequence have been selected, False otherwise
    """

    return sequence_progress(buffer_contents, sequence) == len(sequence)
