"fil för huvudprogram - ska innehålla klassen Spellchecker"
from trie import Trie
from errors import SearchMiss

class SpellChecker:
    "Initiation of spellChecker class"

    def __init__(self):
        "init method creat Trie object"

        self.trie_nodes = Trie()
        self.load_data()

        while True:

            self.meny()
            choice = input("what to do ")   #str


            if choice == "1":
                self.find_word()


            elif choice == "2":
                prev = ""

                prefix = input("Enter three letters then one letter at the time: ")
                try:
                    word_list = self.trie_nodes.prefix_search(prefix)

                    if word_list is False:
                        print(prefix, " is the only word with prefix")
                        continue

                    for word in word_list:
                        print(word)
                    prev += prefix

                except SearchMiss:
                    print("ERROR: No word starts with {p} in wordlist".format(p=prefix))
                    continue

                self.find_prefix(prev)


            elif choice == "3":
                self.change_filename()


            elif choice == "4":
                all_words_list = self.print_all_words()
                all_words_list.sort()
                for i in all_words_list:
                    print(i)

            elif choice == "5":
                self.remove_word()


            elif choice == "q":
                print("Program ended, Welcome back!")
                break


            else:
                print(" choice dont exist in meny, try agian! ")






    def load_data(self):
        "Method for loading file and inserting to trie "

        with open("tiny_dictionary.txt", 'r') as file:
            for line in file:
                line = line.strip()
                self.trie_nodes.insert(line)



    def find_word(self):
        "Method for checking if word exist in trie"

        word = input("enter word to check in wordlist ")
        try:
            self.trie_nodes.word_exist(word)
            print("{w} exist in wordlist! ".format(w=word))

        except SearchMiss:
            print(" ERROR: {w} dont exist in wordlist".format(w=word))




    def find_prefix(self, prev):
        "Method for finding words with input prefix"

        while True:

            next_letter = input("Enter another letter or quit {p}".format(
                p=prev))

            if next_letter != "quit":
                try:
                    word_list = self.trie_nodes.prefix_search(prev + next_letter)

                    if word_list is False:
                        return

                    if len(word_list) > 10:
                        for i in range(10):
                            print(word_list[i])

                    else:
                        for word in word_list:
                            print(word)

                    prev += next_letter

                except SearchMiss:
                    print("ERROR: No word starts with {p} in wordlist".format(
                        p=(prev + next_letter)))
                    continue

            else:
                break

            input("press enter")






    def change_filename(self):
        "Method for changing file, new trie creats and inserts file content to it"

        filename = input("Enter new file name ")
        self.trie_nodes = Trie()
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                self.trie_nodes.insert(line)






    def print_all_words(self):
        "Method for printing out all words in file"

        word_list = []
        root = self.trie_nodes.root
        for char in root.children.keys():
            current_node = root.children[char]
            temp_word = " "
            temp_word = current_node.value

            self.trie_nodes.recursion_prefix_search(current_node, temp_word, word_list)


        return word_list





    def remove_word(self):
        "Method for removing word from trie"

        word = input("enter word to remove ")
        try:
            self.trie_nodes.word_exist(word)
            self.trie_nodes.word_remove(word)
            print("{w} has been removed".format(w=word))

        except SearchMiss:
            print(" ERROR: {w} dont exist in wordlist".format(w=word))





    @staticmethod
    def meny():
        "staticmethod for printing of meny option"

        print("1: Look up word")
        print("2: Get word suggestion")
        print("3: Change dictionary")
        print("4: Print all words")
        print("5: remove word from word list")
        print("q: exit")











if __name__ == "__main__":

    tri = SpellChecker()
