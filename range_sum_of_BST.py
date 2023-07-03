class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        total = 0
        
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                total += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return total
    