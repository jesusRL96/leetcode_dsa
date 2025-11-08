class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_dfs(root):
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result

def preorder_dfs(root):
    result = []
    def traverse(node):
        if not node:
            return
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return result

def postorder_dfs(root):
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)
    traverse(root)
    return result

def create_sample_tree():
    """Create this binary tree:
          1
         / \
        2   3
       / \   \
      4   5   6
         /
        7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.right.right = TreeNode(6)
    return root

# aditional functions
def dfs_search(root, target):
    """DFS to search for a value in the tree"""
    if not root:
        return False
    if root.val == target:
        return True
    return dfs_search(root.left, target) or dfs_search(root.right, target)

def dfs_max_depth(root):
    """DFS to find maximum depth of the tree"""
    if not root:
        return 0
    left_depth = dfs_max_depth(root.left)
    right_depth = dfs_max_depth(root.right)
    return max(left_depth, right_depth) + 1

# Create tree and test DFS traversals
if __name__ == "__main__":
    root = create_sample_tree()

    print("Binary Tree Structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\   \\")
    print("   4   5   6")
    print("      /")
    print("     7")
    print()

    print("Inorder DFS (Left->Root->Right):", inorder_dfs(root))
    print("Preorder DFS (Root->Left->Right):", preorder_dfs(root))
    print("Postorder DFS (Left->Right->Root):", postorder_dfs(root))

    # Test the additional functions
    print("\nAdditional DFS Operations:")
    print("Search for 5:", dfs_search(root, 5))        # True
    print("Search for 10:", dfs_search(root, 10))      # False
    print("Max depth:", dfs_max_depth(root))           # 4
