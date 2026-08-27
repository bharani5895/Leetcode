# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root, res=None):
        if res is None:
            res = []

        if root:
            self.inOrder(root.left, res)
            res.append(root.val)  
            self.inOrder(root.right, res)

        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = self.inOrder(root)
        return nodes[k - 1]
        