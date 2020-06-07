class Node:
    def __init__(self, data=None):  # it works
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):  # it works
        self.head = Node()
        self.tail = Node()

    def __del__(self):
        current = self.head
        current.next = None
        current.previous = None

    def append(self, data):
        new_node = Node(data)
        current = self.head
        self.tail.previous = new_node
        while current.next is not None:
            current = current.next
        current.next = new_node
        #new_node.next = tail # This line keep breaking

    def prepend(self, data):  # it works
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.previous = self.head
        #if self.head.next is None:
        #    self.tail.previous = new_node.next
        #    new_node.next = self.tail

    def length(self):  # it works
        current = self.head
        total = 0
        while current is not None:
            total += 1
            current = current.next
        return total-1  # discount the tail

    def display(self):  # it works
        elements = []
        current = self.head
        while current is not None:
            current = current.next
            elements.append(current.data)
        return elements

    def displayBackwards(self):  # not works
        elements = []
        current = self.tail
        while current.previous is not None:
            current = current.previous
        elements.append(current.data)
        return elements

    def path(self, index):  # it works
        total = self.length()
        path = total/2
        if index > path:
            return 0     # starts with tail
        else:
            return 1     # starts with head

    def get(self, index):  # it works, just with path ==1
        size = self.length()
        if index > size:
            return "ERROR: 'get' index out of range"
        path = self.path(index)
        if path == 1:
            current_index = 0
            current = self.head
            while True:
                current = current.next
                if current_index == index:
                    return current.data
                current_index += 1
        else:
            current_index = size
            current = self.tail
            while True:
                current = current.previous
                if current_index == index:
                    return current.data
                current_index -= 1

    def erase(self, index):
        size = self.length()
        if index > size:
            return "ERROR: 'get' index out of range"
        path = self.path(index)
        if path == 1:
            current_index = 0
            current = self.head
            while True:
                last_node = current
                current = current.next
                if current_index == index:
                    last_node.next = current.next
                    current.previous = last_node
                current_index += 1
        else:
            current_index = size
            current = self.tail
            while True:
                current = current.previous
                next_node = current
                if current_index == index:
                    current.next = next_node.next
                    next_node.previous = current
                current_index -= 1
