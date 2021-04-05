"Node klass"

class Node:
    "initiation of Node class"
    def __init__(self, value=None):
        "init method for initiation of class attributes"
        self.value = value      # str, storing character.
        self.end_of_word = False  # represents wether node is the last character in word.
        self.children = {}      # storing children as dic were key:char, value:Node object.




if __name__ == "__main__":
    pass
