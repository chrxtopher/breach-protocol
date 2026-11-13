# generate CODE_POOL of 2-digit hexadecimal [00 - FF]
# fills NxN matrix with codes from code pool
import random


def generate_code_pool(size=6):
    codes = set()
    while len(codes) < size:
        n = random.randint(0, 255)
        codes.add(f"{n:02X}")

    return list(codes)


class Matrix:
    def __init__(self, size=6, code_pool=None):
        if code_pool is None:
            code_pool = generate_code_pool()
        self.size = size
        self.code_pool = code_pool
        self.grid = [
            [random.choice(code_pool) for _ in range(size)] for _ in range(size)
        ]

    def get_grid(self):
        return self.grid

    def get_row(self, row):
        return self.grid[row]

    def get_col(self, col):
        return [row[col] for row in self.grid]

    def get_cell(self, row, col):
        return self.grid[row][col]
