# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode],res=None) -> List[int]:
        
        if res is None:
            res = []

        if root:
            self.inorderTraversal(root.left, res)
            res.append(root.val)
            self.inorderTraversal(root.right, res)

        return res