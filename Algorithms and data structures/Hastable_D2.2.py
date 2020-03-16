# Egen implementation av hashtabell


'''Klass HashNode som skapar en ny nod med attributen key,value och next.
    IN: key,value.'''
class HashNode:

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None



''' Klassen för hashtabllen attributen size och table. Initieras med en tom lista av N-size
    Size är satt till 2gg antalet nycklar.'''
class Hashtable:

    def __init__(self):
        self.size=2000000
        #self.items=0
        self.__table=[None]*self.size
        

    '''Metod för insättning i hashtabellen, räknar fram hashvärde för input-key och kollar om tabellen är tom för det hashvärdet
    om ja, skapas en ny nod(nyckel,värde) om inte traveserar vi i den länkade listan tills det finns tom plats.
    IN: nyckel,värde'''
    def store(self,key,value):

        #self.items+=1
        index= self.hash(key)

        if self.__table[index]is None:
            self.__table[index]=HashNode(key,value)
            return 

        else:
            node=self.__table[index]
            next_node= node.next
            while next_node is not None:
                node=next_node
                next_node=next_node.next          

            node.next= HashNode(key,value)
            return 
                
                    
    '''Metod för sökning i hashtabllen, räknar fram ett hashvärde för input-key, traveserar fram i den länkade listan till noden
        returnerar motsvarande value till noden, om noden inte finns returneras inte.
        IN: nyckel
        UT: value om den finns annars inget.'''           

    def search(self,key):

        index= self.hash(key)
        node= self.__table[index]    
        
        while node is not None and node.key!=key:
            node=node.next           
        
        
        if node is None:
            print('nyckeln finns inte')
            return
            
        else:
            return node.value

        '''
        try:
            
            return node.value
        except KeyError:
            print('nyckeln finns inte i hashtabellen')'''
      



    '''Hashfuktion tar input en sträng och reurnerar ett hashvärde för strängen. Beräknas genom Ord(sträng)*index(sträng)
    IN: nyckel
    UT: total(hashvärdet för strängen)'''

    def hash(self,key):
        total=0
        for index,i in enumerate(key):
            total+=index*ord(i)

        total=total%self.size
        
        return total 



    def __repr__(self):
        return str(self.__table)



'''läser in filen och lagrar datan i hashtabellen med artiser som nyckel och låt som värde.
    UT: 2 listor med artister resp låtar'''
def readfile():
    track_file=open('test.txt','r',encoding='utf-8')
    tracks= track_file.readlines()
    artist=[]
    song=[]

    for i in tracks:
        i=i.strip()
        splitting_line= i.split('<SEP>')
        artist.append(splitting_line[-2])
        song.append(splitting_line[-1])

    track_file.close()

    return artist,song


               

''' Definerar min hashtabell och lagrar artist och låtar i hashtabellen
    UT: myDict(hastabell) med artister som nyckel och låtar som key.'''
def Dictionary():

    myDict=Hashtable()
    artist,track=readfile()
    for i in range(len(artist)):
        myDict.store(artist[i],track[i])

    return myDict


'''Huvudfunktion som progammet körs ifrån. '''
def main():
    myDict=Dictionary()
    print(myDict.search('theo'))
    
    

main()







    
            
