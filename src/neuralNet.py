import vectorOperations
from nnLayer import NNLayer
from artificialNeuron import ArtificialNeuron
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
		

	def generateLayers(self, neuronsPerLayers):
		layers = []

		for i in range(len(neuronsPerLayers)):
			numberOfNeuronsInLayer = neuronsPerLayers[i]
			layers.append(self.generateSingleLayer(i,numberOfNeuronsInLayer))

		return layers

	def connectAllLayers(self):

		for layerIndex in range(len(self.layers)):
			currentLayer = self.layers[layerIndex]

			layersToConnectTo = self.getLayersToConnectTo(layer.layerIndex, self.LAYER_CONNECTION_DEPH)

			if(not layersToConnect):
				continue

			self.connectCurrentLayer(currentLayer,layersToConnectTo)


	def connectCurrentLayer(currentLayer,layersToConnectTo):
		listNumberOfConnectionsToLayers = distributeConnectionsToLayers(layersToConnectTo, self.MAX_NEURON_CONNECTIONS)

		numberOfLayersToConnect = len(layersToConnectTo)

		for neuron in currentLayer:

			connectNeuronToLayers(neuron,layersToConnectTo, listNumberOfConnectionsToLayers)

			#xxx Connect : we connect to layers. If not enough neurons, we push remaining
			#connections to next layers



	def distributeConnectionsToLayers(layersToConnectTo, numberOfNeuronConnections):
		''' Returns a list containing how many connections must be made on each layer
		'''
		layersConnectionList	= []
		availlableConnections 	= numberOfNeuronConnections

		for layers in layersToConnectTo:
			pass

		return layersConnectionList


	def connectNeuronToLayers(neuron,layersToConnect, listNumberOfConnectionsToLayers):
		if len(listNumberOfConnectionsToLayers) > 0:
			
			for i in range(len(layersToConnect)):
				layer = layersToConnect[i]

				numberOfLayerConnections = listNumberOfConnectionsToLayers[i]

				connectNeuronToSingleLayer(neuron,layer,numberOfLayerConnections)


	def connectNeuronToSingleLayer(neuron,layer,numberOfConnections):
		targetNeurons = self.getClosestNeurons(neuron.id,layer,numberOfNeuronConnections)

		for targetNeuron in targetNeurons:
			neuron.connectToNeuron(targetNeuron)


	def getLayersToConnectTo(currentLayerIndex, connectionDepth):
		maxPossibleIndex 	= len(self.layers)-1
		layers 				= []

		if currentLayerIndex >= maxPossibleIndex:
			return layers
		
		
		nextLayerIndex 	= currentLayerIndex + 1
		lastLayerIndex 	= nextLayerIndex + connectionDepth
		layersIndex 	= range(nextLayerIndex,lastLayerIndex)

		for i in layersIndex:
			layers.append(self.layers[layersIndex])

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