import heapq


class PrioritySet:
    def __init__(self):
        self.elements = {}  # Dictionary to store elements and their priorities
        self.heap = []  # Max-heap (simulated using min-heap with negative priorities)

    def insert(self, element, priority):
        if element in self.elements:
            self.change_priority(element, priority)
        else:
            self.elements[element] = priority
            heapq.heappush(self.heap, (-priority, element))

    def delete(self, element):
        if element in self.elements:
            del self.elements[element]
            # To delete from heap efficiently, mark as deleted (lazy deletion)

    def get_max(self):
        while self.heap:
            priority, element = self.heap[0]
            if element in self.elements and self.elements[element] == -priority:
                return element
            else:
                heapq.heappop(self.heap)
        return None

    def extract_max(self):
        while self.heap:
            priority, element = heapq.heappop(self.heap)
            if element in self.elements and self.elements[element] == -priority:
                del self.elements[element]
                return element
        return None

    def change_priority(self, element, new_priority):
        if element in self.elements:
            self.elements[element] = new_priority
            heapq.heappush(self.heap, (-new_priority, element))

    def contains(self, element):
        return element in self.elements


# Example Usage
priority_set = PrioritySet()
priority_set.insert("apple", 5)
priority_set.insert("banana", 3)
priority_set.insert("cherry", 7)

print(priority_set.get_max())  # Output: "cherry"
print(priority_set.extract_max())  # Output: "cherry"
print(priority_set.contains("banana"))  # Output: True
priority_set.change_priority("banana", 10)
print(priority_set.get_max())  # Output: "banana"
