#from arrayQFile import ArrayQ
from arrayQFile import LinkedQ







def Magic_tric(kort_lista):
    
    #indata_kort= input('skriv vilka kort(1-13) vi ska trolla med, använd mellanslag mellan varje siffra?')
    #kort_lista= indata_kort.split()    
    lista_kort=[]
    #cards= ArrayQ()
    cards= LinkedQ()
    for i in kort_lista:
        #i=int(i)
        cards.enqueue(i)
    '''Här börjar trolleritricket '''
    while not cards.isEmpty():
        cards.enqueue(cards.dequeue())       
        visa_kort= cards.dequeue()
        lista_kort.append(visa_kort)
   
    
    print('korten kommer ut i följande ordning:', lista_kort)

#Magic_tric()

Magic_tric([7,1,12,2,8,3,11,4,9,5,13,6,10])



if __name__=='__main__':  
   # ArrayQ()
   LinkedQ()






























  
