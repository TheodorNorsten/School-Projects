"Class file queue"
from node import Node
from errors import EmptyQueueException



class Queue:
    " class initiering av kön"
    def __init__(self):
        """" initiering av kö, definerar 2 attribut ett för översta noden(head),
        dvs noden som gick in först och den andre för den understa noden(last,
        dvs noden som gick in sist)"""

        self.head = None
        self.last = None


    def enqueue(self, data):
        "metod som skapar ny nod och lägger till i kön"
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            new_node.next = self.last
            self.last = new_node



    def dequeue(self):
        "metod som tar bort nod från kö, om kö är tom lyfts ett exception."
        if self.is_empty():
            raise EmptyQueueException

        q = self.last
        p = self.last.next


        if p is None:
            self.head = None
            self.last = None
            return q.data


        while p.data != self.head.data:
            p = p.next
            q = q.next

        q.next = None
        self.head = q
        return p.data


    def is_empty(self):
        "metod som kontrollerar om kö är tom"
        return self.head is None



    def peek(self):
        "metod som koller på det översta noden dvs head elementet."
        if self.is_empty():
            raise EmptyQueueException

        return self.head.data


    def size(self):
        "metod som retunerar antal noder i kön"
        q = self.last
        count = 0
        while q is not None:
            count += 1
            q = q.next
        return count



if __name__ == '__main__':

    pass
