from Board import Board

class Node:
	def __init__(self, name, parent, childList, value): 
		self.name = name
		self.parent = parent
		self.childList = childList
		self.bestChildIndex = -1
		self.value = value 

	def insertChild(self, node):
		self.childList.append(node)

	def setParent(self, minNode):
		self.minParent = minNode