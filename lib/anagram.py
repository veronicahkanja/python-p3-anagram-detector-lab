# your code goes here!


class Anagram:
    def __init__(self, word):
        # Store the original word in lowercase for easier comparison
        self.word = word.lower()

    def match(self, words):
        # List to store the matching anagrams
        matches = []
        
        for w in words:
            # Ignore case and do not match the word itself
            if w.lower() != self.word and sorted(w.lower()) == sorted(self.word):
                matches.append(w)
        
        return matches
