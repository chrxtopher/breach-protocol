# generate CODE_POOL of 2-digit hexadecimal [00 - FF]
# fills NxN matrix with codes from code pool
import random


def generate_code_pool(size: int = 6) -> list[str]:
    """Generates list of random hex codes (00-FF) for Matrix grid — default size 6"""

    if size > 256:
        raise ValueError("Size exceeds hex code ceiling (256)")
    codes = set()
    while len(codes) < size:
        n = random.randint(0, 255)
        codes.add(f"{n:02X}")

    return list(codes)


class Matrix:
    """A square grid of 2-digit hex codes drawn from a code pool"""

    def __init__(self, size: int = 6, code_pool: list[str] | None = None) -> None:
        if code_pool is None:
            code_pool = generate_code_pool()
        self.size = size
        self.code_pool = code_pool
        self.grid = [
            [random.choice(code_pool) for _ in range(size)] for _ in range(size)
        ]

    def get_grid(self) -> list[list[str]]:
        return self.grid

    def get_row(self, row: int) -> list[str]:
        return self.grid[row]

    def get_col(self, col: int) -> list[str]:
        return [row[col] for row in self.grid]

    def get_cell(self, row: int, col: int) -> str:
        return self.grid[row][col]
