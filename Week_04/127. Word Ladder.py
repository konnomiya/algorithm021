from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        bfs = deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, level = bfs.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordSet and new_word != word:
                        bfs.append((new_word, level + 1))
                        wordSet.remove(new_word)
        return 0
