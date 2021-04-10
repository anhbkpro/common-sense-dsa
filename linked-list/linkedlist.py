class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def traverse(self):
        current_node = self.first_node
        while current_node is not None:
            print(str(current_node.data))
            current_node = current_node.next_node

    def read(self, index):
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
        if current_node is not None:
            print(f'Node at {index} contains "{current_node.data}"')
            return current_node.data
        else:
            print(f'You read index out of range')
            return None

    def index_of(self, value):
        # We begin 'at' the first node of the list:
        current_node = self.first_node
        current_index = 0
        if self.first_node.data == value:
            return current_index
        while current_node is not None:
            # If we find the data we're looking for, we return it:
            if current_node.data == value:
                return current_index
            # Otherwise, we move on the next node
            current_node = current_node.next_node
            current_index += 1
        # If we 'get' through the 'entire' list and 'without finding the data', we return None:
        return None

    def insert_at_index(self, index, value):
        # We created a new node with the provided value
        new_node = Node(value)
        # If we are inserting at the beginning of the list
        if index == 0:
            # Have our new node link to what was the first node
            new_node.next_node = self.first_node
            # Node our node is the first node of the list
            self.first_node = new_node
            return

        # If we are inserting anywhere other than the beginning
        current_node = self.first_node
        current_index = 0
        # First we access the node immediately before where the new node will go
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, index):
        # If we are deleting the first node:
        to_be_removed_node = self.first_node
        if index == 0:
            # Simply set the first node to be what is currently the second node:
            self.first_node = to_be_removed_node.next_node
            return to_be_removed_node.data

        current_node = self.first_node
        current_index = 0

        # First, we find the node immediately before the node we want to delete
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
        to_be_removed_node = current_node.next_node
        current_node.next_node = to_be_removed_node.next_node
        return to_be_removed_node.data


node_1 = Node("once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4
list = LinkedList(node_1)
list.traverse()
list.read(3)
print(list.index_of("why"))

print("*** insert new node ***")
list.insert_at_index(3, "purple")
list.traverse()
print("*** delete a node ***")
print(list.delete_at_index(3), 'deleted')
list.traverse()
