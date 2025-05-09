# This is better than below in my opinion.
class MinStack:

    def __init__(self):
        self.stack = []
        # another stack to record min value corresponding to each value of stack
        self.current_min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.current_min_stack:
            self.current_min_stack.append(val)
        else:
            val = min(val, self.getMin())
            self.current_min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.current_min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.current_min_stack:
            return self.current_min_stack[-1]


# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_order_stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#         if not self.min_order_stack:
#             self.min_order_stack.append(val)
#         else:
#             if self.getMin() > val:
#                 self.min_order_stack.append(val)
#             else:
#                 popped = self.min_order_stack.pop()
#                 self.min_order_stack.append(val)
#                 self.min_order_stack.append(popped)

#     def pop(self) -> None:
#         popped = self.stack.pop()
#         self.min_order_stack.remove(popped)

#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1]

#     def getMin(self) -> int:
#         if self.min_order_stack:
#             return self.min_order_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
