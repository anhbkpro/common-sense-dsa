class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.parent = None
		self.value = value

		
root = Node(20)
node9 = Node(9)
node25 = Node(25)
root.left = node9
root.right = node25
node5 = Node(5)
node12 = Node(12)
node11 = Node(11)
node14 = Node(14)
node9.parent = root
node9.left = node5
node9.right = node12
node5.parent = node9
node12.parent = node9
node12.left = node11
node12.right = node14
node11.parent = node12
node14.parent = node12
node25.parent = root

def find_inorder_successor(root):
    if root.right:
        return find_left_leaf_on_the_right(root.right)
    else:
        return find_parent_of_current_branch(root)

def find_left_leaf_on_the_right(root):
    if root.left:
        return find_left_leaf_on_the_right(root.left)
    else:
        return root

def find_parent_of_current_branch(root):
    if root.parent is not None and root.parent.left is root:
        return root.parent
    elif root.parent is None:
        return None
    else:
        return find_parent_of_current_branch(root.parent)

result = find_inorder_successor(root)
if result is not None:
    print(result.value)
else:
    print('None')
