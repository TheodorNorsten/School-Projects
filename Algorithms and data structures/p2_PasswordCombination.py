#Theodor Norsten
#DD1321 p2

#Globala variabler
Alfabet= {'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R',
          's':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}



'''In: en bokstav(str)
    Funktionen kontrollerar om inparametern finns som nyckel i hashtabellen Alfabet.
    Ut: Versalen(värdet) till inparametern om den finns i Hashtabellen annars oförändrad.'''
def Big_small(letter):

    if letter in Alfabet.keys():
        return Alfabet[letter]
    else:
      return letter





'''IN: ord(str)
    Funktionen retunerar en lista av inparametern där varje element i listan innehåller en versal
    UT: tom_lista(lista)'''
def Bigletter(string):
    letter_list=[]

    for i in range(len(string)):
        lisT= list(string)
        lisT[i]= Big_small(lisT[i])
        combine=''.join(lisT)
        letter_list.append(combine)

    return letter_list




'''IN: ord(str)
    Funktionen returnerar en lista med alla kombinationer av versaler(par)för ordet.
    UT: tomL(lista)'''
def twoBigletter(string):
    letter_list= []

    for i in range(len(string)):
        lisT= list(string)
        lisT[i]= Big_small(lisT[i])

        for j in range(len(string)-(i+1)):
            lisT_2= list(string)
            lisT_2[j+(i+1)]= Big_small(lisT_2[j+(i+1)])
            lisT_2[i]=lisT[i]
            joina= ''.join(lisT_2)
            letter_list.append(joina)
    return letter_list





'''IN: sträng(str)
    Funktionen placerar varje element ur en lista framför,bakom och mellan varje bokstav av inparametern
    UT: lista med alla kombinatiner av elementens placering.'''

def sneakin(string):
    numbers= ['2','3','4']
    new_list=[]
    for i in range(len(string)+1):
        lista= list(string)

        for j in range(len(numbers)):
            list2= list(string)
            list2.insert(i,numbers[j])
        
            new_list.append(''.join(list2))

    return new_list



'''IN: sträng
    Funktionen anropar de 3 tidigare funktionerna och returnerar en lista med returvärdet för resp funktion
    UT: lista med returvärdet från tidigare funktioner.'''

def combine(sträng):
    all_functions=[]
    function_1=Bigletter(sträng)
    function_2=twoBigletter(sträng)
    function_3=sneakin(sträng)

    all_functions.append(function_1)
    all_functions.append(function_2)
    all_functions.append(function_3)
    
    final_list=[]
    for i in all_functions:
        for j in i:
            final_list.append(j)
            

    return final_list




print(combine('basket'))
#print(combine('basket')[0])




'''IN:
    Funktionen läser in fil med lösenord
    UT: lista med alla lösenord.'''

def read_file():
    password_fil= open('p2_passwords.txt','r')
    password_lista=[]
    password= password_fil.readline().strip()
    while password!='':
        password_lista.append(password)
        password= password_fil.readline().strip()
        
    password_fil.close()

    return password_lista
#print(read_file())




'''IN:
    Funktionen tar in lista med alla lösenord och returnerar lista med alla kombinationer för reso lösenord.
    UT: lista med alla kombinationer för varje lösenord.'''  
    
def combine_password():
    combination_list=[]
    for i in read_file():
        
        password_comb=combine(i)
        for j in password_comb:
            combination_list.append(j)
    return combination_list

#print(combine_password())




'''IN:
    Funktionen skapar en ny textfil och skriver till lista med alla kombinationer för resp lösenord.
    UT. '''

def save_password():
    with open('password_komb.txt','w') as fil:
        
        for i in combine_password():
                fil.write('%s\n' % i)
            
    
#save_password()









      

        






    









