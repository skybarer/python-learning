class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None and current.next.data != data:
                current = current.next
            if current.next is not None:
                current.next = current.next.next

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
sorted_list = SortedLinkedList()
sorted_list.insert(5)
sorted_list.insert(2)
sorted_list.insert(8)
sorted_list.insert(1)
sorted_list.insert(9)

sorted_list.display()  # Output: 1 2 5 8 9

print(sorted_list.search(5))  # Output: True
print(sorted_list.search(3))  # Output: False

sorted_list.delete(2)
sorted_list.display()  # Output: 1 5 8 9
