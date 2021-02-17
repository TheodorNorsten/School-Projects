#D2
#1. Hashning med pythons inbyggda dictionary


'''Definerar klassen DictHash som initieras med en tom dictionary.
'''
class DictHash:

    def __init__(self):
        self.__myhash={}
    
    '''Metod som lagrar värden och nycklar i min hashtabell
    IN: nyckel, värden'''
    def store(self,key,value):
        self.__myhash[key]=value        

    '''Metod som tar en nyckel som input och returnerar tillhörande value
    IN: nyckel
    UT value'''
    def search(self,key):
        
        for i in self.__myhash.keys():
            if i.lower()==key.lower():
                return i
        else:
            print('key dosent exist in dictionary')


    def __getitem__(self,key):
        return self.__myhash[key]


    def __contains__(self,key):
        for i in self.__myhash.keys():
            if i==key:
                return True
        else:
            return False


    def __repr__(self):
        return str(self.__myhash)
    



'''läser in filen och lagrar datan i hashtabellen med artiser som nyckel och låt som värde.
    UT: 2 listor med artister resp låtar'''
def readfile():
    track_file=open('tracks.txt','r',encoding='utf-8')
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
def dictionary():

    myDict=DictHash()
    artist,track=readfile()
    for i in range(len(artist)):
        myDict.store(artist[i],track[i])
    return myDict


    
'''Huvudfunktion som progammet körs ifrån. '''
def main():
    myDict=dictionary()
    print(myDict['Karkkiautomaatti'])
    
              

main()

    







































 
    













    
