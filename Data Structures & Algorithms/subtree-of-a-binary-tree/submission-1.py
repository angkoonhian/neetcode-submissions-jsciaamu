# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        is_same_tree = self.isSameTree(root, subRoot)
        compare_left = self.isSubtree(root.left, subRoot)
        compare_right = self.isSubtree(root.right, subRoot)
        return compare_left or compare_right or is_same_tree

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
            

    



        