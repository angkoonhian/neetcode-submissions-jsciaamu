# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            curr_val_compare = q.val == p.val
            # Compare left, then right
            left_is_same = self.isSameTree(p.left, q.left)
            right_is_same = self.isSameTree(p.right, q.right)
            return left_is_same and right_is_same and curr_val_compare
            

    