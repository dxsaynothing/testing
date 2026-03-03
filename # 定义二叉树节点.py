# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def widthOfBinaryTree(root):
    if not root:
        return 0
    max_width = 0
    # 队列存储(节点, 节点索引)
    queue = [(root, 0)]
    while queue:
        level_len = len(queue)
        # 记录当前层最左、最右索引
        left_idx = queue[0][1]
        right_idx = queue[-1][1]
        # 更新最大宽度
        max_width = max(max_width, right_idx - left_idx + 1)
        # 处理当前层所有节点
        for _ in range(level_len):
            node, idx = queue.pop(0)
            if node.left:
                queue.append((node.left, 2 * idx))
            if node.right:
                queue.append((node.right, 2 * idx + 1))
    return max_width

# 测试示例1
root1 = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
print(widthOfBinaryTree(root1))  # 4

# 测试示例2
root2 = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, None, TreeNode(7))))
print(widthOfBinaryTree(root2))  # 7

# 测试示例3
root3 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
print(widthOfBinaryTree(root3))  # 2