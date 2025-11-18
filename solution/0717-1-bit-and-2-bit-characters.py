class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        char_start_idx = 0

        while char_start_idx < len(bits) - 1:
            if bits[char_start_idx] == 0:
                char_start_idx += 1
            else:
                char_start_idx += 2

        return char_start_idx == len(bits) - 1
