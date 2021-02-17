from linkedQFile import *
from d5_ver2 import *
class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

		


def words():
	d = []
	with open('word3.txt', 'r') as file:
		for line in file:
			line = line.strip()
			d.append(line)
	return d

def makechildren(words, d, usedwords): # word = ordet som ska få barn, d = BinTree hastabell med alla ord, usedwords = använda ord 
	children = []
	for i in d: # för varhe ord i hastabellen
		if words[0]==i[0] and words[1]==i[1]: # kolla efter ord som har en ändring
			truefalse = i in usedwords # kolla om det ordet finns i usedwords
			if truefalse==False: # om ordet inte finns i usedwords
				children.append(i) # lägg till i listan children
		elif words[0]==i[0] and words[2]==i[2]:
			truefalse = i in usedwords # kolla om det ordet finns i usedwords
			if truefalse==False: # om ordet inte finns i usedwords
				children.append(i) # lägg till i listan children
		elif words[2]==i[2] and words[1]==i[1]:
			truefalse = i in usedwords # kolla om det ordet finns i usedwords
			if truefalse==False: # om ordet inte finns i usedwords
				children.append(i) # lägg till i listan children 			
	return children


def queue2():
	startword = ParentNode("fan")
	endword = "gud"

	q = LinkedQ()
	q.enqueue(startword)

	d = words()

	usedwords = BinTree()
	usedwords.store(startword.word, startword.word)

	while not q.isEmpty():
		nextword = q.dequeue()
		if nextword.word == endword:
			return nextword
		children = makechildren(nextword.word, d, usedwords)
		for i in children:
			usedwords.store(i, i)
			newchild = ParentNode(i, nextword)
			q.enqueue(newchild)
	return None

def writechain(child, chain):
	startword = "fan"
	endword = "gud"
	parent = child.parent
	chain.insert(0, child.word)
	if parent != None:
		writechain(parent, chain)
		#print(child.word, end=" ")
	else:
		for i in range(len(chain)):
			if chain[i] != endword:
				print(chain[i], "->", end =" ")
			else:
				print(chain[i], end =" ")
		print(" ")

nod = queue2()
chain = []
writechain(nod, chain)



