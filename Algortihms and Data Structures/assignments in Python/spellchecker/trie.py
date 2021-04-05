"klass/kod för trie datastruktur."
from node import Node
from errors import SearchMiss




class Trie:
    "Class initiation of Trie structure"

    def __init__(self):
        "Initiation root attribute"
        self.root = Node()  # root node for Trie object
        self.count = 0      # help attribute for word_remove function




    def insert(self, word):
        "Method for inserting word to trie"
        current_node = self.root
        for letter in word:
            if not letter in current_node.children.keys():
                current_node.children[letter] = Node(letter)

            current_node = current_node.children[letter]
        current_node.end_of_word = True



    def word_exist(self, word):
        """Method for checking if word exist in Trie, than return True else
        raises Exception. """

        current_node = self.root

        for letter in word:
            if not letter in current_node.children.keys():
                raise SearchMiss

            current_node = current_node.children[letter]

        if current_node.end_of_word:
            return current_node.end_of_word

        raise SearchMiss




    def prefix_search(self, prefix):
        """ Method for returning words with prefix equal to input,
         uses recursion method, than returns list of corresponding words,
         if prefix dont exist - raises exception else return False"""

        current_node = self.root
        temp_word = ""

        for letter in prefix:
            if letter not in current_node.children.keys():
                #om det inte existerar ord med detta prefix
                raise SearchMiss

            temp_word += letter
            current_node = current_node.children[letter]

            #kontrollera om current_node har children eller ej
            if current_node.end_of_word and not current_node.children:
                #finns inga andra ord med detta prefix
                return False


        word_list = []
        self.recursion_prefix_search(current_node, temp_word, word_list)
        return word_list






    def recursion_prefix_search(self, node, word, word_list):
        "recursion method for prefix_search method"

        if node.end_of_word:
            word_list.append(word)

        for letter, child_node in node.children.items():
            self.recursion_prefix_search(child_node, word + letter, word_list)



    def word_remove(self, word):
        """ Method for removing word from trie. if last node(letter) in word
        has children than only change end_of_word attribute to False, else
        also remove node and use recursion to check if parent node have children
        if not remove those as well. """

        current_node = self.root
        previous_node = None

        for letter in word:
            previous_node = current_node
            current_node = current_node.children[letter]

        self.count += 1

        #current_node har inga barn - ta bort current node
        if not current_node.children:
            current_node.end_of_word = False
            previous_node.children.pop(current_node.value)
            word = word[:-1]


            if len(word) >= 1:
                self.word_remove(word)

        #current_node har barn
        else:
            if self.count == 1:
                # första iterationen - ändrar endast end_of_word attribute.
                current_node.end_of_word = False

        self.count = 0

if __name__ == "__main__":
    pass
