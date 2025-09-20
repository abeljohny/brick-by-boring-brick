from dataclasses import dataclass, field

@dataclass
class _TrieNode:
    children: dict[str, '_TrieNode'] = field(default_factory=dict)
    is_word: bool = False


class Trie:

    def __init__(self):
        self._root = _TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._node_for(word)
        return bool(node and node.is_word)

    def startsWith(self, prefix: str) -> bool:
        return self._node_for(prefix) is not None

    def _node_for(self, s):
        node = self._root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert('apple')
# print(obj.search('apple'))
# print(obj.search('app'))
# print(obj.startsWith('app'))
# obj.insert('app')
