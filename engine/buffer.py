# holds the player's cell selection (considered the player's hand)
# fixed number of slots, set to match the length of the winning sequence


class Buffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.contents = []

    def add(self, code: str):
        if not self.is_full():
            self.contents.append(code)

    def is_full(self) -> bool:
        return len(self.contents) >= self.capacity

    def empty_slot_count(self) -> int:
        return self.capacity - len(self.contents)

    def get_contents(self) -> list:
        return self.contents
