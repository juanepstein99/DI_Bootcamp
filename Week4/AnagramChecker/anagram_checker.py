class AnagramChecker:
    def __init__(self, filename="word_list.txt"):
        self.words = []

        with open(filename, "r") as file:
            for line in file:
                self.words.append(line.strip().lower())

    def is_valid_word(self, word):
        word = word.lower().strip()
        return word in self.words

    def is_anagram(self, word1, word2):
        if len(word1) != len(word2):
            return False
        return sorted(word1) == sorted(word2)

    def get_anagrams(self, word):
        word = word.lower().strip()
        anagrams = []

        for w in self.words:
            if w != word and self.is_anagram(word, w):
                anagrams.append(w)

        return anagrams
