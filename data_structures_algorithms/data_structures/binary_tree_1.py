from typing import Optional, List


class Node:

    def __init__(self, value=None) -> None:
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.value: int = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)


# types of traversal
# 1. in-order -> left, root, right : [4, 2, 5, 1, 3]
# 2. pre-order ->  root, left, right: [1, 2, 4, 5, 3]
# 3. post-order -> left, right, root : [4, 5, 2, 3, 1]


def preorder_traversal(node: Optional[Node]) -> List[int]:
    result = []
    if node:
        result.append(node.value)
        result += preorder_traversal(node.left)
        result += preorder_traversal(node.right)
    return result


def inorder_traversal(node: Optional[Node]) -> List[int]:
    result = []
    if node:
        result += inorder_traversal(node.left)
        result.append(node.value)
        result += inorder_traversal(node.right)
    return result


def postorder_traversal(node: Optional[Node]) -> List[int]:
    result = []
    if node:
        result += postorder_traversal(node.left)
        result += postorder_traversal(node.right)
        result.append(node.value)
    return result


if __name__ == "__main__":
    """
            1
        2           3
    4       5
    """
    root = Node(value=1)
    root.left = Node(value=2)
    root.right = Node(value=3)
    root.left.left = Node(value=4)
    root.left.right = Node(value=5)
    print(root)
