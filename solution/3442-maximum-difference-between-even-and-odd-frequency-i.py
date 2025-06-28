class Solution:
    def maxDifference(self, s: str) -> int:
        ch_to_freq = Counter(s)

        freqencies = ch_to_freq.values()
        odd_frequencies = filter(lambda x: x % 2 == 1, freqencies)
        even_frequencies = filter(lambda x: x % 2 == 0, freqencies)

        return max(odd_frequencies) - min(even_frequencies)
