#Theodor Norsten 2019-02-28
#Kurskod: DD100N
'''Programmet läser in information från textfil som läggs till som objekt i skapad klass.Programmet presenterar en användarmeny där användaren
Kan skriva ut objekten,ändra attributen och spara filen.'''
class Husdjur:
    '''representerar klassen Hund, har attributen, namn,hunger,klappbehov.'''
    def __init__(self,djur,namn,hunger,klappbehov):
        '''Konstruktionen som anropas när vi skapar ett Husdjur
        Parametrar djur(str) namn(str) hunger(str) klappbehov(str)'''

        self.namn= namn # sträng
        self.hunger= hunger # int
        self.klappbehov= klappbehov # int
        self.djur= djur # sträng

    
    def __repr__(self):
        '''Metod som returnerar en sträng som beskriver objektet.
        Inparameter:self
        Returvärde: sträng'''
        return self.djur + self.namn +' '+ str(self.hunger) + ' ' + str(self.klappbehov)

    def skrivut(self):
        '''Metoden returnerar en sträng
        inparameter:self
        Returvärde:inget'''
        print(self.djur + self.namn + ' Hunger: ' + str(self.hunger) + ' Klappbehov: ' + str(self.klappbehov))

    def __lt__(self,other):
        '''metoden jämför namnet mellan objekten och sorterar efter bokstavsordning.
        Inparameter:self,other
        Returvärde:True annars False'''

        if self.namn < other.namn:
            return True
        else:
            return False
        

    def klappa(self):
        '''Metoden minskar attributet klappbehov med 1.
        Inparameter:self.
        returvärde:inget.'''
        self.klappbehov= self.klappbehov-1
        

    def mata(self):
        '''Metoden minskar attributet hunger med 1.
        inparameter:self.
        Returvärde:inget.'''
        self.hunger= self.hunger-1
    
  
def läsa_fil():
    '''läser information från filen Husdjur.txt som läggs till i listan Husdjuren
     parametrar:inget.
     Returvärde:husdjurslista.'''
    husdjurslista=[]
    djurfil= open('djur.txt','r')
    djur= djurfil.readline().strip()
    while djur:
        namn= djurfil.readline().strip()
        hunger=int(djurfil.readline().strip())
        klappbehov=int(djurfil.readline().strip())
        ny_lista= Husdjur(djur,namn,hunger,klappbehov)
        husdjurslista.append(ny_lista)
        djur= djurfil.readline().strip()
    
    djurfil.close()
    return husdjurslista 
                      
    

def spara_fil(husdjurslista):
    '''skriver ut och lagrar alla husdjur i filen Husdjur.txt.
    Inparameter: husdjurslista,filnman.
    Returvärde: inget.'''
    djurfil= open('djur.txt','w')
    husdjurslista.sort()
    for i in husdjurslista:
        djurfil.write(i.djur + '\n')
        djurfil.write(i.namn + '\n')
        djurfil.write(str(i.hunger) + '\n')
        djurfil.write(str(i.klappbehov)+ '\n')
    djurfil.close()


def menyval():
    '''funktionen skriver ut menyvalen och returnerar användarens input.
    Inparameter: inget
    Returvärde: val(str)'''

    print('Vad kan jag stå till tjänst med?')
    print('1: Lista Husdjur och deras status')
    print('2: Leta upp djur')
    print('3: Avsluta')
    val=(input('välj alternativ'))
    return val




def inmatning(husdjurslista):
    '''Funktionen kontrollerar om nytt_värde finns i husdjurslista.
    Inparameter:husdjurslista
    Returvärde:i(objekt)'''
    nytt_värde=input('Vilket djur vill du att jag letar upp?')
    
    while True:
        for i in husdjurslista:
            if i.namn==nytt_värde:
                print('hittade ',nytt_värde,' under soffan ',end='')
                return i
        else:
            print('Namnet finns inte,försök igen')
            nytt_värde=input('Vilket djur vill du att jag letar upp?')
    
          

def felhantering(värde):
    '''funktionen kontrollerar att värde är heltal.
    Inparameter:värde.
    Returvärde: True om heltal annars False.'''
    try:
        int(värde)
        return True
    except ValueError:
        return False


def meny_val_2(djur):
    '''Funktionen printar ut menyn för val 2 i huvudprogrammet.
    Inparameter: djur(objekt)
    Returvärde:inget'''
    print('vad ska jag göra nu?')
    print('1:klappa',djur.namn)
    print('2:Mata',djur.namn)
    print('3:tillbaka till huvudmenyn')

def huvudprogram():
    '''Funktionen presenterar en meny och låter användaren göra inmatning
    Inparameter:inget
    Returvärde:inget'''
    print('välkommen till PetRobo!')
    djurlista=läsa_fil()
    while True:
        val= menyval()
        while not felhantering(val):
            print('Det där är ingen siffra,Försök igen')
            val=menyval()
        val=int(val)
        if val==1:
            djurlista.sort()
            for i in djurlista:
                i.skrivut()
        elif val==2:
            att_göra=1
            djur=inmatning(djurlista)
            while att_göra!=3:
                meny_val_2(djur)
                att_göra=int(input())
                if att_göra==1:
                    djur.klappa()
                elif att_göra==2:
                    djur.mata()
            else:
                continue
        elif val==3:
            spara_fil(djurlista)
            break
        else:
            print('felaktigt menyval,försök igen')
    print('Programmet avslutas.Tack för att du använder PetRobo')

huvudprogram()






            
