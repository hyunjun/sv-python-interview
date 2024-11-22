def chain_from_sub(self, word, all_words, chain_length, cache):
    if not word:
        # 비어 있으면 길이를 반환한다.
        return chain_length - 1

    # 단어를 방문한 경우 해당 단어의 길이를 반환한다.
    if word in cache:
        return cache[word] + chain_length - 1

    # 단어가 사전에 없으면 -1을 반환한다.
    if word not in all_words:
        return -1

    max_chain_length = 0
    for i in range(len(word)):
        new_word = word[:i] + word[i + 1:]
        current_chain_length = self.chain_from_sub(
            new_word, all_words, chain_length + 1, cache
        )
        max_chain_length = max(max_chain_length, current_chain_length)

    cache[word] = max_chain_length
    return max_chain_length


def longest_subword_chain_sub(self, words):
    all_words = set()
    for w in words:
        all_words.add(w)

    max_chain_length = 0
    cache = {}
    for w in words:
        current_chain_length = self.chain_from_sub(w, all_words, 1, cache)
        if current_chain_length > max_chain_length:
            max_chain_length = current_chain_length

    return max_chain_length
