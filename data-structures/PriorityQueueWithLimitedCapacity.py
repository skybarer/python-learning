class PriorityQueueWithLimitedCapacity:
    def __init__(self, max_capacity):
        # Initialize priority queue and capacity variables
        self.priority_queue = PriorityQueue()
        self.capacity = max_capacity

    def insert(self, element, priority):
        if self.priority_queue.size() < self.capacity:
            self.priority_queue.insert(element, priority)
        else:
            # If queue is full, remove element with lowest priority
            self.priority_queue.delete_lowest_priority()
            self.priority_queue.insert(element, priority)

    def delete(self):
        # Remove and return element with highest priority
        return self.priority_queue.delete()

    def peek(self):
        # Return element with highest priority without removing it
        return self.priority_queue.peek()

    def size(self):
        # Return current number of elements in the queue
        return self.priority_queue.size()

    def is_empty(self):
        # Check if the queue is empty
        return self.priority_queue.is_empty()

    def is_full(self):
        # Check if the queue has reached its maximum capacity
        return self.priority_queue.size() == self.capacity
