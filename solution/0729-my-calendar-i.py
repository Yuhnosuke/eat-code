# iteration
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:

        for booked_start, booked_end in self.events:
            # De Morgan's laws
            # if endTime > booked_start and booked_end > startTime:
            if not (endTime <= booked_start or booked_end <= startTime):
                return False

        self.events.append([startTime, endTime])
        return True


# Binary Search Tree
class TreeNode:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None

    def _insert(self, root, start, end):
        curr = root

        while True:
            if end <= curr.start:
                if not curr.left:
                    curr.left = TreeNode(start, end)
                    return True
                curr = curr.left
            elif curr.end <= start:
                if not curr.right:
                    curr.right = TreeNode(start, end)
                    return True
                curr = curr.right
            else:
                return False

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = TreeNode(startTime, endTime)
            return True

        return self._insert(self.root, startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
