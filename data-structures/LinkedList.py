class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(data)
        return curr

    def insert_at_front(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head
        else:
            temp = Node(data)
            temp.next = self.head
            return temp

    def delete(self, data):
        pass

    def delete_from_beginning(self):
        pass

    def search(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr
        return None
