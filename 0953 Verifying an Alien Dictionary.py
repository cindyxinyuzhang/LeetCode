class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alien_order = {char : i for i, char in enumerate(order)}
        
        def isSorted(word1, word2):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    return alien_order[char1] < alien_order[char2]
            return len(word1) <= len(word2)
        
        return all(isSorted(words[i], words[i+1]) for i in range(len(words)-1))
