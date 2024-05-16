class IndexedDeque:
    def __init__(self):
        self.front = []
        self.back = []

    def _rebalance(self):
        # Re-balance the two halves if necessary
        if len(self.front) > len(self.back) + 1:
            self.back.insert(0, self.front.pop())
        elif len(self.back) > len(self.front) + 1:
            self.front.append(self.back.pop(0))

    def push_front(self, item):
        self.front.append(item)
        self._rebalance()

    def push_back(self, item):
        self.back.insert(0, item)
        self._rebalance()

    def pop_front(self):
        if self.front:
            item = self.front.pop()
        else:
            item = self.back.pop(0)
        self._rebalance()
        return item

    def pop_back(self):
        if self.back:
            item = self.back.pop(0)
        else:
            item = self.front.pop()
        self._rebalance()
        return item

    def get(self, index):
        if index < len(self.front):
            return self.front[-1 - index]
        else:
            return self.back[index - len(self.front)]

    def set(self, index, item):
        if index < len(self.front):
            self.front[-1 - index] = item
        else:
            self.back[index - len(self.front)] = item

    def size(self):
        return len(self.front) + len(self.back)


# Example usage
deque = IndexedDeque()
deque.push_front(1)
deque.push_back(2)
deque.push_front(0)
print(deque.pop_back())  # Output: 2
print(deque.get(1))  # Output: 1
deque.set(1, 3)
print(deque.get(1))  # Output: 3
print(deque.size())  # Output: 2
