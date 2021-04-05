"insertion_sort file"

from unorderedlist import UnorderedList

def insertion_sort(items):
    """ Insertion sort """
    for i in range(1, items.size()):
        j = i
        while j > 0 and items.get(j) < items.get(j-1):
            #items[j], items[j-1] = items[j-1], items[j]
            value_j = items.get(j)
            value_jminus = items.get(j-1)

            items.set(j, value_jminus)
            items.set(j-1, value_j)

            j -= 1

    return items




def recursive_insertion_sort(items, n):
    """ recursive inertion sort"""
    #basfall
    if n <= 1:
        return None
    # sorterar förs n-1 element
    recursive_insertion_sort(items, n-1)
    # tilldelar sista och näst sita elementet temp-variabler
    last = items.get(n-1)
    j = n-2

    while j >= 0 and items.get(j) > last:
        value_j = items.get(j)
        #value_jplus = items.get(j+1)
        items.set(j+1, value_j)

        j -= 1

    items.set(j+1, last)
    return items




if __name__ == "__main__":

    lista = UnorderedList()
    lista.append(1)
    lista.append(2)
    lista.append(1)
    lista.append(4)
    lista.append(5)
    print(lista.print_list())

    new = (insertion_sort(lista))
    print(new.print_list())
