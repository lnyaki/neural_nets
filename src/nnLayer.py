from artificialNeuron import ArtificialNeuron
import vectorOperations

class NNLayer():
	NEURON_SPACING = 80

	position 	= None
	neurons		= []


	def __init__(self, startPosition, layerSize):
		neuronSize = 40

		self.position 	= startPosition
		self.neurons 	= self.generateNeurons(startPosition,layerSize, neuronSize)

	def generateNeurons(self,layerStartPosition,layerSize,neuronSize):
		neuronList = []

		neuronPosition 			= layerStartPosition
		neuronPositionIncrement = self.getNeuronSpacingVector()

		for neuronId in range(layerSize):
			neuron = ArtificialNeuron(neuronPosition, neuronId)
			neuronList.append(neuron)

			neuronPosition = vectorOperations.addVectors(neuron.position,neuronPositionIncrement)

		return neuronList


	def getNeuronSpacingVector(self):
		return (0, self.NEURON_SPACING)

	def draw(self,gameDisplay):
		for neuron in self.neurons:
			neuron.draw(gameDisplay)