# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        q = [root]
        res = []
        level=1
        while len(q) != 0:
            arr = []
            leng = len(q)
            for i in range(leng):
                temp = q.pop(0)
                arr.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            if level%2==0:
                arr.reverse()
                res.append(arr)
            else:
                res.append(arr)
            level+=1
        return res