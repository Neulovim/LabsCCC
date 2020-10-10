import numpy as np

from data import TrainingData
from network import Network

inputData = [9, 8, 7]
# inputData = [5, 4, 3]

training = TrainingData(inputData, 4)
training.create_training_list()
training.create_bool_function_results()
training.print_result()

# набор входных данных
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# выходные данные
y = np.array([[0, 0, 1, 1]]).T

network = Network(X, y)
network.get_network_results()