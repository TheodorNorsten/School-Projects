# Theodor Norsten
# Datum: 2019-02-09
# Kurskod: DD100N

'''Programmet simulerar spelet tre i rad.Programmet ritar först upp spelplanen för spelet. Programmet körs sedan i huvudfunktionen mha tidigare definierade funktioner
 Varje funktion har en kommentar som beskriver vad funktionen gör samt definerar in-och-returparametrar. '''

#För att rita ut spelplanen används Box Drawing Characters": https://en.wikipedia.org/wiki/Box-drawing_character
import random
def skrivUtSpelplan(spelplan):
    '''funktionen ritar ut spelplanen.
        Inparameter: variablen spelplan
        Returvärde: 3x3 matris'''
    print('      A     B      C  ')
    print('  ┏━━━┳━━━┳━━━┓')
    radRäknare = 0
    for rad in spelplan:
        radRäknare += 1
        print(str(radRäknare) +' ┃', end=' ')
        for ruta in rad:
            print(' ' + ruta, end='  ')
            print('┃', end=' ')
        print()
        if radRäknare < 3:          #Efter sista raden vill vi inte göra detta
            print('  ┣━━━╋━━━╋━━━┫')
    print('  ┗━━━┻━━━┻━━━┛')          #Utan istället detta


def kontrolleraRader(spelplan):
    """Kontrollerar om det finns tre likadana tecken på någon rad och returnerar då True, annars False
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare annars False (booleskt värde)
    """
    for i in range(3):
        if ' ' not in [spelplan[i][0], spelplan[i][1], spelplan[i][2]]:
            if spelplan[i][0] == spelplan[i][1] == spelplan[i][2]:
                return True
           
    return False
                                                                           

def kontrolleraKolumner(spelplan):
    '''Kontrollerar om det finns 3 likadana tecken i någon kolumn och returnerar True annars False.
    Inparameter: spelplan (matris)
    Returvärde: True om det finns en vinnare (kolumnvis) annars False'''
    for i in range(3):
        if ' ' not in [spelplan[0][i], spelplan[1][i], spelplan[2][i]]:
            if spelplan[0][i] == spelplan[1][i] == spelplan[2][i]:
                return True
            
            
    return False


def kontrolleraDiagonaler(spelplan):
    '''kontrollerar om det finns 3 likadana tecken i någon diagonal riktning och returnerar True annars False.
    Inparameter: spelplan(matris)
    Returvärde: True om det finns en vinnare(diagonalt) annars False'''
    #första diagonalen, uppe till vänster till nere till höger
    if ' ' not in [spelplan[0][0], spelplan[1][1], spelplan[2][2]] and spelplan[0][0] == spelplan[1][1] == spelplan[2][2]:
        return True
    elif ' ' not in [spelplan[2][0], spelplan[1][1], spelplan[0][2]] and spelplan[2][0]== spelplan[1][1]== spelplan[2][0]:
        return True
    else:
        return False


def finnsVinnare(spelplan):
    '''kontrollerar om det finns 3 likadana tecken diagonalt eller kolumnvis returnerar True annars False
    Inparameter: spelplan(matris)
    Returvärde: True om det finns någon vinnare(kolumnvis eller diagonalt) annars False.'''
    if kontrolleraKolumner(spelplan) or kontrolleraDiagonaler(spelplan) or kontrolleraRader(spelplan):
        return True
    else:
        return False

def oavgjort(spelplan):
    '''kontrollerar om det finns element i alla positioner(rad,kolumn) i matrisen spelplan, Returnerar True annars False
    Inparameter: spelplan(Matris)
    Returvärde: True om det finns ett element i alla positioner(rad,kolumn)annars False. '''
    for rad in spelplan:
        for element in rad:
            if element ==' ':
                return False
    return True

def tolkaInmatning(inmatning):
    '''Tilldelar inparameter (inmatning)ett värde för postion av rad och kolumn.  ''
    Inparameter: inmatning(bokstav och siffra)
    Returvärde: rad och kolumn för inmatningen.  '''
    while True:
        bokstav = inmatning[0].upper() #Använder .upper() för att göra om alla inmatade bokstäver till versaler
        rad = int(inmatning[1])-1
        if bokstav == 'A':
            kolumn = 0
        elif bokstav == 'B':
            kolumn = 1
        elif bokstav == 'C':
            kolumn = 2
        else:
            break
        return rad, kolumn



def slumpa():
    '''funktionen returnerar slumpmässigt talen 0 eller1
    Inparameter: existerar ej
    Returvärde: 0 eller 1'''
    return(random.randint(0,1))
    




def spela(spelarNamn1, spelarNamn2):
    '''Funktionen gör att användarna(inparametrarna) kan spela spelet. Returnerar vinnaren annars oavgjort.
    Inparameter: spelarnamn1,spelarNamn2
    Returvärde: resultatet från spelet dvs antingen vinnarens namn eller oavgjort.'''
    print("Då kör vi!")
    print("Ange de koordinater du vill lägga på på formatet A1, B3 osv.")
    spelplan = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    spelarLista = [spelarNamn1, spelarNamn2]
    vemsTur=slumpa()
    while finnsVinnare(spelplan) == False:
        vemsTur = (vemsTur+1)% 2 #vemsTur ska aldrig bli 2, utan börja om igen på 0, %-är modul dvs resten vid heltals division.
        skrivUtSpelplan(spelplan)
        if vemsTur == 0:
            markör = 'X'
        else:
            markör = 'O'
        while True:
            inmatning = input(str(spelarLista[vemsTur]) + "s tur att spela: ")
            rad,kolumn = tolkaInmatning(inmatning)
            if ' ' in spelplan[rad][kolumn]:
                break
            else:
                print('rutan upptagen!försök igen')
        spelplan[rad][kolumn] = markör
        if oavgjort(spelplan) == True:
            skrivUtSpelplan(spelplan)
            print("Det blev oavgjort!")
            break
        
    if not oavgjort(spelplan):
        skrivUtSpelplan(spelplan)
        print("Grattis " + str(spelarLista[vemsTur]) + " du vann!")


def huvudfunktion():
    '''Härifrån körs programmet
    Inparameter: existerar ej
    Returvärde: Resultatet från spelet'''
    print("Hej och väkommen till Tre-i-rad!")
    spelarNamn1 = input("Vad heter spelare 1? ")
    spelarNamn2 = input("Vad heter spelare 2? ")
    spela(spelarNamn1, spelarNamn2)

huvudfunktion()
