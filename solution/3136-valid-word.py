class Solution:
    def isValid(self, word: str) -> bool:

        def is_length_valid(word):
            return len(word) >= 3

        def is_alpha_num_valid(word):
            return word.isalnum()

        vowels = set("aiueo")

        def is_vowel_valid(word):
            for vowel in vowels:
                if vowel in word or vowel.upper() in word:
                    return True
            return False

        def is_consonant_valid(word):
            consonants = set("abcdefghijklmnopqrstuvwxyz") - vowels
            for consonant in consonants:
                if consonant in word or consonant.upper() in word:
                    return True
            return False

        return (
            is_length_valid(word)
            and is_alpha_num_valid(word)
            and is_vowel_valid(word)
            and is_consonant_valid(word)
        )
