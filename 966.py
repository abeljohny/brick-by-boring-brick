class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        def mask_vowels(word: str):
            return ''.join('*' if ch in 'aeiou' else ch for ch in word)

        wordset = set(wordlist)
        wordmap_lower = dict()
        wordmap_devowel = dict()
        for word in wordlist:
            word_lower = word.lower()
            wordmap_lower.setdefault(word_lower, word)
            wordmap_devowel.setdefault(mask_vowels(word_lower), word)

        def solve(query: str) -> str:
            if query in wordset:
                return query
            query_lower = query.lower()
            if query_lower in wordmap_lower:
                return wordmap_lower[query_lower]
            if mask_vowels(query_lower) in wordmap_devowel:
                return wordmap_devowel[mask_vowels(query_lower)]
            return ''

        return list(map(solve, queries))
