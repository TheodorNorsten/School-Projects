from array import array

class ArrayQ():
    
    def __init__(self,):
        self.item= array('i',[])


    def enqueue(self,new_value):

        return self.item.insert(0,new_value)


    def dequeue(self):
        try:
             return self.item.pop()
        except:
            return 'Tom lista'


    def isEmpty(self):

        return self.item ==array('i',[])

    def __repr__(self):
        return str(self.item)


            

def Magic_tric(kort_lista):

    #indata_kort= input('vilka kort från 1(Ess) till 13(kung) ska vi trolla med?')
    #kort_lista= indata_kort.split()    
    lista_kort=[]
    cards= ArrayQ()
    #print('indata lista', kort_lista)
    kort_lista.reverse()
    for i in kort_lista:
        #i=int(i)
        cards.enqueue(i)
    print('klassen kort', cards)    
    while not cards.isEmpty():
        cards.enqueue(cards.dequeue())
        visa_kort= cards.dequeue()
        lista_kort.append(visa_kort)

    lista_kort.sort()
    print(cards)
    print(lista_kort)


    
        


Magic_tric([4,1,6,3,2,10,11,5,7,9,8,12,13])


































        
        
    
