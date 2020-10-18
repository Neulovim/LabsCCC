from random import seed
from random import random


# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
    new_network = list()
    hidden_layer = [{'weights': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    new_network.append(hidden_layer)
    output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    new_network.append(output_layer)
    return new_network


seed(1)
# network = initialize_network(3, 3, 2)
# for layer in network:
#     print(layer)


# Calculate the derivative of an neuron output
def transfer_derivative(output):
    return output * (1.0 - output)


# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])


# test backpropagation of error
network = [[{'output': 0, 'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],
           [{'output': 0, 'weights': [0.2550690257394217, 0.49543508709194095]},
            {'output': 1, 'weights': [0.4494910647887381, 0.651592972722763]}]]
# expected = [0, 1]
# [0, 0, 1, 1]
expected = [[0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            ]
backward_propagate_error(network, expected)
for layer in network:
    print(layer)
