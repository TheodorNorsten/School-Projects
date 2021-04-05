"Test file for Trie class"
import unittest
from node import Node
from trie import Trie
from errors import SearchMiss


class TestTrie(unittest.TestCase):
    "initiation of test class"

    def setUp(self):
        """ Create object for all tests """
        self.trie = Trie()


    def tearDown(self):
        """ Remove dependencies after test """
        self.trie = None


    def test_is_instance_trie(self):
        """ Test that trie is instance of Trie class """
        self.assertIsInstance(self.trie, Trie)


    def test_is_instance_node(self):
        """ Test that node in trie is instance of Node class """
        self.trie.insert('hudkins')
        node = self.trie.root.children["h"]

        self.assertIsInstance(node, Node)



    def test_insert_root(self):
        """ Test that root node contains correct children after insertion """

        seq = ["hudkins", "vardy", "yamagani", "appreciated", "surinaams"]
        for i in seq:
            self.trie.insert(i)

        root_children = []
        for key in self.trie.root.children:
            root_children.append(key)

        self.assertEqual(root_children, ['h', 'v', 'y', 'a', 's'])



    def test_word_exist_correct(self):
        """ Test that trie returns True when word exist """
        seq = ["hudkins", "vardy", "yamagani", "appreciated", "surinaams"]
        for i in seq:
            self.trie.insert(i)

        self.assertTrue(self.trie.word_exist("hudkins"))


    def test_word_exist_exception(self):
        """ Test that Exception raises when word dont exist in trie """

        seq = ["hudkins", "vardy", "yamagani", "appreciated", "surinaams"]
        for i in seq:
            self.trie.insert(i)

        with self.assertRaises(SearchMiss) as _:
            self.trie.word_exist("angry")
            self.trie.word_exist("vi")
            self.trie.word_exist("huda")
            self.trie.word_exist("vardys")



    def test_prefix_search_correct(self):
        """ Test that trie returns correct when prefix exist """
        seq = ["hudkins", "vardy", "anticyclic", "androlepsy", "surinaams"]
        for i in seq:
            self.trie.insert(i)

        self.assertEqual(self.trie.prefix_search('an'), ["anticyclic", "androlepsy"])
        self.assertEqual(self.trie.prefix_search('hud'), ['hudkins'])



    def test_prefix_search_false(self):
        """ Test that trie returns False when prefix exist in trie
        and no other words has it as prefix """

        seq = ["hudkins", "vardy", "anticyclic", "androlepsy", "surinaams", "aaa"]
        for i in seq:
            self.trie.insert(i)

        self.assertFalse(self.trie.prefix_search("aaa"))



    def test_prefix_search_exception(self):
        """ Test that trie raises exception if no word with given prefix exist"""

        seq = ["hudkins", "vardy", "anticyclic", "androlepsy", "surinaams", "aaa"]
        for i in seq:
            self.trie.insert(i)

        with self.assertRaises(SearchMiss) as _:
            self.trie.prefix_search("angry")
            self.trie.prefix_search("vi")
            self.trie.prefix_search("huda")
            self.trie.prefix_search("aae")



    def test_remove_no_children(self):
        " Test that trie removes correct with word with no children"

        seq = ["hudkins", "vardy", "anticyclic", "androlepsy", "surinaams", "aaa"]
        for i in seq:
            self.trie.insert(i)

        self.trie.word_remove("vardy")
        self.trie.word_remove("androlepsy")

        with self.assertRaises(SearchMiss) as _:
            self.trie.word_exist("vardy")
            self.trie.word_exist("androlepsy")





if __name__ == "__main__":
    unittest.main(verbosity=3)
