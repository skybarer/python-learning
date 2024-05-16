class IntervalMapNode:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value
        self.left = None
        self.right = None
        self.max_end = end


class IntervalMap:
    def __init__(self):
        self.root = None

    def insert(self, start, end, value):
        if start >= end:
            raise ValueError("Invalid interval")
        self.root = self._insert(self.root, start, end, value)

    def _insert(self, node, start, end, value):
        if not node:
            return IntervalMapNode(start, end, value)

        if start < node.start:
            node.left = self._insert(node.left, start, end, value)
        else:
            node.right = self._insert(node.right, start, end, value)

        node.max_end = max(node.max_end, end)
        return node

    def query(self, start, end):
        return self._query(self.root, start, end)

    def _query(self, node, start, end):
        if not node or start >= end:
            return None

        if node.start < end and start < node.end:
            return node.value

        if node.left and node.left.max_end > start:
            return self._query(node.left, start, end)

        return self._query(node.right, start, end)

    def delete(self, start, end):
        self.root = self._delete(self.root, start, end)

    def _delete(self, node, start, end):
        if not node:
            return None

        if start < node.start:
            node.left = self._delete(node.left, start, end)
        elif start > node.start:
            node.right = self._delete(node.right, start, end)
        else:
            if node.end == end:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                min_larger_node = self._get_min(node.right)
                node.start, node.end, node.value = min_larger_node.start, min_larger_node.end, min_larger_node.value
                node.right = self._delete(node.right, min_larger_node.start, min_larger_node.end)

        node.max_end = max(node.end, self._get_max_end(node.left), self._get_max_end(node.right))
        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def _get_max_end(self, node):
        if not node:
            return float('-inf')
        return node.max_end


# Example usage
imap = IntervalMap()
imap.insert(1, 5, "A")
imap.insert(6, 10, "B")
print(imap.query(4, 7))  # Output: "A"
imap.delete(1, 5)
print(imap.query(4, 7))  # Output: None
