import json

import jsonpickle

from core.learning.training_set import TrainingSet
from impl.activation_functions.linear import Linear
from impl.activation_functions.tanh import Tanh
from impl.input_functions.weighted_sum import WeightedSum
from impl.multi_layer_perceptron import MultiLayerPerceptron


training_set = TrainingSet()

training_set.append([0.0, 1.0], [1.0])

n = MultiLayerPerceptron(0.2, 0)
# n.max_iterations = 10000

input_function = WeightedSum()
activation_function = Tanh()

n.add_layer(2, input_function, Linear())
n.add_layer(2, input_function, activation_function)
n.add_layer(2, input_function, activation_function)
n.add_layer(1, input_function, activation_function)

n00 = n.layers[0].neurons[0]
n01 = n.layers[0].neurons[1]
b0 = n.layers[0].neurons[2]

n10 = n.layers[1].neurons[0]
n11 = n.layers[1].neurons[1]
b1 = n.layers[1].neurons[2]

n20 = n.layers[2].neurons[0]
n21 = n.layers[2].neurons[1]
b2 = n.layers[2].neurons[2]

n30 = n.layers[3].neurons[0]

# Layer 02
n10.input_connections[n00].weight = -0.3
n10.input_connections[n01].weight = 0.7
n10.input_connections[b0].weight = 0.2

n11.input_connections[n00].weight = 0.1
n11.input_connections[n01].weight = 0.9
n11.input_connections[b0].weight = 0.9

# Layer 03
n20.input_connections[n10].weight = 0.6
n20.input_connections[n11].weight = 0.2
n20.input_connections[b1].weight = 0.4

n21.input_connections[n10].weight = -0.5
n21.input_connections[n11].weight = -0.3
n21.input_connections[b1].weight = -0.1

# Layer 04
n30.input_connections[n20].weight = 0.4
n30.input_connections[n21].weight = 0.3
n30.input_connections[b2].weight = 0.0

# print(json.dumps(json.loads(jsonpickle.encode(n)), indent=4, sort_keys=True))

n.learn(training_set)

print(json.dumps(json.loads(jsonpickle.encode(n)), indent=4, sort_keys=True))
