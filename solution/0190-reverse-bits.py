class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0

        for bit_position in range(32):
            shifted_input = n >> bit_position
            extracted_bit = shifted_input & 1

            reversed_position = 31 - bit_position
            reversed_bits += extracted_bit << reversed_position

        return reversed_bits
