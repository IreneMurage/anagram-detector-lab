# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        self._sig = self._signature(word)

    @staticmethod
    def _signature(s: str):
        return tuple(sorted(s.lower()))

    def match(self, candidates):
        base = self.word.lower()
        results = []
        for w in candidates:
            if w.lower() == base:
                continue  # don't match the same word
            if self._signature(w) == self._sig:
                results.append(w)
        return results
