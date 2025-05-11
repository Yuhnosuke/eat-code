from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students)
        queue = deque(students)

        answer = length

        for sandwich in sandwiches:
            count = 0

            # case that a student does not prefer the sandwich
            while count < length and queue[0] != sandwich:
                popped = queue.popleft()
                queue.append(popped)
                count += 1

            # case prefer
            if queue[0] == sandwich:
                queue.popleft()
                answer -= 1
            else:
                break

        return answer
