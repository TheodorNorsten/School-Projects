#Theodor Norsten 2019-03-25
#Kurskod:DD100N
#P-uppgift 144 Tennismatch


'''Programmet presenterar spelarstatistik från olika tennisspelare och läser in och skriver till textfil.Programmet låter användaren simulera
 valfria matcher mellan 2 spelare och ange vinnaren för respektive match.Programmet uppdaterar spelarstatistiken , sparar och avslutar programmet efter användaren.'''



class Tennis:
    '''En klass(Tennis) som tilldelas attributen namn,serve,vinst,matcher,andel. '''
    def __init__(self,spelare,serve,vinst,matcher):
        '''konstruktor som skapar ett nytt objekt(tennisspelare).
        Inparametrar: namn(sträng), serve(float) vinst(str), matcher(str),andel(float).'''
        self.spelare= spelare 
        self.serve= float(serve) 
        self.vinst=int(vinst)
        self.matcher=int(matcher)
        self.andel=self.vinst/self.matcher  


    def __lt__(self,other):
        '''metoden jämför attributet andel mellan objekten och sorterar efter största värde.
        inparameter:self,other.
        Returvärde: False annars True.'''
        if self.andel < other.andel:
            return False
        else:
            return True


    def förlorade(self):
        '''metoden uppdaterar attributet matcher med 1 samt attributet andel.
        Inparameter: self
        Returvärde:inget'''
        self.matcher= self.matcher + 1
        self.andel= self.vinst/self.matcher

    def vann(self):
        '''metoden uppdaterar attributen vinst och matcher med 1 samt attributet andel.
        Inparameter:self
        Returvärde:inget'''
        
        self.vinst= self.vinst + 1
        self.matcher= self.matcher+1
        self.andel = self.vinst / self.matcher
           
        


    def skrivut(self):

        '''Metoden returnerar en sträng utifrån hur resultaten ska presenteras.
        inparameter:self.
        Returvärde:sträng.'''

        return( self.spelare  + '|' + str(self.serve)+ ' '*(18-len(str(self.serve))) + '|' + str(self.vinst) + ' '*(18-len(str(self.vinst))) + '|' + str(self.matcher) + ' '*(19-len(str(self.matcher))) + '|' + str(round(self.andel,3)) + ' '*(14-len(str(round(self.andel,3)))) + ' \n')




def skrivlista(spelarlista): # tydligare utskrift
    '''Funktionen skriver ut en lista med alla spelare(spelarlista)
    Inparameter: spelarlista
    Returvärde:  spelarlista'''
    print('placering |','spelare |','serveprocent |','vinster |','matcher |','vinstprocent |')
    
    for i in range(len(spelarlista)): 
         print(i+1,' '*(9-len(str(i+1))),spelarlista[i].skrivut())

    return spelarlista
            
    







def läsa_fil(): # Ha filnamn som inparameter, köra en try , except för att filen existerar.
    '''Funktionen läser information från filen Tennisspelare.txt
    Inparameter: inget.
    Returvärde: spelarlista.'''
    try:
        spelarfil= open('Tennisspelare.txt','r')
    except IOError as e:
        print(e)
    
    spelarlista=[]
    spelare=spelarfil.readline().strip()
    while spelare:
        serve= float(spelarfil.readline().strip())
        vinst=int(spelarfil.readline().strip())
        matcher= int(spelarfil.readline().strip())
      
        lista_klass= Tennis(spelare,serve,vinst,matcher)
        spelarlista.append(lista_klass)
        spelare=spelarfil.readline().strip()
    
    spelarfil.close()
    return spelarlista
    



def spara_fil(spelarlista):
    '''Funktionen skriver ut och lagrar alla Tennisspelare i filen Tennisspelare.txt
    Inparameter: spelarlista.
    Returvärde: inget.'''

    spelarfil=open('Tennisspelare.txt','w')
    spelarlista.sort()
    for i in spelarlista:
        spelarfil.write(i.spelare + '\n')
        spelarfil.write(str(i.serve) + '\n')
        spelarfil.write(str(i.vinst) + '\n')
        spelarfil.write(str(i.matcher) + '\n')
    spelarfil.close()
    




def meny():
    '''funktionen presenterar en meny för användaren för inmatning.
    Inparameter:inget
    Returvärde:val(str)'''
    
    print('Berätta vad du vill göra? ')
    print(' 1: Ange resultat för spelad match? ')
    print(' 2: spara och avsluta ')
    val= input(' Välj ett alternativ ')

    return val
    



def leta_lista(spelare,spelarlista):
    '''Funktionen kontrollerar att spelare(inmatning) finns i spelarlista,returnerar objektet annars inget.
    Inparameter: spelare(inmatning),spelarlista
    Returvärde: i(objekt) annars inget(None)'''
    for i in spelarlista:
        if i.spelare==spelare:
            return i
    print(spelare + ' finns inte i listan,försök igen')
    return None




def välj_match(spelarlista):
    '''Funktionen låter användaren ange resultat från en match och uppdaterar attributen för resp objekt(spelare_1.spelare och spelare_2.spelare)
    Inparameter: spelarlista.
    Returvärde: inget.'''

    while True:

        print('välj 2 spelare ur listan som möter varandra i en match ')
        spelare_1_in= input('Ange namn på spelare 1 ')
        spelare_2_in= input('Ange namn på spelare 2 ')


        spelare_1 = leta_lista(spelare_1_in,spelarlista)
        spelare_2 = leta_lista(spelare_2_in,spelarlista)

        
        if spelare_1 and spelare_2:
            
            vinnare= input('Ange spelarnamn på vinnaren ')
            
                                                                              
            if vinnare==spelare_1.spelare:     
                spelare_1.vann()
                spelare_2.förlorade()
            else:
                spelare_2.vann()
                spelare_1.förlorade()

            return
            

            

                    
    

def felhantering(tal):
    '''Funktionen kontrollerar att inmatning är ett accepterat värde(heltal)
    Inparameter: tal(inmatning från användare)
    Returvärde: True om heltal annars False'''

    try:
        int(tal)
        return True
    except ValueError:
        return False





def huvudprogram():
    '''Funktionen presenterar meny med val och låter användaren göra inmatning.
    Inparameter:inget
    Returvärde:inget''' 

    print('Hej och välkommen till Resultatsidan ')
    spelarlista= läsa_fil()
    while True:
        print('Resultatställningen är följande: ')
        print('Nedan presenteras Statistik över alla spelare ')
        
        spelarlista.sort()
        skrivlista(spelarlista)

        val= meny()
        while not felhantering(val):
            print('Felaktig inmatning,försök igen')
            val= meny()
        val=int(val)
        
        if val==1:
            välj_match(spelarlista)

            
        elif val==2:
            spara_fil(spelarlista)
            break
        else:
            print('Felaktigt menyval,vänligen försök igen')
    print('programmet sparas och avslutas,välkommen åter')

huvudprogram()
    
    





