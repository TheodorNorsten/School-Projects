# D4 Sökning och Sortering

#Del 1 - olika algoritmer löser samma problem
import timeit
import random



class Track():
    ''' Klass som representerar en låt med attributen, id, track_time, artist_name song_title '''
    def __init__(self, track_id, track_time, artist_name,song_title):

        self.track_id = track_id
        self.track_time = track_time
        self.artist_name = artist_name
        self.song_title = song_title


    def __lt__(self,other):
        '''metod som jämför om attributet atrist_name är mindre mellan 2 objekt. '''
        if self.artist_name < other.artist_name:
            return True

        else:
            return False


    def __repr__(self):
        return (self.track_id + ' ' + self.track_time + ' ' + self.artist_name + ' ' + self.song_title)
        
        



'''läser in filen och lagrar varje låts attribut till Track-objekt och lägger in alla objekt i lista.
    UT: lista där varje element i listan är ett objekt.'''
def readfile():
    track_file=open('unique_tracks.txt','r',encoding='utf-8')
    tracks= track_file.readlines()
    TrackList_object=[]

    for i in tracks:
        i=i.strip()
        splitting_line= i.split('<SEP>')
        track_id = splitting_line[0]
        track_time = splitting_line[1]
        artist_name = splitting_line[2]
        song_title = splitting_line[3]

        TrackList_object.append(Track(track_id ,track_time ,artist_name , song_title))

    track_file.close()

    return TrackList_object




''' Definerar min hashtabell och lagrar varje objekt i en dictionary med artist_name som nyckel.
    UT: myDict(hastabell) med artist_name som nyckel och objekt som value.'''
def dictionary():

    myDict={}
    TrackList_object=readfile()
    for Object in TrackList_object:
        myDict[Object.artist_name]=[Object]
    return myDict

#Tidtagning dictionary
def search_dictionary(myDict,artist):
    return myDict[artist]


#myDict= dictionary()
#random_track= random.choice(readfile())
#random_artist= random_track.artist_name 
#time_dic=timeit.timeit(stmt= lambda: search_dictionary(myDict,random_artist) ,number=100)
#print('tiden att hitta element i dictionary är ', round(time_dic,9),' sekunder')




''' Tidtagning: nedanstående del är funktioner som besvarar delfrågorna under Delen Tidtagning"'''










#1: linjärsökning O(n) i värsta fallet



def sorted_list(TrackList_object):
    '''linjärsökning i sorterad lista som hittar det näst sista elementet.
    returnerar det näst sista objektets artist_name'''   
    TrackList_object.sort()

    for i in range(len(TrackList_object)):
        if TrackList_object[i].artist_name== TrackList_object[-2].artist_name:

            return TrackList_object[i].artist_name



def unsorted_list(TrackList_object,penultimate_artist):
    '''linjärsökning i osorterad lista, returnerar artist_name för näst sista elementet '''  
    for i in TrackList_object:
        if i.artist_name== penultimate_artist:
            return penultimate_artist
        



# Linjärsökning, sorterad och osorterad lista
def linear_search():
    TrackList_object=readfile()
    TrackList_object.sort()
    penultimate_artist= sorted_list(TrackList_object)
    
    
    #sorterad lista
    lintime_sort= timeit.timeit(stmt=lambda: sorted_list(TrackList_object),number=1)

    #osorterad lista
    lintime_unsort= timeit.timeit(stmt=lambda: unsorted_list(TrackList_object,penultimate_artist),number=1)

    print('linjärsökning sorterad lista tog:', round(lintime_sort,4), 'sekunder')
    print('linjärsökning osorterad lista tog:', round(lintime_unsort,4), 'sekunder')


linear_search()



#2 Mergesort


def mergeSort(alist):
   # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)


alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
#print(alist)

#merge_time= timeit.timeit(stmt=lambda: mergeSort(alist),number=100)
#print('sortering med mergesort tog:', round(merge_time,9), 'sekunder')

    


''' 4: Linjärsökning osorterad lista 1000 slumpade element redovisa genomsnittet. '''


def linear_random():
    lintime_random=0
    TrackList_object=readfile()
    random_object= random.choice(TrackList_object)
    for i in range(1000):   
        random_name= random_object.artist_name

        lintime_random+= timeit.timeit(stmt=lambda: unsorted_list(TrackList_object, random_name),number=1)
    print('snitt tiden för linjärsökning med slumpad element tog ', round(lintime_random/1000,4), 'sekunder')

#linear_random()
        

''' 5: Binärsökning i sorterad lista O(log2n)'''

def binary_search(TrackList_object, artist):
   low = 0
   high = len(TrackList_object)-1
   found = False

   while low <= high and not found:
      middle = (low + high)//2
      if TrackList_object[middle].artist_name == artist:
         found = True
      else:
         if artist < TrackList_object[middle].artist_name:
            high = middle - 1
         else:
            low = middle + 1
   return found


def binary_time():
    TrackList_object=readfile()
    artist_object= random.choice(TrackList_object)
    artist_name= artist_object.artist_name
    bintime= timeit.timeit(stmt=lambda: binary_search(TrackList_object, artist_name),number=100)
    print('binärsökning tog ', round(bintime,9), 'sekunder')

binary_time()











