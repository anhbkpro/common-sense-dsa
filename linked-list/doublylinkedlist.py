class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.first_node is None:
            print('insert first and last node')
            self.first_node = new_node
            self.last_node = new_node
            return

        new_node.previous_node = self.last_node
        self.last_node.next_node = new_node
        print(f'make the node = {value} the last node')
        self.last_node = new_node

    def remove_from_front(self):
        if self.first_node is None:
            print('can not remove an empty list')
            return
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node

    def print_in_reverse(self):
        current_node = self.last_node
        while current_node is not None:
            print(f'{current_node.data}')
            current_node = current_node.previous_node


class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, element):
        self.queue.insert_at_end(element)

    def dequeue(self):
        removed_node = self.queue.remove_from_front()
        return removed_node.data

    def read(self):
        if self.queue.first_node is None:
            return None
        return self.queue.first_node.data


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.enqueue(3)
print(q.read())
q.dequeue()
print(q.read())



