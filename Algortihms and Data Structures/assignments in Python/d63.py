import sys


class Node: # skapar en nod
	def __init__(self, value, nextNode=None):
		self.value = value # sätter värdet på noden
		self.next = nextNode # sätter värdet på nästa nod

class LinkedQ:
	def __init__(self):
		self.__first = None # sätter första nod
		self.__last = None # sätter sista nod

	def enqueue(self, x):	#stoppa in x sist
		ny = Node(x) # ny nod
		if self.__first==None: # om första noden är tom
			self.__first = ny # då blir den nya noden den första noden
			self.__last = ny # sista noden blir också den nya noden
		else:
			gammal = self.__last # spara den förra noden som var sist
			self.__last = ny # nu blir den nya noden den sista noden
			gammal.next = ny # den förra noden blir pekar på den nya noden

	def dequeue(self):	#plocka ut det som står först
		if self.__first==None: # om första noden är tom
			return None # det finns inget att plocka ut
		else:
			nod = self.__first # första noden sparas
			x = nod.value # värdet på första noden
			self.__first = nod.next # första noden blir nästa nod
			return x

	def isEmpty(self):	# kolla om kön är tom
		if self.__first==None: # om första noden är tom
			return True # kön är tom
		else:
			return False # kön är inte tom

class ParentNode:
	def __init__(self, word, parent = None):
		self.word = word
		self.parent = parent

class DictHash:
	def __init__(self, key=None, value=None):
		self.dict = {}

	def store(self, key, data=None): # lagrar data som value i din dictionary, med nyckel som key
		self.dict[key]=data

	def search(self, key): # slår upp nyckel i din dictionary
		return self.dict[key]

	def __getitem__(self, key): # d[nyckel] istället för d.search(nyckel), Länkar till en externa sida.som anropar din search-metod.
		return self.search(key)

	def  __contains__(self, key): # if nyckel in d ? Länkar till en externa sida.som returnerar True om nyckel finns i d, False annars.
		return key in self.dict

def words():
	d = DictHash()
	with open('word3.txt', 'r',encoding='utf-8') as file:
		for line in file:
			line = line.strip()
			d.store(line)
	return d

def makechildren(words, d, usedwords): # word = ordet som ska få barn, d = DictHash hastabell med alla ord, usedwords = använda ord
	children = []
	for item in d.dict.items(): # för varhe ord i hastabellen
		i = item[0]
		if (words[0]==i[0] and words[1]==i[1]) or (words[0]==i[0] and words[2]==i[2]) or (words[2]==i[2] and words[1]==i[1]): # kolla efter ord som har en ändring
			truefalse = i in usedwords # kolla om det ordet finns i usedwords
			if truefalse==False: # om ordet inte finns i usedwords
				children.append(i) # lägg till i listan children
	return children

def queue(startword, endword):
	startwordNode = ParentNode(startword)
	q = LinkedQ()
	q.enqueue(startwordNode)
	d = words()
	usedwords = DictHash()
	usedwords.store(startwordNode.word)

	while not q.isEmpty():
		nextword = q.dequeue()
		if nextword.word == endword:
			return nextword
		children = makechildren(nextword.word, d, usedwords)
		for i in children:
			usedwords.store(i)
			newchild = ParentNode(i, nextword)
			q.enqueue(newchild)
	return None

def writechain(child, chain, startword, endword):
	parent = child.parent
	chain.insert(0, child.word)
	if parent != None:
		writechain(parent, chain, startword, endword)
	else:
		for i in range(len(chain)):
			if chain[i] != endword:
				print(chain[i], "->", end =" ")
			else:
				print(chain[i], end =" ")
		print(" ")

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("parametrar saknas")
		sys.exit()
	elif len(sys.argv[1]) == 3 and len(sys.argv[2]) == 3:
		print("Kortaste vägen från ",  sys.argv[1], " till ", sys.argv[2], " är: ")
		startword = sys.argv[1]
		endword = sys.argv[2]
		nod = queue(startword, endword)
		chain = []
		writechain(nod, chain, startword, endword)
	else:
		print("Den finns ingen väg från ",  sys.argv[1], " till ", sys.argv[2], ".")
