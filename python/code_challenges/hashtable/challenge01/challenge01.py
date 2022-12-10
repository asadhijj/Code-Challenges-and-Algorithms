class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        '''A method that takes in nodes and an integer then append them to a list, then sums left and right values 
        to check if the sum is equal to thee entered integer and returns a boolean depending on the case'''
        self.values = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            self.values.append(root.val)
            dfs(root.right)
        dfs(root)
        left, right = 0, len(self.values) - 1
        while left < right:
            total = self.values[left] + self.values[right]
            if total == k:
                return True
            if total < k:
                left += 1
            else:
                right -= 1
        return False

