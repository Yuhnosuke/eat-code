class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: sorted str, value: original strs
        anagram_map = defaultdict(list)

        for st in strs:
            sorted_s = "".join(sorted(st))
            anagram_map[sorted_s].append(st)

        ans = []

        for grouped_strs in anagram_map.values():
            ans.append(grouped_strs)

        return ans


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_strs = {"".join(sorted(word)): [] for word in strs}

        for word in strs:
            sorted_to_strs["".join(sorted(word))].append(word)

        return list(sorted_to_strs.values())
