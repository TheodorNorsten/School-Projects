"File containing Node class"

class Node:
    "Initiation of Class Node"
    def __init__(self, key, value, parent=None):
        "init method"
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


    def has_left_child(self):
        "method checks if node has left child"
        return self.left is not None


    def has_right_child(self):
        "method checks if node has right child"
        return self.right is not None


    def has_both_children(self):
        "method checks if node has left and right child"
        return self.has_left_child() and self.has_right_child()


    def has_parent(self):
        "method checks if node has left parent"
        return self.parent is not None


    def is_left_child(self):
        "method checks if node is left child"
        if self.key == self.parent.left.key:
            return True
        return False



    def is_right_child(self):
        "method checks if node is right child"
        if self.key == self.parent.right.key:
            return True
        return False



    def is_leaf(self):
        "method checks if node is leaf node"
        if self.left is None and self.right is None:
            return True
        return False



    def __lt__(self, other):
        "lt method for key attribute"
        if isinstance(other, Node):
            return self.key < other.key

        return self.key < other


    def __gt__(self, other):
        "gt method for key attribute"
        if isinstance(other, Node):
            return self.key > other.key

        return self.key > other


    def __eq__(self, other):
        "eq method for key attribute"
        if isinstance(other, Node):
            return self.key == other.key

        return self.key == other


if __name__ == "__main__":
    pass
