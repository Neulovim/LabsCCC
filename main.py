import numpy as np

from data import TrainingData
from network import Network


def print_number(number, digits=2):
    print(f"%.{digits}f" % number)


# initialData = [5, 5, 5]
initialData = [9, 8, 7]

colab = []
for i in range(10):
    for j in range(10):
        for z in range(10):
            colab += [[i, j, z]]

# for line in colab:
#     print(line)
# print(len(colab))
# print(len(colab[0]))

training = TrainingData(initialData, 4)
inputData = training.get_training_list()
# print(len(inputData))
# print(len(inputData[0]))
outputData = training.get_bool_function_results(inputData)
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
print("Results: ")
for line in result:
    for value in line:
#     if value < 1:
        print_number(value, 16)
#         countNumbersLessOne += 1
#
# print(f"countNumbersLessOne: {countNumbersLessOne}")