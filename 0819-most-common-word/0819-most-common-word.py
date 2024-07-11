from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban_set = set(banned)
        word_count = {}
        max_count = 0
        most_common_word = ''
        for word in paragraph.lower().split():
            word = ''.join(filter(str.isalnum, word))
            if word and word not in ban_set:
                word_count[word] = word_count.get(word, 0) + 1
                if word_count[word] > max_count:
                    max_count = word_count[word]
                    most_common_word = word
        return most_common_word