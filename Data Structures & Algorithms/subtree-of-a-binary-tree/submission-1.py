# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSubroot(root, subRoot):
            if root == None and subRoot != None:
                return False
            if root != None and subRoot == None:
                return False
            if root == None and subRoot == None:
                return True
            if root.val != subRoot.val:
                return False
            return checkSubroot(root.left, subRoot.left) and checkSubroot(root.right, subRoot.right)


        def dfs(root):
            if root == None:
                return False
            if checkSubroot(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        
        return dfs(root)
        

