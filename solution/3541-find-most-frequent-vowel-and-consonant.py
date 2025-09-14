class Solution:
    def maxFreqSum(self, s: str) -> int:
        ch_to_freq = {}

        for ch in s:
            if ch not in ch_to_freq:
                ch_to_freq[ch] = 0
            ch_to_freq[ch] += 1

        vowel_max, consonant_max = 0, 0
        vowels = "aiueo"

        for ch, freq in ch_to_freq.items():
            if ch in vowels:
                vowel_max = max(vowel_max, freq)
            else:
                consonant_max = max(consonant_max, freq)

        return vowel_max + consonant_max
