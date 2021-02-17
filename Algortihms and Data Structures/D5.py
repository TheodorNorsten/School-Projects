# Labb D5 Theodor Norsten
# uppgift implementation av ett binärt sökträd



''' Första uppgift skriva en klass för binärasökträd'''


class Node:
    ''' Klass Nod, skapar ny nod för varje element i trädet
    attributen: key,value, höger-pekar, vänster-pekare'''
    
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right= None




class Bintree:

    ''' Klass för Binära sökträdet, initierar trädet med rot elementet. '''
    

    def __init__(self):
        self.rot=None


    def store(self,key,value):
        '''Metod för att lagra ny nod, med key och value på rätt plats.
        Kallar på den rekursiva funktionen rekstore- som returnerar plats för ny nod'''
        
        self.rot= rekstore(self.rot,key,value)


    def search(self,key):

        '''Metoden kallar på den rekursiva funktionen reksearch och söker efter nyckel i trädet och returnerar tillhörande value.
        om nyckeln finns returneras värdet, annars KeyError'''
        
        
        nod= self.rot
        if nod == None:
            raise KeyError
        else:
            return reksearch(nod,key)

    

    def contains(self,key):

        ''' söker efter nyckel i trädet och returnerar True om nyckel finns annars, False. '''
        
        letar= True
        nod= self.rot
        while letar:
            if nod == None:
                return False

            if nod.key == key:
                return True

            if key < nod.key:
                nod=nod.left

            if key > nod.key:
                nod=nod.right
        


    def write(self):
        '''Skriver ut trädets element i inorder, kallar på den rekursiva funktionen rekwrite. '''
        rekwrite(self.rot)
        print('\n')



''' Hjälpfunktioner '''





def rekstore(rot, key,value):
    ''' Rekursiv funktion, tar in rot ,key och value och returnerar ny nod som sätts in
    med tillhörande key, value '''

    nod=rot
    if nod == None:
        return Node(key,value)  # om noden är tom skapas en ny nod

    else:
        if value < nod.value:   # om ny nod är mindre än jmförande nod kolla vänster nod
            nod.left= rekstore(nod.left,key,value) # anropar funktionen igen, med den vänstra noden som input

        elif value > nod.value: #om ny nod är mindre än jmförande nod kolla höger nod
            nod.right= rekstore(nod.right,key,value)

        return nod 


    
def reksearch(nod,key):


    ''' Rekursiv funktion som söker efter key i trädet och returnerar tillhörande värde ifall noden finns
    annars KeyError'''

    try:
        if nod == None:
            #print('noden är tom')
            return None

        if nod.key == key:  # om nyckel är densamma som sökt nyckel
            return nod.value

        if key < nod.key:   # om nycken är mindre än sökt nyckel kolla vänster
            nod=nod.left
            return reksearch(nod,key)

        if key > nod.key:   # om nycken är mindre än sökt nyckel kolla höger
            nod=nod.right
            return reksearch(nod,key)

    except KeyError:    
        pass
        


           
def rekwrite(rot):
    '''Rekursiv funktion som skriver ut trädet i inorder '''
    nod=rot
    if nod!= None:
        rekwrite(nod.left)
        print(nod.value)
        rekwrite(nod.right)
   



träd= Bintree()

träd.store(10, 10)
träd.store(5, 5)
träd.store(20, 20)
träd.store(15, 15)
träd.store(25,25)
träd.store(8, 8)

träd.write()














    














