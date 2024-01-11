# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.d=0
        
        def tra(r):
            if not r:
                return [-1,1000000]
            if r.left==None and r.right==None:
                return [r.val,r.val]
            
            a=tra(r.left)
            b=tra(r.right)
            m=max(a[0],b[0])
            n=min(a[1],b[1])
            self.d=max(self.d,max(abs(r.val-n),abs(r.val-m)))
            m=max(m,r.val)
            n=min(n,r.val)
            return [m,n]
        
        c=tra(root)
        return self.d