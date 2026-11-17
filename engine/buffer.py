# holds the player's cell selection (considered the player's hand)
# fixed number of slots, set to match the length of the winning sequence


class Buffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.contents = []

    def add(self, code):
        self.contents.append(code)

    def is_full(self):
        return len(self.contents) >= self.capacity

    def empty_count(self):
        return len(self.capacity) - len(self.contents)

    def get_contents(self):
        return self.contents
