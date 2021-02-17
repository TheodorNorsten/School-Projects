# D3, problemträd, breddenförstsökning
# Theodor Norsten DD1321

import string
import sys
from Hashtable_D2 import DictHash
from arrayQFile import LinkedQ

alphabet= string.ascii_lowercase + "åäö"


'Nod klass för att lagra varje kombination(barn) av rot-Noden. attribut: word och dess förälder. '
class ParentNode:

    def __init__(self,word,parent=None):
        self.word=word
        self.parent=parent


    
    def __repr__(self):
        return str(self.word)




'''Läser in filen med trestaviga ord returnerar lista med alla ord. '''
def read_file():

    word_file= open("word3.txt","r")
    word_list= []
    
    myDict=DictHash()
    word= word_file.readline()
    while word:
        word=word.strip()
        word_list.append(word)
        word=word_file.readline()
        
    return word_list
    

' Funktionen sparar alla ord som values från fil till en dictionary.'
def myDictionary():

    myDict=DictHash()
    word_list= read_file()

    for i in range(len(word_list)):
        myDict.store(i,word_list[i])
    
    return myDict


'Hashtabell som lagrar redan besökta ord '
myDict_used= DictHash()



'''Funktionen tar in sträng och returnerar en lista med alla barn till strängen.
    IN: string(str)
    UT: unique_child(lista)'''
def makechildren(string):
    
                            
    if string not in myDict_used.values():          #Lägger till input strängen i hashtabell med besökta ord, om strängen inte finns.
        myDict_used.store(myDict_used.len(),string)

    child_list=[]
    unique_child=[]
    temp_vek=[]
   
    myDict= myDictionary()                          #hashtabell med alla trestaviga ord som värden
       
    'Kontrollerar vilka kombinationer av ordet string som finns i myDict och lagrar dessa i child_list. '  
    for i in string:
        for j in alphabet:
            comb_letter=(string.replace(i,j))
            
            for value in myDict.values():
                if value == comb_letter and comb_letter!=string:
                 child_list.append(comb_letter)      

    
    for unique in child_list:                           #Tar bort alla dubletter i child_list lagrar unika värden i unique_child.
        if unique not in unique_child: 
            unique_child.append(unique)


    
    if myDict_used.len()==1:                            #Om hashtabell med besökta värden endast innehåller 1 värde.
        
        for i in range(len(unique_child)):
            myDict_used.store(i+1,unique_child[i])
            
        #print(myDict_used,'\n')
        return unique_child
    
         
    else:
        'kollar om orden unique_child redan har besökts(finns i hashtabell, om ja sparas värdena till listan temp_vek.'
        for i in unique_child:     
            if i in myDict_used.values():
                temp_vek.append(i)
                
        
        for i in temp_vek:                          #tar bort alla element som redan finns
            unique_child.remove(i)

        'Lägger till alla barn i unique_child till hashtabellen med redan besökta barn.'       
        for i in range(len(unique_child)):
           myDict_used.store(myDict_used.len(),unique_child[i]) 
              
              
        #print(myDict_used,'\n')
        return unique_child
                


#print(makechildren("fan"))
#print(makechildren("ban"))



'Funktionen tar som input Nod ur klassen ParentNode och skriver ut vägen mellan rot-ord och slutord om det finns.'
def writechain(endNode):

    if endNode.parent !=None:
        writechain(endNode.parent)
    print(endNode.word)





'Funktionen tar som input startord och slutord och skriver ut vägen mellan dessa om det finns, annars None'

def findPath(startWord,endWord):

    queueOfWords= LinkedQ()                     #skapar en kö
    node= ParentNode(startWord)                 # skapar ett objekt av ParentNode av startordet
    
    queueOfWords.enqueue(node)                  #lägger

    while not queueOfWords.isEmpty():
        
        nextWord= queueOfWords.dequeue()
        

        if nextWord.word== endWord:
            break
        
        child_list= makechildren(nextWord.word) #skickar in ordet till makechildren
        for i in child_list:
            node_children= ParentNode(i,nextWord) # skapar objekt ur klassen ParentNode av varje barn som returneras från makechildren.
            queueOfWords.enqueue(node_children)
        
        continue

    if queueOfWords.isEmpty():
        print("ingen väg fanns")
        return None

    else:
        print("det fanns en väg")
        print("vägen mellan", startWord, " och", endWord, "är:\n")
        writechain(nextWord)
        


#findPath("fan","gud")







'test funktion att funktionen makechildren returnerar rätt antal kombinationer. '
def ControlNumb(string):
    
    length_combLetter= len(makechildren(string))
    

    if length_combLetter==len(string)*len(alphabet):
        print("same number of combinations")
        print("length string:", len(string))
        print("length aplhabet:", len(alphabet))
        print("length comb:" , length_combLetter)

    else:
        print("wrong number of combinations")

#ControlNumb("hej")






def main():
    

    if len(sys.argv)==3:
        findPath(sys.argv[1],sys.argv[2])    
    
    else:
        print("felaktig input, input ska vara start och slutnod")
        sys.exit()


main()






