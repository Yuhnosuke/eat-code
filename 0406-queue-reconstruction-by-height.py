class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        length = len(people)
        ans = [None] * length

        people.sort()

        for height, people_in_front in people:
            # index for insertion
            i = 0
            # counter for the number of people who have a height greater than or equal to
            j = -1

            while i < length:
                if not ans[i] or ans[i][0] == height:
                    j += 1

                if j == people_in_front:
                    break

                i += 1

            ans[i] = [height, people_in_front]

        return ans
