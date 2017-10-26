from Board import Board

class maxNode:
	def __init__(self, minParent, childList, ): 
		self.minParent = minParent
		self.childList = childList


	def insertChild(self, val):
		self.childList += val

	def setParent(self, minNode):
		self.minParent = minNode

	def getValue(self):
		return self.value

class minNode:
	def __init__(self, maxParent, childList, value):
		self.maxParent = maxParent
		self.childList = childList

	def insertChild(self, val):
		self.childList += val

	def setParent(self, maxNode):
		self.minParent = maxNode

class minimaxTree:
	def __init__(self, root, children):
		self.root = root
		self.children = children

	def insertChild(self, child):
		self.children += child

	def getRoot(self):
		return self.root



