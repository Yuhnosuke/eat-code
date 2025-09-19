class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            elif n == 0:
                return True
            else:
                return False

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    ans += 1
            elif 0 < i < len(flowerbed) - 1:
                if (
                    flowerbed[i - 1] == 0
                    and flowerbed[i] == 0
                    and flowerbed[i + 1] == 0
                ):
                    flowerbed[i] = 1
                    ans += 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    ans += 1

        return ans >= n


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                is_left_empty = i == 0 or flowerbed[i - 1] == 0
                is_right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if is_left_empty and is_right_empty:
                    ans += 1
                    flowerbed[i] = 1

        return ans >= n
