
class InteractiveElement():

	def __init__(self,position=(0,0)):
		self.position = position

	def checkHover(self):
		pass

	def hover(self):
		pass

	def checkCollision(self,position):
		pass

	def collision(self):
		pass

	def getPosition(self):
		return self.position

	def setPosition(self,position):
		self.postion = position

	def setContainer(self,container):
		self.container = container

	def getContainer(self):
		return self.container

	def draw(self, gameDisplay):
		pass