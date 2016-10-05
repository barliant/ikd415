''' NeuralNet class

Based on video series https://www.youtube.com/watch?v=UJwK6jAStmg
'''

import numpy as np

class Neural_Network(object):
    def __init__(self):
        #define hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSie = 3

        #initialize weights
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, outputLayerSize)

    def forward(self, X):
        #propagate inputs through network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(z):
        #Apply sigmoid activation function
        return 1/(1+np.exp(-z))

NN = Neural_Network()
yHat = NN.forward(X)

