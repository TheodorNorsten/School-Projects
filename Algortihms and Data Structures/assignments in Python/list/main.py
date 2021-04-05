" Main file"
from unorderedlist import UnorderedList
from errors import EmptyListException, KeyErrorException, IndexErrorException

class Handler():
    """initiation of Handler class, containging a infinity while loop,
    contaninga meny of all methods in the unorderedlist class"""

    def __init__(self):
        "init method, creats list class"
        self.node_list = UnorderedList()

        while True:

            self.menu()

            choice = input("Välj ett alternativ ")
            while not self.try_input(choice):
                print(" input måste vara en siffra")
                choice = input("Välj ett alternativ ")

            choice = int(choice)

            if choice == 1:
                self.choice_one()


            if choice == 2:
                self.choice_two()


            if choice == 3:
                self.choice_three()


            if choice == 4:

                self.choice_four()

            if choice == 5:

                self.choice_five()


            if choice == 6:
                self.choice_six()


            if choice == 7:
                self.choice_seven()


            if choice == 8:
                break




    @staticmethod
    def menu():
        "meny method, gets printed in while loop"

        print('1. Lägg till värde')
        print('2. tar bort en Nod')
        print('3. ändra data för nod')
        print('4. storlek på listan')
        print('5. Returnerar värde på index')
        print('6. Returnerar index av värde')
        print('7. skriver ut listans innehåll')
        print('8. Avsluta')



    @staticmethod
    def try_input(choice):
        "error handler, checks that input for variable 'choice' is int"
        try:
            int(choice)
            return True
        except ValueError:
            return False


    def choice_one(self):
        """ method for appending element to list"""

        data = input("värde ")
        self.node_list.append(data)


    def choice_two(self):
        """ method for removing element to list"""

        data = input("värde ")
        try:
            self.node_list.remove(data)
        except (KeyErrorException, EmptyListException):
            print("Error: lista tom eller data existerar ej, försök igen")




    def choice_three(self):
        """ method for change value of index element """

        try:
            index = int(input('skriv index på nod du vill byta data på '))
            data = input(' skriv data du vill ändra värdet på ')
        except ValueError:
            print(" value input måste vara siffra ")
            return

        try:
            self.node_list.set(index, data)
        except (IndexErrorException, EmptyListException):
            print("Error: lista tom eller index existerar ej, försök igen")



    def choice_four(self):
        """ method for printing out size of list element to list"""
        print("size ", self.node_list.size())



    def choice_five(self):
        """ returning value of input index"""

        try:
            index = int(input('skriv index på nod du vill returnera värde '))
        except ValueError:
            print("index måste vara en siffra")
            return

        try:
            print(self.node_list.get(index))
        except (IndexErrorException, EmptyListException):
            print("Error: lista tom eller data existerar ej, försök igen")


    def choice_six(self):
        """ returning index of input element"""

        value = input(' skriv värde vars index ska returneras ')

        try:
            print(self.node_list.index_of(value))
        except (KeyErrorException, EmptyListException):
            print("Error: lista tom eller index existerar ej, försök igen")



    def choice_seven(self):
        """ method for printing out all elements in list"""
        print("lista: ", self.node_list.print_list())








if __name__ == "__main__":
    x = Handler()
