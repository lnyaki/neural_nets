import unittest
import sys
sys.path.append('..')

from neuralNet import NeuralNet



class NeuralNetTest(unittest.TestCase):

	def testRightNumberOfLayersIsGenerated(self):
		layerMap = [4,5,6]

		nn = NeuralNet((0,0),layerMap)

		self.assertEquals(3,len(nn.layers))

	def testDistributeConnectionsToLayers():

		distributeConnectionsToLayers(layersToConnect, numberOfNeuronConnections)

if __name__ == '__main__':
	unittest.main()