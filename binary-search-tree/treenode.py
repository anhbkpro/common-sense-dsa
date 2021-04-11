class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right


def search(search_value, node):
    if node is None or node.value == search_value:
        print('Found it')
    elif node.value > search_value:
        print('Left')
        return search(search_value, node.leftChild)
    else:
        print('Right')
        return search(search_value, node.rightChild)


node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
search(75, root)
