class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Tree:
    def __init__(self):
        self.queue = []
    def making_the_tree(self, root):
        '''
        a method to build the tree
        '''
        stack = []
        if not root:
            stack.append(None)
            return "Tree is empty"
        node= root
        self.queue.append(node)
        while self.queue:
            node= self.queue.pop(0)
            stack.append(node.val)
            if node.left != None:
                self.queue.append(node.left)
            if node.right != None:
                self.queue.append(node.right)
        return stack

    def listToBts(self, array) :
        '''
        Convert ascending sequence to balanced BST
        '''
        if len(array) == 0: # Our list is empty
            return None
        if len(array) == 1: # Our list has only one element
            return TreeNode(array[0])
        array.sort()
        mid = len(array) // 2
        root = TreeNode(array[mid])
        root.left = self.listToBts(array[:mid])
        root.right = self.listToBts(array[mid+1:])
        return root