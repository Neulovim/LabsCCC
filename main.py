import numpy as np

from data import TrainingData
from network import Network


def print_number(number, digits=2):
    print(f"%.{digits}f" % number)


# inputData = [5, 4, 3]
initialData = [9, 8, 7]

training = TrainingData(initialData, 4)
inputData = training.get_training_list()
outputData = training.get_bool_function_results()

training.print_result()

# набор входных данных
X = [[0, 0, 1],
     [0, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]

# выходные данные
y = [[0, 0, 1, 1]]

network = Network(inputData, outputData)
result = network.get_network_results()

# countNumbersLessOne = 0
# print("Results: ")
# for value in result:
#     if value < 1:
#         print_number(value, 16)
#         countNumbersLessOne += 1
#
# print(f"countNumbersLessOne: {countNumbersLessOne}")