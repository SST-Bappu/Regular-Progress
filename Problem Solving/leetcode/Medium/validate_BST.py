class TreeNode:
    def __init__(self,value):
        self.val = value
        self.right = None
        self.left = None
def validate_BST(head,left=float("-inf"), right = float("inf")):
    if not head:
        return True
    if head.val<=left or head.val>=right:
        return False
    return validate_BST(head.left,left,head.val) and validate_BST(head.right,head.val,right)