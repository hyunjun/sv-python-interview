class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        """
        데이터 구조 초기화
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        단어 삽입
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return cur.isWord
            if word[i] == ".":
                for child in cur.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if word[i] not in cur.children:
                    return False
                return dfs(i + 1, cur.children[word[i]])

        return dfs(0, self.root)
