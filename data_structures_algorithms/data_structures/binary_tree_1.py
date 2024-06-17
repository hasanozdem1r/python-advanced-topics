class Node:

    def __init__(self,value=None) -> None:
        self.left = None
        self.right = None
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)

# types of traversal
# 1. in-order -> left, root, right : [4, 2, 5, 1, 3]
# 2. pre-order ->  root, left, right: [1, 2, 4, 5, 3]
# 3. post-order -> left, right, root : [4, 5, 2, 3, 1]

# in-order : 4 -> 2 -> 5 -> 1 - 3


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