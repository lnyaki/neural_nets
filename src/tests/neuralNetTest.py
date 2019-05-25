import unittest
import sys
sys.path.append('..')

from neuralNet import NeuralNet



class NeuralNetTest(unittest.TestCase):

	def testRightNumberOfLayersIsGenerated(self):
		layerMap = [4,5,6]

		nn = NeuralNet((0,0),layerMap)

		self.assertEqual(3,len(nn.layers))

	def testDistributeConnectionsToLayers(self):
		layerMap 	= [4,5,6]
		nn 			= NeuralNet((0,0),layerMap)

		numberOfNeuronConnections = 20
		numberOfLayers 	= 0
		numberOfLayers2 = 1
		numberOfLayers3	= 2

		result = nn.distributeConnectionsToLayers(0, numberOfNeuronConnections)
		print(result)
		self.assertEqual(len(result),0)


		result = nn.distributeConnectionsToLayers(1, numberOfNeuronConnections)
		print(result)
		self.assertEqual(len(result),1)
		self.assertEqual(result,[20])

		result = nn.distributeConnectionsToLayers(2, numberOfNeuronConnections)
		print(result)
		self.assertEqual(len(result),2)
		self.assertEqual(result,[14,6])

		print(nn)


if __name__ == '__main__':
	unittest.main()