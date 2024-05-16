class FlexiTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class FlexiTree:
    def __init__(self):
        self.root = None

    def add_node(self, parent, data):
        if parent is None:
            if self.root is None:
                self.root = FlexiTreeNode(data)
                return True
            else:
                return False

        new_node = FlexiTreeNode(data)
        parent.children.append(new_node)
        return True

    def remove_node(self, parent, node_to_remove):
        if parent is None:
            if self.root == node_to_remove:
                self.root = None
                return True
            else:
                return False

        if node_to_remove in parent.children:
            parent.children.remove(node_to_remove)
            return True
        else:
            return False
