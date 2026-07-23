from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, root.val)])
        total = 0

        while queue:
            node, curr = queue.popleft()

            if not node.left and not node.right:
                total += curr
            else:
                if node.left:
                    new_num = (curr << 1) + node.left.val
                    queue.append((node.left, new_num))

                if node.right:
                    new_num = (curr << 1) + node.right.val
                    queue.append((node.right, new_num))
        return total

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    sol = Solution()
    print(sol.sumRootToLeaf(root)) 
