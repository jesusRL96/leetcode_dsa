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
    print("    / \\")
    print("   4   5")
    print()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

def diameter_bt_dfs(root):
    def traverse(node, diameter):
        if not node:
            return 0, diameter
        left_edges, diameter = traverse(node.left, diameter)
        right_edges, diameter = traverse(node.right, diameter)
        diameter_n = left_edges + right_edges
        print("diamter: ", diameter_n)
        print("max diamter: ", diameter)
        diameter = max(diameter, diameter_n)
        print("max: ", max(left_edges, right_edges) + 1)
        return max(left_edges, right_edges) + 1, diameter
    result = traverse(root, 0)
    print(f"{result=}")


# Create tree and test DFS traversals
if __name__ == "__main__":
    root = create_sample_tree()
    diameter_bt_dfs(root)
    root = create_sample_tree2()
    diameter_bt_dfs(root)
