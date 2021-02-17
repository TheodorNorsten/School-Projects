from array import array

class ArrayQ():
    
    def __init__(self):
        self.__item= array('i',[])


    def enqueue(self,new_value):

        return self.__item.append(new_value)
        

    def dequeue(self):
        try:
             return self.__item.pop(0)
        except:
            return 'Tom lista'


    def isEmpty(self):

        return self.__item ==array('i',[])

    def __repr__(self):
        return str(self.__item)






''' Implementera kön som en länkad lista '''

''' Nod klassen '''

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next



''' Länkad lista klassen'''

'''Definition: self.first= underst (längst bak) i kön dvs elementet som gick in sist.
               self.last= Övest (högst upp) i kön dvs elementet som gick in först.'''


class LinkedQ:
    def __init__(self):
        self.first= None
        self.last= None  

    def enqueue(self,data):
        ny_nod= Node(data)

        if self.first==None:
            #ny_nod.next= None
            self.first=ny_nod
            self.last=self.first
               
        else:
            ny_nod.next=self.first
            self.first=ny_nod

        #return self.last.data) + ' ' +  str(self.first.data)
        

    def dequeue(self):
        q= self.first
        p= self.first.next
        
        if q.data==self.last.data:
            self.first=None
            self.last=None
            return q.data
                       
        else:
            while p.data!= self.last.data:
                p=p.next
                q=q.next
                
            q.next=None
            self.last=q        
            return p.data    
    
    def isEmpty(self):       
        return self.first==None


               

    def remove(self,x):

        if self.first== None:
            return 'listan är tom'
        
        q= self.first
        p=self.first.next

        if q.data== x:
            self.first=p
            del q       
          
        else:
            while p.data!=x:              
                 p=p.next
                 q=q.next
                 if p== None:
                     return 'elementet finns inte i listan'
            
            
            if p.next== None:
                q.next=None
                self.last= q
                del p
                
            else:
                q.next=p.next
                del p
            




           

   # def __repr__(self):
        #return  str(self.first) + ' ' + str(self.last)









''' Testfall '''

#noder= LinkedQ()
#print(noder.enqueue(1))
#print(noder.enqueue(2))
#print(noder.enqueue(3))
#print(noder)


''' mittersta element '''
#noder.remove(2)

'''första element '''
#noder.remove(1)

'''Elementet finns inte '''
#print(noder.remove(10))
#print(noder)

''' sista elementet '''
#ndoer.remove(3)

''' ta bort element ur tom lista '''
#noder.remove(1)

#print(noder)

      

















