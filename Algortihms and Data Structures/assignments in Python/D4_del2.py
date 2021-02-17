import timeit
import matplotlib.pyplot as plt 

class Song():
    ''' Song klass med attributen artist_name, song_title, track_length, year'''
    def __init__(self, artist_id, artist_name, song_title, track_length, year):

        self.artist_id = artist_id
        self.artist_name = artist_name
        self.song_title = song_title
        self.track_length = track_length
        self.year= year


    def __lt__(self,other):
        ''' lt metod som jmf vilket objekt som är minst beroende på attributet track_length'''

        if self.track_length > other.track_length:
            return True

        else:
            return False


    def __repr__(self):
        return (self.artist_id + ' ' + self.artist_name + ' ' + self.song_title + ' ' + str(self.track_length) + ' ' + self.year)
        
        



'''läser in filen och lagrar varje låts attribut till Song-objekt och lägger in alla objekt i lista.
    UT: lista där varje element i listan är ett objekt.'''
def readfile():
    track_file=open('song_artist.txt','r',encoding='utf-8')
    tracks= track_file.readlines()
    TrackList_object=[]

    for i in tracks[:100000]:
        i=i.strip()
        splitting_line= i.split('\t')
        artist_id = splitting_line[0]
        artist_name = splitting_line[1]
        song_title = splitting_line[2]
        track_length = float(splitting_line[3])
        year= splitting_line[4]

        TrackList_object.append(Song(artist_id ,artist_name , song_title, track_length, year))

    track_file.close()

    return TrackList_object




#Metod 1 upprepade linjärsökningar

def linear_search(TrackList_object,k):

    ''' funktionen linjärsöker efter den k längsta låten, tar bort det längsta låten efter varje iteration
    tills k funnits returnerar den k-längsta sångtiteln.'''
    
    for j in range(k-1):
        max_length= TrackList_object[0].track_length
        max_index= 0
        for i in range(1,len(TrackList_object)):
            if max_length < TrackList_object[i].track_length:
                max_length,max_index = TrackList_object[i].track_length, i


        #print(TrackList_object[max_index])
        del TrackList_object[max_index]


    max_Index= 0
    max_Length= TrackList_object[0].track_length
    ''' Måste loopa en sista gång för att få ut det k-största elementet '''
    for i in range(1,len(TrackList_object)):
        if max_Length < TrackList_object[i].track_length:
            max_Length,max_Index = TrackList_object[i].track_length, i

    return TrackList_object[max_Index].song_title


'''
Tracklist=readfile()
k=3
print('Den ',k, ' längsta låten är: ' ,linear_search(Tracklist,k))
time_linear = timeit.timeit(stmt = lambda: linear_search(Tracklist, k), number = 1)
print('linjärsökning i osorterad lista tog:', round(time_linear ,9), 'sekunder\n')'''






#Metod 2 Sortera och plocka ut

def mergeSort(alist):
    #print("Splitting ",alist)
    
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
            if lefthalf[i].track_length <= righthalf[j].track_length:
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
    

    return alist


  
def merge_find(Tracklist,k):    
    
    #lista=mergeSort(Tracklist)
    #Tracklist.reverse()
    return mergeSort(Tracklist)[k-1].song_title


'''
k=15
Tracklist= readfile()

print('Den ', k ,'längsta låten är: ', merge_find(Tracklist,len(Tracklist)-(k-1)))
time_mergeSort= timeit.timeit(stmt= lambda: merge_find(Tracklist,k),number=1)
print('mergesort i sorterad lista tog:', round(time_mergeSort ,9), 'sekunder\n')'''







def main():
    linear_list=[]
    merge_list=[]
    k_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    Tracklist= readfile()
    k=1

    while k<=100:    
        time_linear = timeit.timeit(stmt = lambda: linear_search(Tracklist, k), number = 5)
        print('linjärsökning i osorterad lista tog:', round(time_linear ,9), 'sekunder\n')

        time_mergeSort= timeit.timeit(stmt= lambda: merge_find(Tracklist,k),number=5)
        print('mergesort i sorterad lista tog:', round(time_mergeSort ,9), 'sekunder\n')

        #print(k,time_linear,time_mergeSort)
        k+=5

        linear_list.append(time_linear)
        merge_list.append(time_mergeSort)
        


    plt.plot(k_list,linear_list)
    plt.plot(k_list,merge_list)
    plt.show()
    
    
     
main()







