import vectorOperations
from nnLayer import NNLayer
from artificialNeuron import ArtificialNeuron
class NeuralNet():
	SPACE_BETWEEN_LAYERS 	= 200
	SPACE_BETWEEN_NEURONS 	= 50

	position = None
	layers = []

	def __init__(self, position, neuronsPerLayers):
		self.position 	= position
		self.layers 	= self.generateLayers(neuronsPerLayers)
		

	def generateLayers(self, neuronsPerLayers):
		layers = []

		for i in range(len(neuronsPerLayers)):
			numberOfNeuronsInLayer = neuronsPerLayers[i]
			layers.append(self.generateSingleLayer(i,numberOfNeuronsInLayer))

		return layers

	def generateSingleLayer(self, layerNumber,numberOfNeurons):
		layerPosition 	= self.computeLayerPosition(layerNumber)
		layer 			= NNLayer(layerPosition,numberOfNeurons)

		return layer

	def computeLayerPosition(self,layerNumber):
		spacingVector 	= (self.SPACE_BETWEEN_LAYERS,0)
		layerOffset 	= vectorOperations.scalarVectorMultiplication(spacingVector,layerNumber)
		

		return vectorOperations.addVectors(self.position,layerOffset)

	def draw(self,surface):
		for layer in self.layers:
			layer.draw(surface)