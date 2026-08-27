# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replacenode(self,root):
        while root.right !=None:
            root=root.right

        return root.val
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root==None:
            return None
        
            
        if root.val<key:
            root.right= self.deleteNode(root.right,key)
        elif root.val>key:
            root.left= self.deleteNode(root.left,key)
        else:
            if root.left == None and root.right ==None:
                return None

            if root.left ==None:
                return root.right
            if root.right ==None:
                return root.left

            temp=self.replacenode(root.left)
            root.val=temp
            root.left=self.deleteNode(root.left,temp)
            
        return root

        
