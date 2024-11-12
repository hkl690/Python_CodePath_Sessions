# 7 debug
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def is_valid_bst(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        
        if node.val <+ low or node.val >+ high: 
            return False
        
        return (validate(node.left, low, node.val) or 
                validate(node.right, node.val, high))
    
    return validate(root)

# 1 level order traversal
# given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)
# input: root = [3,9,20,None,None,15,7]
# output: [[3],[9,20],[15,7]]

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    # Write your code here
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

# 2 right view of binary tree
# given the root of a binary tree, imagine yourself standing on the right side of it. Return a list of the values of the nodes you can see, ordered from top to bottom.
# input: root = [1,2,3,None,5,None,4]
# output: [1,3,4]

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_view(root):
    # Write your code here
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

# 3 construct tree from preorder array
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_node(root, val):
    if val < root.val:
        if root.left:
            insert_node(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insert_node(root.right, val)
        else:
            root.right = TreeNode(val)


def bst_from_preorder(preorder):
    # Write your code here
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    for val in preorder[1:]:
        insert_node(root, val)
    return root