class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.left.val if self.left else None} <- {self.val} -> {self.right.val if self.right else None}"

def create_sample_tree():
    print("Binary Tree Structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\   \\")
    print("   4   5   6")
    print("      /")
    print("     7")
    print()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.right.right = TreeNode(6)
    return root

def create_sample_tree2():
    print("Binary Tree Structure:")
    print("       2")
    print("      / \\")
    print("     1   3")
    print("    / \\   \\")
    print("   4   5   9")
    print("      /")
    print("     7")
    print()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root

def max_ancestor_diff_dfs(root):
    def traverse(node,min_val, max_val):
        if not node:
            print(f"{max_val} - {min_val} = {max_val - min_val}")
            return max_val - min_val
        min_val = min(min_val, node.val)
        max_val = max(max_val, node.val)

        left = traverse(node.left, min_val, max_val)
        right = traverse(node.right, min_val, max_val)
        print(str(node))
        print(f"{left=}")
        print(f"{right=}")
        return max(left, right)
    result = traverse(root, root.val, root.val)
    print(f"{result=}")


# Create tree and test DFS traversals
if __name__ == "__main__":
    root = create_sample_tree()
    max_ancestor_diff_dfs(root)
    root = create_sample_tree2()
    max_ancestor_diff_dfs(root)
