class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.child = None
        self.next_sibling = None


class CircularLinkedTree:
    def __init__(self):
        self.root = None

    def add_child(self, parent_node, data):
        new_node = TreeNode(data)
        new_node.parent = parent_node
        if parent_node.child is None:
            parent_node.child = new_node
            new_node.next_sibling = new_node  # Circular reference
        else:
            sibling = parent_node.child
            while sibling.next_sibling != parent_node.child:
                sibling = sibling.next_sibling
            sibling.next_sibling = new_node
            new_node.next_sibling = parent_node.child

    def traverse(self, start_node=None):
        if start_node is None:
            start_node = self.root
        current_node = start_node
        while current_node is not None:
            print(current_node.data)
            if current_node.child:
                self.traverse(current_node.child)
            current_node = current_node.next_sibling
            if current_node == start_node:  # Break the loop if we've traversed the entire circular structure
                break


# Example usage
if __name__ == "__main__":
    tree = CircularLinkedTree()
    tree.root = TreeNode("A")
    tree.add_child(tree.root, "B")
    tree.add_child(tree.root, "C")
    tree.add_child(tree.root.child, "D")
    tree.add_child(tree.root.child, "E")
    tree.add_child(tree.root.child.child, "F")

    print("Traversal:")
    tree.traverse()
