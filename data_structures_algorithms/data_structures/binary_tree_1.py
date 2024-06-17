class Node:

    def __init__(self, left=None, right=None, value=None) -> None:
        self.left = left
        self.right = right
        self.value = value


if __name__ == "_main__":
    """
            3
        6       9
    12
    """
    n1 = Node(value=3)
    n2 = Node(value=6)
    n3 = Node(value=9)
    n4 = Node(value=12)
    n1.left = n2
    n1.right = n3
    n3.left = n4
