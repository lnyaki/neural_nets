import vectorOperations
from nnLayer import NNLayer
from artificialNeuron import ArtificialNeuron
import math

class NeuralNet():
	SPACE_BETWEEN_LAYERS 	= 200
	SPACE_BETWEEN_NEURONS 	= 10

	LAYER_CONNECTION_DEPH	= 1
	maxNeuronConnections 	= None
	FULLMESH = -1

	position = None
	layers = []

	def __init__(self, position, neuronsPerLayers, maxNeuronConnections = 4):
		self.maxNeuronConnections = maxNeuronConnections
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

		biggestLayerSize = self.getBiggestLayerSize(neuronsPerLayers)

		for i in range(len(neuronsPerLayers)):
			numberOfNeuronsInLayer = neuronsPerLayers[i]
			layers.append(self.generateSingleLayer(i,numberOfNeuronsInLayer, biggestLayerSize))

		return layers

	def getBiggestLayerSize(self,layerSizes):
		maxSize = 0

		for size in layerSizes:
			if(size > maxSize):
				maxSize = size

		return maxSize

	def generateSingleLayer(self, layerNumber,numberOfNeurons, maxLayerSize):
		layerPosition 				= self.computeLayerPosition(layerNumber)
		verticalOffset 				= self.getVerticalLayerOffset(numberOfNeurons,maxLayerSize,NNLayer.neuronSize,NNLayer.NEURON_SPACING) # (0,0)
		verticallyAjustedPosition	= vectorOperations.addVectors(layerPosition,verticalOffset)

		layer 						= NNLayer(verticallyAjustedPosition,numberOfNeurons, layerNumber)
		layer.setVerticalNeuronShift(math.floor((maxLayerSize - numberOfNeurons)/2))

		return layer

	def getVerticalLayerOffset(self,neuronsInLayer, maxLayerSize, neuronSize,neuronSpacing):

		sizeDifference = maxLayerSize - neuronsInLayer

		if(sizeDifference == 0):
			return (0,0)

		verticalDifference = math.floor((sizeDifference * (neuronSize+ neuronSpacing/2)))

		return (0, verticalDifference)

	def computeLayerPosition(self,layerNumber):
		spacingVector 	= (self.SPACE_BETWEEN_LAYERS,0)
		layerOffset 	= vectorOperations.scalarVectorMultiplication(spacingVector,layerNumber)
		

		return vectorOperations.addVectors(self.position,layerOffset)


	def connectAllLayers(self):

		for layerIndex in range(len(self.layers)):
			currentLayer = self.layers[layerIndex]

			layersToConnectTo = self.getLayersToConnectTo(currentLayer.layerIndex, self.LAYER_CONNECTION_DEPH)

			if(not layersToConnectTo):
				continue

			self.connectCurrentLayer(currentLayer,layersToConnectTo)


	def connectCurrentLayer(self,currentLayer,layersToConnectTo):
		

		listNumberOfConnectionsToLayers = self.distributeConnectionsToLayers(layersToConnectTo, self.maxNeuronConnections)

		numberOfLayersToConnect = len(layersToConnectTo)

		for neuron in currentLayer.neurons:

			self.connectNeuronToLayers(neuron,layersToConnectTo, listNumberOfConnectionsToLayers)

			#xxx Connect : we connect to layers. If not enough neurons, we push remaining
			#connections to next layers



	def distributeConnectionsToLayers(self,layersToConnectTo, numberOfNeuronConnections):
		''' Returns a list containing how many connections must be made on each layer
		'''
		layersConnectionList	= []
		availlableConnections 	= numberOfNeuronConnections

		numberOfLayers = len(layersToConnectTo)

		if(numberOfNeuronConnections == self.FULLMESH) and numberOfLayers > 0 :
			layersConnectionList = [len(layersToConnectTo[0].neurons)]

		elif numberOfLayers == 0 :
			pass

		elif(numberOfLayers == 1):
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
		print()
		print("ConnectNeuronToLayer : layers to connect "+str(len(listNumberOfConnectionsToLayers)))


		if len(listNumberOfConnectionsToLayers) > 0:
			
			for i in range(len(layersToConnect)):
				layer = layersToConnect[i]

				numberOfLayerConnections = listNumberOfConnectionsToLayers[i]

				self.connectNeuronToSingleLayer(neuron,layer,numberOfLayerConnections)
				print("Neuron ("+str(neuron.layerID)+" | "+str(neuron.id)+") Total Connections : "+str(len(neuron.connectedNeurons)))


	def connectNeuronToSingleLayer(self,neuron,layer,numberOfNeuronConnections):
		targetNeurons = self.getClosestNeurons(neuron.id,layer,numberOfNeuronConnections)
		#targetNeurons = self.getClosestNeurons2(neuron.neuronSize,layer,numberOfNeuronConnections)
		print("Neuron ("+str(neuron.layerID)+" | "+str(neuron.id)+")  desired connections : "+str(numberOfNeuronConnections))

		for targetNeuron in targetNeurons:
			neuron.connectToNeuron(targetNeuron)
	


		'''
		else:
			neuronList = layer.neurons

			orderedHeightDict = self.getNeuronsHeightDictionary(layer)
			neuronVerticalValue = neuron.position[1]

			returnClosestsNeurons(neuronVerticalValue,heightDict)
			1. Remove vertical value from all elements
			2. square then squareroot
			3. Sort
			4. Take x first

		'''

	def getClosestNeurons2(self, neuronVerticalValue, layer, numberOfNeuronConnections):
		neurons = []

		if(len(layer.neurons) <= numberOfNeuronConnections):
			neurons = layer.neurons

		else:
			heightDict = self.getNeuronsHeightDictionary(layer)

			print("Height DICT result !")
			print(heightDict)

			heightList = self.heightDictToList(heightDict)
			
			print("heightDicToList. Vertical value : "+str(neuronVerticalValue))
			print(heightList)

			# https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
			tupleNeurons = sorted(list(map(lambda x: (x[0],math.sqrt((x[1]-neuronVerticalValue)**2)),heightList )),key=lambda tup: tup[1])
			neurons = [tupleNeurons[x] for x in range(numberOfNeuronConnections)]

		return neurons 


	def heightDictToList(self,heightDict):
		result = []

		for key,value in heightDict.items():
			result.append((key,value))

		return result

	def getClosestNeurons(self,neuronIndex, layer, numberOfNeuronConnections):
		neurons = []

		if(len(layer.neurons) <= numberOfNeuronConnections):
			neurons = layer.neurons

		else:
			neuronRange = self.generateSelectionRange(neuronIndex, numberOfNeuronConnections)

			if(neuronRange and (neuronRange[0])< 0):
				neuronRange = self.shiftRange(neuronRange, (neuronRange[0]*-1))

			elif (neuronRange and (neuronRange[-1])>= len(layer.neurons)):
				neuronRange = self.shiftRange(neuronRange, ((len(layer.neurons)-1) - neuronRange[-1]))

			print("Neuron Index : "+str(neuronIndex)+" Neuron Range : "+str(neuronRange)+" NeuronList length : "+str(len(layer.neurons)))
			neurons = self.getSpecificNeurons(neuronRange, layer.neurons)
				
		return neurons 


	def getNeuronsHeightDictionary(self,layer):

		heightList = {}

		for neuron in layer.neurons:
			heightList[neuron.id] = neuron.position[1]

		return heightList

	def generateSelectionRange(self,neuronIndex, numberOfNeuronConnections):
		neuronRange = []
		halfConnections = math.floor(numberOfNeuronConnections/2)
		numberIsEven = (numberOfNeuronConnections %2 == 0)

		if numberIsEven:
			neuronRange = list(range((neuronIndex - halfConnections) +1, neuronIndex+halfConnections+1))
		else:
			neuronRange = list(range(neuronIndex - halfConnections, neuronIndex+halfConnections+1))

		return neuronRange

	def getSpecificNeurons(self,neuronRange, neuronList):

		neurons = []

		for neuronIndex in neuronRange:
			neurons.append(neuronList[neuronIndex])

		return neurons


	def shiftRange(self,range, shift):
		return list(map(lambda a: a+shift, range))

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


	def draw(self,surface):
		for layer in self.layers:
			layer.draw(surface)