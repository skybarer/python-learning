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
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return self.head
        else:
            temp.next = self.head
            return temp

    def insert_at_position(self, pos, data):
        temp = Node(data)
        if pos == 1:
            temp.next = self.head
            return temp
        curr = self.head
        for i in range(pos - 2):
            curr = curr.next
            if curr is None:
                return self.head
        temp.next = curr.next
        curr.next = temp
        return self.head

    def delete(self, data):
        pass

    def delete_from_beginning(self):
        if self.head is None:
            return None
        else:
            return self.head.next

    def delete_from_last(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return None
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def sort_insert(self, data):
        temp = Node(data)
        if self.head is None:
            return temp
        elif data < self.head.data:
            temp.next = self.head
            return temp
        else:
            curr = self.head
            while curr.next is not None and curr.next.data < data:
                curr = curr.next
            temp.next = curr.next
            curr.next = temp
            return self.head

    def search(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr
        return None

    def reverse(self):
        stack = []
        curr = self.head
        while curr is not None:
            stack.append(curr.data)
            curr = curr.next
        curr = self.head
        while curr is not Node:
            curr.data = stack.pop()
            curr = curr.next
        return self.head

