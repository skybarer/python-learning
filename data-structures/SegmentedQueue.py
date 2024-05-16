class SegmentedQueue:
    def __init__(self, segment_capacity):
        self.segment_capacity = segment_capacity
        self.segments = [[]]  # Start with one empty segment
        self.total_size = 0

    def enqueue(self, element):
        if len(self.segments[-1]) == self.segment_capacity:
            self.segments.append([])  # Create a new segment if the last one is full
        self.segments[-1].append(element)
        self.total_size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty SegmentedQueue")
        element = self.segments[0].pop(0)
        if len(self.segments[0]) == 0:
            self.segments.pop(0)  # Remove the segment if it's empty
        self.total_size -= 1
        return element

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty SegmentedQueue")
        return self.segments[0][0]

    def is_empty(self):
        return self.total_size == 0

    def size(self):
        return self.total_size

    def segment_size(self):
        return len(self.segments[-1])


# Example usage:
sq = SegmentedQueue(segment_capacity=3)
sq.enqueue(1)
sq.enqueue(2)
sq.enqueue(3)
sq.enqueue(4)
print(sq.dequeue())  # Output: 1
print(sq.peek())  # Output: 2
print(sq.size())  # Output: 3
print(sq.segment_size())  # Output: 1 (only one element in the current segment)
