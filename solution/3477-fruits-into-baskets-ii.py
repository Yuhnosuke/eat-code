class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed_indices = set()
        n = len(fruits)

        for i in range(n):
            fruit = fruits[i]

            for j in range(n):
                if baskets[j] >= fruit and j not in placed_indices:
                    placed_indices.add(j)
                    break

        return n - len(placed_indices)
