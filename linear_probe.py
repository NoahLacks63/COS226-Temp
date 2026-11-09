class LinearProbe:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, index, value):
        while self.table[index] is not None:
            if self.table[index] == key:
                break
            index = (index + 1) % self.size
        self.table[index] = (key, value)