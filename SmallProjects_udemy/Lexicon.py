import json
import difflib
#help(difflib.SequenceMatcher)

with open('data.json') as file:
    data=json.load(file)

#print(data['rain'])

def nyckel(nyckel):
    return data[nyckel]


def skriva_ut():
    while True:
        word= input('skriv ett ord')
        word=word.lower()
        for i in data.keys():
            if i==word:
                return i
            elif i== word.title():
                return i
            elif i == word.upper():
                return i
            
        else:
            reko_ord= difflib.get_close_matches(word,data.keys())
           
            if len(difflib.get_close_matches(word,data.keys()))>0:
                rätt_reko= input('menade du ordet: ' + reko_ord[0] + ' ja eler nej')
                if rätt_reko=='ja':
                    return reko_ord[0]
                else:
                    continue
               
            else:
                print('ordet finns inte försök igen')
            



def huvudprogram():
    ord_lista=skriva_ut()
    
    if type(nyckel(ord_lista))==list:
        for i in nyckel(ord_lista):
            print(i)
    else:
        print(nyckel(ord_lista))

huvudprogram()

