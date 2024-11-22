class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        # endWord에서 BeginWord까지의 단어 거리를 설정한다.
        dist = {endWord: 0}
        q = deque()
        q.append((endWord, 0))
        words = set(wordList)

        # 입력 단어와 한 글자씩 다른 가능한 모든 단어를 생성한다.
        def nextWords(word):
            result = []
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c == word[i]:
                        continue
                    w = word[:i] + c + word[i + 1:]
                    if w in words or w == beginWord:
                        result.append(w)
            return result

        # BFS
        while q:
            word, distance = q.popleft()
            if word == beginWord:
                break
            for w in nextWords(word):
                if w not in dist:
                    dist[w] = 1 + distance
                    q.append((w, 1 + distance))

        solution = []

        # DFS를 사용하여 BeginWord에서 endWord까지의 모든 경로를 계산한다.
        def dfs(word, res):
            if word == endWord:
                solution.append(res[:])
                return
            for w in nextWords(word):
                if w not in dist:
                    continue
                if dist[w] == (dist[word] - 1):  # 현재 단어와 거리가 인접한 다음 단어만 고려
                    res.append(w)
                    dfs(w, res)
                    res.pop()

        dfs(beginWord, [beginWord])
        return solution
