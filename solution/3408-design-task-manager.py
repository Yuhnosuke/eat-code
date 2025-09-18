class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.max_heap = []  # (priority, task_id)
        self.task_to_priority = {}  # task_id -> priority
        self.task_to_user = {}  # task_id -> user_id

        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.max_heap, (-priority, -taskId))
        self.task_to_priority[taskId] = priority
        self.task_to_user[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.max_heap, (-newPriority, -taskId))
        self.task_to_priority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.task_to_priority[taskId] = -1

    def execTop(self) -> int:
        while self.max_heap:
            popped = heapq.heappop(self.max_heap)
            priority, task_id = -popped[0], -popped[1]

            if self.task_to_priority.get(task_id, -2) == priority:
                self.rmv(task_id)
                return self.task_to_user.get(task_id, -1)

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
