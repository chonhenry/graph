#Implementation of graph using adjacent list
class graph:
	def __init__(self):
		self.numOfNode=0
		self.adjlist={}
	
	def addVertex(self, node):
		if node not in self.adjlist:
			self.numOfNode+=1
			self.adjlist[node]=[]

	def addEdge(self, node1, node2):
		self.adjlist[node1].append(node2)
		self.adjlist[node2].append(node1)

	def printgraph(self):
		for i in self.adjlist.items():
			print(i)

myGraph = graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')

myGraph.addEdge('3', '1') 
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')
myGraph.printgraph()

















