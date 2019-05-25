import vectorOperations
from nnLayer import NNLayer
from artificialNeuron import ArtificialNeuron
import math

class NeuralNet():
	SPACE_BETWEEN_LAYERS 	= 200
	SPACE_BETWEEN_NEURONS 	= 50

	LAYER_CONNECTION_DEPH	= 1
	MAX_NEURON_CONNECTIONS 	= 4

	position = None
	layers = []

	def __init__(self, position, neuronsPerLayers):
		self.position 	= position
		self.layers 	= self.generateLayers(neuronsPerLayers)
		self.connectAllLayers()
		
	def __str__(self):
		result = ""

		for layer in self.layers:
			result += str(layer)+"\r\n"

		return result

	def generateLayers(self, neuronsPerLayers):
		layers = []

		for i in range(len(neuronsPerLayers)):
			numberOfNeuronsInLayer = neuronsPerLayers[i]
			layers.append(self.generateSingleLayer(i,numberOfNeuronsInLayer))

		return layers

	def connectAllLayers(self):

		for layerIndex in range(len(self.layers)):
			currentLayer = self.layers[layerIndex]

			layersToConnectTo = self.getLayersToConnectTo(currentLayer.layerIndex, self.LAYER_CONNECTION_DEPH)

			if(not layersToConnectTo):
				continue

			self.connectCurrentLayer(currentLayer,layersToConnectTo)


	def connectCurrentLayer(self,currentLayer,layersToConnectTo):
		listNumberOfConnectionsToLayers = self.distributeConnectionsToLayers(len(layersToConnectTo), self.MAX_NEURON_CONNECTIONS)

		numberOfLayersToConnect = len(layersToConnectTo)

		for neuron in currentLayer.neurons:

			self.connectNeuronToLayers(neuron,layersToConnectTo, listNumberOfConnectionsToLayers)

			#xxx Connect : we connect to layers. If not enough neurons, we push remaining
			#connections to next layers



	def distributeConnectionsToLayers(self,numberOfLayers, numberOfNeuronConnections):
		''' Returns a list containing how many connections must be made on each layer
		'''
		layersConnectionList	= []
		availlableConnections 	= numberOfNeuronConnections

		if(numberOfLayers == 1):
			layersConnectionList.append(numberOfNeuronConnections)
		
		elif (numberOfLayers == 2):
			firstLayerPercentage 	= 0.70
			value1 					= math.ceil(numberOfNeuronConnections * firstLayerPercentage)
			value2 					= numberOfNeuronConnections - value1
			layersConnectionList.append(value1)
			layersConnectionList.append(value2)

		else:
			# Create proper distribution
			pass

		return layersConnectionList


	def connectNeuronToLayers(self,neuron,layersToConnect, listNumberOfConnectionsToLayers):
		if len(listNumberOfConnectionsToLayers) > 0:
			
			for i in range(len(layersToConnect)):
				layer = layersToConnect[i]

				numberOfLayerConnections = listNumberOfConnectionsToLayers[i]

				self.connectNeuronToSingleLayer(neuron,layer,numberOfLayerConnections)


	def connectNeuronToSingleLayer(self,neuron,layer,numberOfNeuronConnections):
		targetNeurons = self.getClosestNeurons(neuron.id,layer,numberOfNeuronConnections)

		map(neuron.connectToNeuron, targetNeurons)

		'''
		for targetNeuron in targetNeurons:
			neuron.connectToNeuron(targetNeuron)
		'''

	def getClosestNeurons(self,neuronIndex, layer, numberOfNeuronConnections):
		neurons = []

		if(len(layer.neurons) <= numberOfNeuronConnections):
			neurons = layer.neurons

		else:
			numberIsEven = (numberOfNeuronConnections %2 == 0)

			halfConnections = math.floor(numberOfNeuronConnections/2)
			neuronRange = []

			if numberIsEven:
				neuronRange = range(numberOfNeuronConnections - halfConnections +1, neuronIndex+halfConnections)
			else:
				neuronRange = range(numberOfNeuronConnections - halfConnections, neuronIndex+halfConnections)

			if(neuronRange and (neuronRange[0])< 0):
				self.shiftRange(neuronRange, (neuronRange[0]*-1))

			elif (neuronRange and (neuronRange[-1])>= len(layer.neurons)):
				self.shiftRange(neuronRange, (len(layer.neurons) - neuronRange[-1]))

		return neurons 

	def shiftRange(self,range, shift):
		return map(lambda a: a+shift, range)

	def getLayersToConnectTo(self,currentLayerIndex, connectionDepth):
		maxPossibleIndex 	= len(self.layers)-1
		layers 				= []

		if currentLayerIndex >= maxPossibleIndex:
			return layers
		
		
		nextLayerIndex 	= currentLayerIndex + 1
		lastLayerIndex 	= nextLayerIndex + connectionDepth
		layersIndex 	= range(nextLayerIndex,lastLayerIndex)

		for i in layersIndex:
			layers.append(self.layers[i])

		return layers

	def generateSingleLayer(self, layerNumber,numberOfNeurons):
		layerPosition 	= self.computeLayerPosition(layerNumber)
		layer 			= NNLayer(layerPosition,numberOfNeurons, layerNumber)

		return layer

	def computeLayerPosition(self,layerNumber):
		spacingVector 	= (self.SPACE_BETWEEN_LAYERS,0)
		layerOffset 	= vectorOperations.scalarVectorMultiplication(spacingVector,layerNumber)
		

		return vectorOperations.addVectors(self.position,layerOffset)

	def draw(self,surface):
		for layer in self.layers:
			layer.draw(surface)