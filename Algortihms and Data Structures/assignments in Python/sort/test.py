"Test file for methods in the UnorderedList class"
import unittest
from node import Node
from unorderedlist import UnorderedList
from sort import recursive_insertion_sort
from errors import EmptyListException, KeyErrorException, IndexErrorException


class TestUnorderedList(unittest.TestCase):
    "initiation of test class."
    node_1 = 1
    node_2 = 2
    node_3 = 3

    def setUp(self):
        """ Create object for all tests """
        self.node_list = UnorderedList()


    def tearDown(self):
        """ Remove dependencies after test """
        self.node_list = None



    def test_append(self):
        """
        Test that one can add a node to the list.
        """
        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        self.assertIsInstance(self.node_list.head, Node)
        self.assertEqual(self.node_list.head.data, TestUnorderedList.node_3)



    def test_set_correct(self):
        """
        Test that one can change value of node in list.
        """
        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        self.node_list.set(1, 10)
        self.assertEqual(self.node_list.head.next.data, 10)


    def test_set_fail(self):
        """
        Test that exception raises when changing value for empty list
        and when index not exist.
        """

        with self.assertRaises(EmptyListException) as _:
            self.node_list.set(1, 10)

        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        with self.assertRaises(IndexErrorException) as _:
            self.node_list.set(5, 10)




    def test_get_correct(self):
        """
        Test that get method returns the correct value of index.
        """
        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        self.node_list.get(1)
        self.assertEqual(self.node_list.get(1), TestUnorderedList.node_2)

    def test_get_fail(self):
        """
        Test that get method raises exeptions when list empty and index dont exist.
        """
        with self.assertRaises(EmptyListException) as _:
            self.node_list.get(1)

        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        with self.assertRaises(IndexErrorException) as _:
            self.node_list.get(4)


    def test_index_of_correct(self):
        """
        Test that index_of method returns the correct value.
        """
        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        self.assertEqual(self.node_list.index_of(1), 2)


    def test_index_of_fail(self):
        """
        Test that that index_of method raises exeptions,
         when list empty and value dont exist.
        """
        with self.assertRaises(EmptyListException) as _:
            self.node_list.index_of(1)

        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        with self.assertRaises(KeyErrorException) as _:
            self.node_list.index_of(5)



    def test_remove_correct_onenode(self):
        """
        Test that remove method returns correct with one node in list.
        """
        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.remove(1)

        self.assertEqual(self.node_list.head, None)
        self.assertEqual(self.node_list.last, None)


    def test_remove_correct_nodelist(self):
        """
        Test that remove method returns the correct value in list of nodes.
        when removing first, middle and last node. """
        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        self.node_list.remove(3)
        self.assertEqual(self.node_list.head.data, 2)

        self.node_list.append(3)
        self.node_list.remove(2)
        self.assertEqual(self.node_list.head.next.data, 1)

        self.node_list.append(2)
        self.node_list.remove(1)
        self.assertEqual(self.node_list.last.data, 3)




    def test_remove_fail(self):
        """
        Test that remove method raises exception when list empty and value
        not found."""
        with self.assertRaises(EmptyListException) as _:
            self.node_list.remove(1)

        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        with self.assertRaises(KeyErrorException) as _:
            self.node_list.remove(5)




    def test_recursive_sort_correct(self):
        """
        Test that recursive insertion sort function returns correct.
        """
        self.node_list.append(TestUnorderedList.node_1)
        self.node_list.append(TestUnorderedList.node_2)
        self.node_list.append(TestUnorderedList.node_3)

        n = self.node_list.size()

        recursive_insertion_sort(self.node_list, n)
        self.assertEqual(self.node_list.print_list(), [1, 2, 3])


    def test_recursive_sort_empty(self):
        """
        Test that recursive insertion sort function returns correct,
        when list empty.
        """
        n = self.node_list.size()
        self.assertEqual(recursive_insertion_sort(self.node_list, n), None)


    def test_recursive_sort_one_element(self):
        """
        Test that recursive insertion sort function returns correct,
        when list has 1 element.
        """
        self.node_list.append(TestUnorderedList.node_1)
        n = self.node_list.size()
        self.assertEqual(recursive_insertion_sort(self.node_list, n), None)




if __name__ == "__main__":
    unittest.main(verbosity=3)
