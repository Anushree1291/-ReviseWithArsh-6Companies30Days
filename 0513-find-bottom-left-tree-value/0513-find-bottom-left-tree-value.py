# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, r: Optional[TreeNode]) -> int:
        if r.left==None and r.right==None:
            return r.val
        q=[]
        q.append(r)
        a=r.val
        
        while q:
            a=q[0].val
            l=len(q)
            while l:
                l-=1
                qu=q.pop(0)
                if qu.left:
                    q.append(qu.left)
                if qu.right:
                    q.append(qu.right)
                
        return a