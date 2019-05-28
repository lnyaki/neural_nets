import vectorOperations
from interactiveElement import InteractiveElement

class GUIcontainer(InteractiveElement):
	HORIZONTAL 	= 'horizontal'
	VERTICAL 	= 'vertical'

	def __init__(self, position, direction, padding=10):
		self.elements =[]
		self.direction = direction
		self.nextPosition = (0,0)
		self.padding = padding
		self.position = position

	def add(self,element: InteractiveElement):
		self.elements.append(element)
		element.setContainer(self)
		element.setPosition(self.nextPosition)

		self.nextPosition = self.getNextPosition(self.nextPosition,element, self.direction)

	def getNextPosition(self, currentElementPosition,currentElement, direction):
		nextPosition = currentElementPosition
		
		if(direction == self.HORIZONTAL):
			elementWidth = currentElement.dimension[0]
			vectorList = [currentElementPosition,(self.padding,0), (elementWidth,0)]
			nextPosition = vectorOperations.addVectorList(vectorList)

		elif(direction == self.VERTICAL):
			elementHeight = currentElement.dimension[1]
			vectorList = [currentElementPosition,(0,self.padding), (0,elementHeight)]
			nextPosition = vectorOperations.addVectorList(vectorList)

		return nextPosition

	def draw(self, gameDisplay):
		for element in self.elements:
			element.draw(gameDisplay)