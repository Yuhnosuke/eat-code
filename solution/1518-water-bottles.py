class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk_bottles = 0
        empty_bottles = 0

        while numBottles > 0:
            drunk_bottles += 1
            empty_bottles += 1

            numBottles -= 1

            if empty_bottles == numExchange:
                numBottles += 1
                empty_bottles = 0

        return drunk_bottles


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed = 0

        while numBottles >= numExchange:
            consumed += numExchange
            numBottles -= numExchange

            numBottles += 1

        return consumed + numBottles
