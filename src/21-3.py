import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False  # 단어 완성 여부(단어 끝) 확인


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True  # 단어 끝에 도달했을 때 True로 설정

    def search(self, word):
        node = self.root
        return self.dfs(word, node)

    def startsWith(self, prefix):
        node = self.root
        return self.dfs(prefix, node, False)

    def dfs(self, string, node, is_word_given=True):
        # is_word_given이 True인 경우: 단어를 찾는다.
        # is_word_given이 False인 경우: 접두사를 찾는다.
        for i, c in enumerate(string):
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word if is_word_given else True
