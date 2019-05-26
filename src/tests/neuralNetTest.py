import unittest
import sys
sys.path.append('..')

from nnLayer import NNLayer
from neuralNet import NeuralNet



class NeuralNetTest(unittest.TestCase):

	def RightNumberOfLayersIsGenerated(self):

		print("------==== Test rightNumberOfLayersIsGenerated ======-----")
		layerMap = [4,4,4]

		nn = NeuralNet((0,0),layerMap)

		self.assertEqual(3,len(nn.layers))

	def DistributeConnectionsToLayers(self):
		layerMap 	= [4,3,4]
		nn 			= NeuralNet((0,0),layerMap)

		numberOfNeuronConnections = 20
		numberOfLayers 	= 0
		numberOfLayers2 = 1
		numberOfLayers3	= 2

		print("---=== DistributeConnectionsToLayers : connections : "+str(numberOfNeuronConnections))
		result = nn.distributeConnectionsToLayers(0, numberOfNeuronConnections)
		print("---- Result ----")
		print(result)
		self.assertEqual(len(result),0)


		result = nn.distributeConnectionsToLayers(1, numberOfNeuronConnections)
		self.assertEqual(len(result),1)
		self.assertEqual(result,[20])
		print("---- Result ----")
		print(result)

		result = nn.distributeConnectionsToLayers(2, numberOfNeuronConnections)
		self.assertEqual(len(result),2)
		self.assertEqual(result,[14,6])
		print("---- Result ----")
		print(result)

		print(nn)

	def testGetClosestNeurons(self):
		numberOfNeuronConnections = 4
		layerMap 	= [5,4,3,4]
		nn = self.initNeuralNet(layerMap)

		layerSize 	= 4
		layerIndex 	= 0

		layer = NNLayer((0,0),layerSize,layerIndex)
		neuronIndex = 0

		print("------==== Calling getClosestNeurons ======-----")
		result = nn.getClosestNeurons(neuronIndex,layer,numberOfNeuronConnections)

		self.assertEqual(len(result),layerSize)

		result = nn.getClosestNeurons(neuronIndex,layer,numberOfNeuronConnections-1)
		self.assertEqual(len(result),numberOfNeuronConnections-1)
		print("------==== After getClosestNeurons ====-------")

	def ShiftRange(self):
		print()
		print("||||||| ------======= Shift Range")
		numRange = [0,1,2]
		shift = 2
		expectedResult = [2,3,4]

		nn = self.initNeuralNet([4,5,4])
		result = nn.shiftRange(numRange,shift)

		print("Range : "+str(numRange)+" "+str(result)+" Shift value : "+str(shift))
		self.assertEqual(result, expectedResult)

		print("||||||| ------======= Shift Range]")

	def testRange(self):
		result = list(range(-1,1+1))
		print("XXXX result range : "+str(result))
		self.assertEqual(result,[-1,0,1])


	def initNeuralNet(self,layerMap):
		return NeuralNet((0,0),layerMap)

if __name__ == '__main__':
	unittest.main()