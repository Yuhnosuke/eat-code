class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty_bottles, bottles_drunk = 0, 0

        while numBottles > 0 or empty_bottles >= numExchange:

            numBottles -= 1
            empty_bottles += 1
            bottles_drunk += 1

            if empty_bottles >= numExchange:
                numBottles += 1
                empty_bottles -= numExchange
                numExchange += 1

        return bottles_drunk
