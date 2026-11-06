class Node:
    data = None
    child = None

    def __init__(self, data):
        self.data = data
        self.child = None

class LinkedList:
    head = None
    tail = None

    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.child = new_node
        self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.child