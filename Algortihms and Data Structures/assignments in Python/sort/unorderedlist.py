"file containging UnorderedList class"
from node import Node
from errors import EmptyListException, KeyErrorException, IndexErrorException

class UnorderedList():
    "initiation of UnorderedList class created of  a linked list"

    def __init__(self):
        "initiation of the first(head) and last node in the linked list"
        self.head = None
        self.last = None


    def append(self, data):
        "method thats append new node to list"
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            new_node.next = self.head
            self.head = new_node



    def set(self, index, data):
        """method that changes data of node given input index,
        raises exception if list empty or index not exist"""

        if self.head is not None:
            p = self.head
            q = self.head.next
            count = 0

            while q is not None and count < index:
                p = p.next
                q = q.next
                count += 1

            if count == index:
                p.data = data

            else:
                raise IndexErrorException

        else:
            raise EmptyListException


    def size(self):
        "metod, returns the number of nodes."
        q = self.head
        count = 0
        while q is not None:
            count += 1
            q = q.next
        return count



    def get(self, index):
        """ method, returns the node.data given input index else raie exception
        if list empty or index not exist."""

        if self.head is not None:
            p = self.head
            q = self.head.next
            count = 0

            while q is not None and count < index:
                p = p.next
                q = q.next
                count += 1

            if count == index:
                return p.data


            raise IndexErrorException


        raise EmptyListException


    def index_of(self, value):
        """ method, returns the index given input value of node,
        else raie exception if list empty or value not exist."""

        if self.head is not None:
            p = self.head
            q = self.head.next
            count = 0
            if p.data == value:
                return count

            while q is not None and p.data != value:
                p = p.next
                q = q.next
                count += 1

            if p.data == value:
                return count


            raise KeyErrorException


        raise EmptyListException




    def print_list(self):
        "Method, returns the list of nodes."
        node = self.head
        list_node = []
        while node:
            #print(node.data)
            list_node.append(node.data)
            node = node.next
        return list_node





    def remove(self, data):
        """method removes node given input data, else raises exception if
        empty list or data not exist in node. """

        if self.head is not None:
            p = self.head
            q = self.head.next

            if p.data == data:
                if q is not None:
                    self.head = q
                    del p
                    return

                self.head = None
                self.last = None
                del p
                return

            while q is not None and q.data != data:
                p = p.next
                q = q.next


            if q is None:
                raise KeyErrorException

            if q.next is None:
                p.next = q.next
                self.last = p
                del q
                return


            p.next = q.next
            del q
            return



        raise EmptyListException






if __name__ == "__main__":
    pass
