class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered_to_words = {}
        for word in strs:
            ordered = "".join(sorted(word))
            if ordered not in ordered_to_words:
                ordered_to_words[ordered] = []
            ordered_to_words[ordered].append(word)

        return list(ordered_to_words.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_strs = {"".join(sorted(word)): [] for word in strs}

        for word in strs:
            sorted_to_strs["".join(sorted(word))].append(word)

        return list(sorted_to_strs.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_to_words = defaultdict(list)

        for s in strs:
            f = [0] * 26

            for ch in s:
                i = ord(ch) - ord("a")
                f[i] += 1

            freq_to_words[tuple(f)].append(s)

        return list(freq_to_words.values())
