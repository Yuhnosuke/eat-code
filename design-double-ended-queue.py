class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None and self.tail == None

    def append(self, value: int) -> None:
        node = ListNode(value)

        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def appendleft(self, value: int) -> None:
        node = ListNode(value)

        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def pop(self) -> int:
        if not self.tail:
            return -1

        val = self.tail.val
        self.tail = self.tail.prev

        if not self.tail:
            self.head = None
        else:
            self.tail.next = None
        return val

    def popleft(self) -> int:
        if not self.head:
            return -1

        val = self.head.val
        self.head = self.head.next

        if not self.head:
            self.tail = None
        else:
            self.head.prev = None

        return val
