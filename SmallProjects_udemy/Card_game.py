# milestone project 2
import random
''' step 1'''

suit=['heart','spade','diamonds','clubs']
rank= ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values=[1,2,3,4,5,6,7,8,9,10,10,10,11]
hashtabell= {}
for i in range(len(rank)):
    hashtabell[rank[i]]=values[i]
    
spela= True


''' step 2 creating card class, deck class, hand class. '''

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __repr__(self):
        return str(self.rank) + ' av ' + self.suit


class Deck:
    def __init__(self):
        self.deck=[]
        for färg in suit:
            for värde in rank:
                self.deck.append(Card(färg,värde))

    def __repr__(self):
        sträng=''
        for kort in self.deck:
          sträng+= '\n' +  kort.__repr__()
        return 'kortleken har ' + sträng

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return random.choice(self.deck)
    



class Hand:
    def __init__(self):
        
        self.kort= []
        self.value=0
        self.aces=0

    def addera_kort(self,other):
        self.kort.append(other)
        self.value+= hashtabell[other.rank]
        if other.rank=='Ace':
            self.aces+=1
        
    def hantera_ess(self):
        if self.value>21 and self.aces:
            self.value-=10
            self.aces-=1
        




class Chips:
    def __init__(self):
        self.total=100
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet
        



def take_bet(chips):
    while True:
        try:
            chips.bet= int(input('hur mycket vill du beta'))
        except:
            print('ej en siffra')
            continue
        else:
            if chips.bet> chips.total:
                print('du har inte tillräckligt med pengar, försök igen')
            else:
                break
        
                
def hit(deck,hand):
    
    hand.addera_kort(deck.deal())
    hand.hantera_ess()
    


def hit_or_stand(deck,hand):
    global spela
    
    hit_stand= input('vill du spela eller stanna, ja för spela nej för stanna')
    
    if hit_stand=='ja':
        hit(deck,hand)
            
    elif hit_stand=='nej':
        print('spelare passar, dealer spelar')
        spela=False
            
    else:
        print('svara ja eller nej')
            
    


def show_some(player,dealer):
    print('spelarens hand och aktuell poäng')
    print(player.kort)
    print(player.value)
    print('dealens hand')
    print(dealer.kort[1])

def show_all(player,dealer):
    print('spelarens hand och aktuell poäng')
    print(player.kort)
    print(player.value)
    print('dealens hand och aktuell poäng')
    print(dealer.kort)
    print(dealer.value)


def player_busts(player,dealer,chips):
    print('player busts')
    chips.lose_bet()
    
        
def player_wins(player,dealer,chips):
    print('player won')
    chips.win_bet
    
def dealer_busts(player,dealer,chips):
    print('dealer busts')
    chips.win_bet

def dealer_wins(player,dealer,chips):
    print('dealer won')
    chips.lose_bet

def push(player,dealer,chips):
    print('its a tie')
    


def huvudprogram():
    global spela
    print('välkommen till blackjack, din spelmissbrukare')
    while True:
        deck= Deck()
        deck.shuffle()
        player= Hand()
        dealer= Hand()
        player.addera_kort(deck.deal())
        player.addera_kort(deck.deal())
        dealer.addera_kort(deck.deal())
        dealer.addera_kort(deck.deal())

        player_chips= Chips()
        take_bet(player_chips)
        show_some(player,dealer)
        
        while spela:
            hit_or_stand(deck,player)
            show_some(player,dealer)
            if player.value>21:
                player_busts(player,dealer,player_chips)
                break

        if player.value<=21:

            while dealer.value<17:
                hit(deck,dealer)
                show_all(player,dealer)
                

            if dealer.value>21:
                dealer_busts(player,dealer,player_chips)
                    
            elif dealer.value> player.value:
                player_busts(player,dealer,player_chips)
                    
            elif dealer.value < player.value:
                player_wins(player,dealer,player_chips)
                    
            else:
                push(player,dealer,player_chips)
                    
        print(player_chips.total)
        spela_igen=('vill du spela igen: Enter ja ')
        if spela_igen=='ja':
            spela=True
            continue
        else:
            break
        

huvudprogram()        
                
            
            

        






















'''testa_kortlek= Deck()
testa_kortlek.shuffle()
testa_hand= Hand()
testa_hand.addera_kort(testa_kortlek.deal())
testa_hand.addera_kort(testa_kortlek.deal())
print(testa_hand.value)

print(testa_hand.kort[0])'''




    
