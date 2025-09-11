class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]

        filtered = sorted(filter(lambda x: x in vowels, s))
        fi = 0
        t = []
        for i in range(len(s)):
            if s[i] not in vowels:
                t.append(s[i])
            else:
                t.append(filtered[fi])
                fi += 1
        return "".join(t)
