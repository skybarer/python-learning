class DoubleStackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)
        print(f"Enqueued {item}")

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            item = self.stack2.pop()
            print(f"Dequeued {item}")
            return item
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1] if self.stack2 else None
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)

# Example usage
dsq = DoubleStackQueue()
dsq.enqueue(10)
dsq.enqueue(20)
dsq.enqueue(30)
print(f"Peek: {dsq.peek()}")  # Should print 10
print(f"Dequeue: {dsq.dequeue()}")  # Should print and remove 10
print(f"Dequeue: {dsq.dequeue()}")  # Should print and remove 20
print(f"Size: {dsq.size()}")  # Should print 1
print(f"Is Empty: {dsq.is_empty()}")  # Should print False
dsq.enqueue(40)
print(f"Peek: {dsq.peek()}")  # Should print 30
