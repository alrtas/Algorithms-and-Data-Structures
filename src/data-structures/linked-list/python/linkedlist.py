class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __del__(self):
        current = self.head
        current.next = None

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current = self.head
        while current.next is not None:
            current = current.next
            elements.append(current.data)
        print elements

    def get(self, index):
        if index >= self.length():
            print "ERROR: 'get' index out of range"
            return None
        current_index = 0
        current = self.head
        while True:
            current = current.next
            if current_index == index:
                return current.data
            current_index += 1

    def erase(self, index):
        if index >= self.length():
            print "ERROR: 'get' index out of range"
            return None
        current_index = 0
        current = self.head
        while True:
            last_node = current
            current = current.next
            if current_index == index:
                last_node.next = current.next
                return
            current_index += 1

    def prepend(self, data):
        current = self.head
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
