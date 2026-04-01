class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        results = []

        if node.is_end:
            results.append(prefix)

        for char, child in node.children.items():
            results.extend(self._collect_words(child, prefix + char))

        return results