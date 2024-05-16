class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("Circular Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def peek(self):
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        return self.queue[self.front]

    def rotate(self):
        if not self.is_empty():
            self.enqueue(self.dequeue())


class HierarchicalCircularQueue:
    def __init__(self, num_levels, queue_size):
        self.levels = [CircularQueue(queue_size) for _ in range(num_levels)]
        self.num_levels = num_levels

    def insert(self, data, priority):
        if priority >= self.num_levels or priority < 0:
            raise ValueError("Invalid priority level")
        self.levels[priority].enqueue(data)

    def remove(self):
        for level in self.levels:
            if not level.is_empty():
                return level.dequeue()
        raise IndexError("HCQ is empty")

    def peek(self):
        for level in self.levels:
            if not level.is_empty():
                return level.peek()
        raise IndexError("HCQ is empty")

    def is_empty(self):
        return all(level.is_empty() for level in self.levels)

    def is_full(self):
        return all(level.is_full() for level in self.levels)

    def rotate(self):
        for level in self.levels:
            level.rotate()


# Example Usage
hcq = HierarchicalCircularQueue(num_levels=3, queue_size=5)
hcq.insert("Task1", 1)
hcq.insert("Task2", 2)
hcq.insert("Task3", 1)

print(hcq.remove())  # Should return "Task1"
print(hcq.peek())    # Should return "Task3"
hcq.rotate()         # Rotate current level queues
