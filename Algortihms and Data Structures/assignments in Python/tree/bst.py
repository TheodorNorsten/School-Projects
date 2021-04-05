"File containing BinarySearchTree class"
from node import Node


class BinarySearchTree:
    "Initiation of tree class"

    def __init__(self):
        "init method"
        self.root = None


    def insert(self, key, value):
        "method for inserting node in tree, uses recursive function"
        if self.root is None:
            self.root = Node(key, value)

        self.recursion_insert(self.root, key, value)



    @classmethod
    def recursion_insert(cls, node, key, value):
        "classmethod recursive function for inserting new node"

        if key < node:
            if node.has_left_child():
                cls.recursion_insert(node.left, key, value)
            else:
                node.left = Node(key, value, node)

        elif key > node:
            if node.has_right_child():
                cls.recursion_insert(node.right, key, value)
            else:
                node.right = Node(key, value, node)

        else:
            node.value = value




    def inorder_traversal_print(self):
        "method for inorder print, uses recursive function."
        self.recursion_write(self.root)



    @classmethod
    def recursion_write(cls, node):
        "classmethod, recursive function for inorder printing."
        if node is None:
            return

        if node.has_left_child():
            cls.recursion_write(node.left)
        print(node.value)

        if node.has_right_child():
            cls.recursion_write(node.right)





    def get(self, key):
        "Get method, uses recursive function."
        if self.root is None:
            raise KeyError(" tree is empty")

        return self.recursion_find(self.root, key)




    @classmethod
    def recursion_find(cls, node, key):
        "classmethod, recursive function for getting node"

        if node is None:
            raise KeyError(" Node with key {n} dont exist in tree".format(n=key))

        if key > node:
            return cls.recursion_find(node.right, key)

        if key < node:
            return cls.recursion_find(node.left, key)

        return node.value



    def remove(self, key):
        "method for removing node in tree."
        if self.root is None:
            raise KeyError(" tree is empty")

        return self.recursion_remove(self.root, key)


    @staticmethod
    def find_succesor(node):
        "method for finding succesor_node."
        while node.left is not None:
            node = node.left
        return node


    def remove_leaf(self, node):
        "method for removing leaf node"

        if node.has_parent():

            if node is node.parent.left:
                node.parent.left = None
                node.parent = None

            elif node is node.parent.right:
                node.parent.right = None
                node.parent = None

        else:
            self.root = None


    @staticmethod
    def remove_both_children(succesor_node):
        "method for removing node with two child"

        if succesor_node.key > succesor_node.parent.key:
            succesor_node.parent.right = None

        elif succesor_node.key < succesor_node.parent.key:
            succesor_node.parent.left = None

        else:
            succesor_node.parent.right = None



    def remove_one_child(self, node):
        "method for removing node with one child"

        if node.parent is None:
            #root noden ska bort
            if node.has_right_child():
                node.right.parent = None
                self.root = node.right

            else:
                #self.node.left.parent = None
                node.right.parent = None
                self.root = node.left



        elif node.parent.left is not None:
            if node.has_left_child():
                node.parent.left = node.left
                node.left.parent = node.parent
            else:
                node.parent.left = node.right
                node.right.parent = node.parent


        else:
            if node.has_left_child():
                node.parent.right = node.left
                node.left.parent = node.parent
            else:
                node.parent.right = node.right
                node.right.parent = node.parent





    def recursion_remove(self, node, key):
        "recursive method for removing node in tree."

        if node is None:
            raise KeyError(" Node with key {n} dont exist in tree".format(n=key))

        if key > node:
            return self.recursion_remove(node.right, key)

        if key < node:
            return self.recursion_remove(node.left, key)


        #Hittat noden
        if key == node:
            node_removed = None

            #om leaf nod
            if node.is_leaf():
                self.remove_leaf(node)


            #två barn
            elif node.has_both_children():

                succesor_node = self.find_succesor(node.right)

                node_removed = node.value
                node.key = succesor_node.key
                node.value = succesor_node.value

                #omfördela parent - right till succesor_node potentiella barn
                if succesor_node.is_leaf():
                    #print(succesor_node.parent.left.key)
                    self.remove_both_children(succesor_node)

                else:
                    succesor_node.parent.left = succesor_node.right
                    succesor_node.right.parent = succesor_node.parent

            #one child
            else:
                self.remove_one_child(node)


        if node_removed is not None:
            return node_removed

        return node.value




if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(1, 'first')
    tree.insert(5, 'sec')
    tree.insert(2, 'thord')


    tree.inorder_traversal_print()
    print('\n')
    print(tree.remove(2))
    print('\n')
    tree.inorder_traversal_print()
