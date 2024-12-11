import unittest

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

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_basic_operations(self):
        # Basic insertion and search
        self.trie.insert("hello")
        self.assertTrue(self.trie.search("hello"))
        self.assertFalse(self.trie.search("hell"))
        
    def test_empty_strings(self):
        # Empty string handling
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertEqual(self.trie.starts_with(""), [""])
        
    def test_duplicate_insertions(self):
        # Duplicate insertions
        self.trie.insert("cat")
        self.trie.insert("cat")
        self.assertTrue(self.trie.search("cat"))
        self.assertEqual(self.trie.starts_with("ca"), ["cat"])
        
    def test_prefix_operations(self):
        # Prefix testing
        self.trie.insert("cat")
        self.trie.insert("cats")
        self.trie.insert("catch")
        expected = ["cat", "cats", "catch"]
        self.assertEqual(sorted(self.trie.starts_with("cat")), sorted(expected))
        
    def test_nonexistent_prefixes(self):
        # Non-existent prefixes
        self.assertEqual(self.trie.starts_with("xyz"), [])
        self.assertFalse(self.trie.search("xyz"))
        
    def test_special_characters(self):
        # Special characters handling
        special_word = "hello#@$%^"
        self.trie.insert(special_word)
        self.assertTrue(self.trie.search(special_word))
        
    def test_case_sensitivity(self):
        # Case sensitivity
        self.trie.insert("Hello")
        self.assertTrue(self.trie.search("Hello"))
        self.assertFalse(self.trie.search("hello"))
        
    def test_long_strings(self):
        # Long string handling
        long_string = "a" * 1000
        self.trie.insert(long_string)
        self.assertTrue(self.trie.search(long_string))
        
    def test_unicode_characters(self):
        # Unicode character handling
        unicode_word = "héllö"
        self.trie.insert(unicode_word)
        self.assertTrue(self.trie.search(unicode_word))

if __name__ == "__main__":
    unittest.main()