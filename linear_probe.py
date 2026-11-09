class LinearProbe:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, index, value):
        collisions = 0
        while self.table[index] is not None:
            index = (index + 1) % self.size
            collisions += 1
        self.table[index] = value
        
        return collisions

    def get_list(self):
        return self.table