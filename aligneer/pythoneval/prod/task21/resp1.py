class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
  
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True
  
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
  
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_from_node(node, prefix)
  
    def _find_words_from_node(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._find_words_from_node(next_node, prefix + char))
        return words

trie = Trie()

# Test Case 1
trie.insert("")
assert trie.search("") == True  # or False, depending on the design decision

# Test Case 2
assert trie.starts_with("") == [""]  # or all words in the Trie

# Test Case 3
assert trie.search("nonexistent") == False

# Test Case 4
assert trie.starts_with("nonexistent") == []

# Test Case 5
trie.insert("word")
trie.insert("word")
assert trie.search("word") == True

# Test Case 6
assert trie.starts_with("wo") == ["word"]

# Test Case 7
trie.insert("Word")
assert trie.search("word") == False
assert trie.search("Word") == True

# Test Case 8
trie.insert("word123")
assert trie.search("word123") == True
assert trie.search("word") == False

# Test Case 9
long_word = "a" * 1000
trie.insert(long_word)
assert trie.search(long_word) == True

# Test Case 10
trie.insert("hello")
assert trie.search("hell") == False