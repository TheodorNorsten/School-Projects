#Theodor Norsten 2019-02-25
#kurskod: DD100N
'''Programmet håller räkningen för poängen i pilkasttävling. Programmet läser in från textfil och möjliggör att användaren kan lägga till nya
resultat och sparar sedan den uppdaterade textfilen. '''
    

def läsa_fil(filnamn):
    '''funktionen läser in namn och poäng från fil och returnerar en matris.
    Inparameter: filnamn poäng.txt
    Returvärde: matris(matris) bestående av 2 listor namn och poäng '''
    matris=[]
    poängfil= open(filnamn,'r')
    spelare=poängfil.readline().strip() 
    while spelare!='':
        poäng= int(poängfil.readline().strip())
        matris.append([spelare,poäng])
        spelare=poängfil.readline().strip()
    poängfil.close()

    return matris
    



def upptaget_namn(upptaget,matris):
    '''Funktionen kollar om det det redan finns ett namn i matrisen returnerar False annars True.
    Inparameter: upptaget, matrismed 2 listor namn resp poäng
    Returvärde: True om namnet är upptaget annars False'''
    
    for i in range(len(matris)):
        if matris[i][0]==upptaget: #  ändra namn till upptagen
            return True

    return False



def heltal(värde):
    '''funktionen kontrollerar om inmatning för poäng är ett heltal.
    Inparameter:värde
    Returvärde: True om det är ett heltal, annars False'''

    try:
        int(värde)
        return True
    except ValueError:
        return False

def accepterat_värde(värde):
    '''funktionen kontrollerar om ett hetal är inom intervallet 0-50.
    Inparameter: tal(int) samt undre och övre gräns för intervallet
    Returnerar: True om talet är inom intervallet, annars False.'''

    if värde >= 0 and värde<= 50:
        return True
    else:
        return False

def lägg_till_poäng():
    '''funktionen kontrollerar om ett tal uppfyller krav för inmatning utifrån funktionen accepterat_värde och heltal.
    inparameter:inget
    Returvärde: nytt_poäng(tal)'''
    nytt_poäng= input('skriv nytt resultat')
    korrekt= False
    while not korrekt:
        if heltal(nytt_poäng)==True:
            if accepterat_värde(int((nytt_poäng)))== True:
                korrekt=True
            else:
                print('fel intervall,försök igen')
                nytt_poäng= input('skriv nytt resultat')
        else:
            print('felaktigt värde på poäng')
            nytt_poäng= input('skriv nytt resultat')
    return int((nytt_poäng))


def lägg_till_namn_poäng(matris):
    '''funktionen lägger till nytt namn och poäng till matrisen.
    Inparameter: matris
    Returvärde:matris'''
    while True:
                spelarnamn= input('vad heter spelaren?')
                if upptaget_namn(spelarnamn,matris):
                    print('namnet upptaget,ange nytt namn') 
                else:
                    resultat= lägg_till_poäng()
                    matris.append([spelarnamn,resultat])
                    break
    return matris
                
    
def sortera_resultat(matris):
    '''Funktionen sorterar matrisen utifrån poängen.
    inparameter: matris
    Returvärde: matris'''
    matris=sorted(matris,key=lambda x:x[1],reverse=True)
    
    return matris
        
def spara(matris,filnamn):
    '''Funktionen skriver ut och sparar namn och poäng.
    inpararmeter: matris och filnamn
    Returvärde: inget'''

    poängfil=open(filnamn,'w')
    for i in matris:
        poängfil.write(i[0] + '\n')
        poängfil.write(str(i[1]) + '\n')
    poängfil.close()
                       
def felhantering(menyval):
    try:
        int(menyval)
        return True
    except ValueError:
        return False

# huvudmeny



def huvudprogram():
    '''Funktionen skriver ut huvudmenyn och frågar användaren för inmatning.
    inparameter: inget
    Returvärde: inget'''
    matris= läsa_fil('testa_poäng.txt')
    while True:
        print('huvudmeny')
        print('1. se resultat')
        print('2. Mata in nytt resultat')
        print('3. spara och avsluta')
        val= input('Välj menyval')
        while not heltal(val):
            print('Det är är ingen siffra,vänligen ange siffra och försök igen')
            val=input('välj menyval')
        val=int(val)
        if val==1:     
           matris=sortera_resultat(matris)
           print('just nu är ställningen följande')
           for i in matris:
               print(i,'poäng')
        elif val==2:
            matris=lägg_till_namn_poäng(matris)
       
        elif val==3:
            spara(matris,'poäng.txt')
            break
        else:
            print('felaktigt menyval,försök igen')
    print('Resultattavlan är sparad.Hejdå!')
      
huvudprogram()

          









