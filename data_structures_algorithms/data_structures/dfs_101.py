"""
Start at the Root Node: Mark the starting node as visited.
Explore Adjacent Nodes: For each neighbor of the current node, do the following:
If the neighbor hasn't been visited, recursively perform DFS on it.

Backtrack: Once all paths from a node have been explored, backtrack to the previous node and continue the process.
Termination: The algorithm ends when all nodes reachable from the starting node have been visited.
"""

class Node:
    """
    A class representing a node in a graph or tree structure.
    
    Attributes:
    - value: The data stored in the node
    - children: A list of child nodes connected to this node
    - visited: A flag to track if the node has been visited during traversal
    """
    def __init__(self, value):
        """
        Initialize a node with a given value.
        
        :param value: The data to be stored in the node
        """
        self.value = value
        self.children = []  # List to store child nodes
        self.visited = False  # Flag to track node visitation

    
    def add_child(self, child_node):
        """
        Add a child node to the current node.
        
        :param child_node: Node to be added as a child
        """
        self.children.append(child_node)

def depth_first_search(start_node, target):
    """
    Perform Depth-First Search to find a target value in a graph or tree.
    
    :param start_node: The node to begin the search from
    :param target: The value we're searching for
    :return: The node containing the target value, or None if not found
    """
    # Reset visited status for all nodes before starting
    def reset_visited(node):
        node.visited = False
        for child in node.children:
            reset_visited(child)
    
    reset_visited(start_node)
    
    # Stack to keep track of nodes to visit
    stack = [start_node]
    
    while stack:
        # Get the top node from the stack
        current_node = stack.pop()
        
        # Mark the current node as visited
        current_node.visited = True
        
        # Check if current node matches the target
        if current_node.value == target:
            return current_node
        
        # Add unvisited children to the stack in reverse order
        # (to maintain left-to-right traversal when popping)
        for child in reversed(current_node.children):
            if not child.visited:
                stack.append(child)
    
    # Target not found
    return None

# Example usage and demonstration
def create_sample_graph():
    """
    Create a sample graph to demonstrate DFS
    
    Graph Structure:
             A
           / | \
          B  C  D
         / \    |
        E   F   G
           |
           H
    """
    # Create nodes
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    
    # Build connections
    a.add_child(b)
    a.add_child(c)
    a.add_child(d)
    
    b.add_child(e)
    b.add_child(f)
    
    d.add_child(g)
    
    f.add_child(h)
    
     # root node
    return a 

# Demonstrate DFS
def main():
    # Create the sample graph
    root = create_sample_graph()
    
    # Search for different nodes
    print("Searching for 'H':")
    result = depth_first_search(root, 'H')
    print(f"Found node: {result.value if result else 'Not Found'}")
    
    print("\nSearching for 'X':")
    result = depth_first_search(root, 'X')
    print(f"Found node: {result.value if result else 'Not Found'}")

if __name__ == "__main__":
    main()