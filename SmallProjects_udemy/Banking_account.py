
class Account:
    '''Bas klassen attribut, ta ut å sätt in pengar '''
    def __init__(self,nr, saldo):
        self.nr=nr
        self.saldo= saldo


    def deposit(self,pengar):
        self.saldo+= pengar



    def withdraw(self,pengar):
        if self.saldo>=pengar:
            self.saldo-= pengar
        else:
            print('du har inte tillräckligt med pengar på kontot')



    def __repr__(self):
        return 'du har ' + str(self.saldo) + ' pengar kvar på kontot'



class CheckingAccount(Account):
    '''inparameter: account klassen. Attribut saldo, '''
    def __init__(self,nr, saldo):
        super().__init__(nr, saldo)

    def __repr__(self):
        return 'kontonummer:'+ str(self.nr) + ' har ' + str(self.saldo) + ' pengar kvar på kontot'

class SavingsAccount(Account):
    ''' inparameter: account klassen. Attribut saldo '''
    def __init__(self,nr, saldo):
        super().__init__(nr, saldo)
    def __repr__(self):
        return 'kontonummer:'+ str(self.nr) + ' har ' + str(self.saldo) + ' pengar kvar på kontot'

class BuisnessAccount(Account):
    def __init__(self,nr, saldo):
        super().__init__(nr, saldo)

    def __repr__(self):
        return 'kontonummer:'+ str(self.nr) + 'har ' + str(self.saldo) + ' pengar kvar på kontot'




class Costumer:
    def __init__(self,namn,pinkod):
        self.namn=namn
        self.pinkod=pinkod
        self.konton= {'C':[],'S':[],'B':[]}

    def open_checking(self,nr,saldo):
        self.konton['C'].append(CheckingAccount(nr,saldo))

    def open_saving(self,nr,saldo):
        self.konton['S'].append(SavingsAccount(nr,saldo))

    def open_buisness(self,nr,saldo):
        self.konton['B'].append(BuisnessAccount(nr,saldo))


    def __repr__(self):
        return self.namn

    def total_balans(self):
        total=0
        for i in self.konton['C']:
            print(i)
            total+= i.saldo

        for i in self.konton['S']:
            print(i)
            total+= i.saldo

        for i in self.konton['B']:
            print(i)
            total+= i.saldo
        print('total balans',total)



def göra_uttag(kund,nr,konto_typ,belopp):

    for i in kund.konton[konto_typ]:
        if nr== i.nr:
            i.withdraw(belopp)

def göra_insättning(kund,nr,konto_typ,belopp):
    
    for i in kund.konton[konto_typ]:
        if nr== i.nr:
            i.deposit(belopp)



theodor= Costumer('theodor',1212)
theodor.open_checking(111,200)
theodor.total_balans()
göra_uttag(theodor,111,'C',100)
theodor.total_balans()
göra_insättning(theodor,111,'C',100)
theodor.total_balans()






def felhantering(val):
    
    try:
        int(val)
        return True
    except:
        
        return False    
            
        
def meny():
    print('1:sätta in pengar')
    print('2:ta ut pengar')
    print('3:kolla saldo')
    print('4: avsluta')

def meny_2():
    print('vilket konto vill du sätta in pengar på')
    print('1:checking account')
    print('2: savings account')
    print('3: Buisness account')

'''def huvudprogram():
    print('välkommen till automaten')
    namn= input('skriv förnman')
    kod= input('skriv kod')
    while not felhantering(kod):
        print('måste vara en siffra försök igen')
        felhantering(kod)
    kod= int(kod)
    kund= Account(

    print('vad vill du göra?')
    


    if val==1:
        felhantering()
        if val==1:
            
        


    elif val==2:



    elif val==3:



    elif val==4:'''

    









