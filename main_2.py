import numpy as np

from data import TrainingData
from network import Network


def get_str_number(number, digits=2):
    return f"%.{digits}f" % number


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
X = [[9, 8, 7],
     [9, 8, 6],
     [9, 8, 8],
     [9, 7, 7],
     [9, 7, 6],
     [9, 7, 8],
     [9, 9, 7],
     [9, 9, 6],
     [9, 9, 8],
     [8, 8, 7],
     [8, 8, 6],
     [8, 8, 8],
     [8, 7, 7],
     [8, 7, 6],
     [8, 7, 8],
     [8, 9, 7],
     [8, 9, 6],
     [8, 9, 8],
     [7, 8, 7],
     [7, 8, 6]]
# выходные данные
y = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1]]

network = Network(inputData, outputData)
result = network.get_network_results()

# countNumbersLessOne = 0
print("Results: ")
# print(result)
# print(y)
for value in range(len(result)):
    #     if value < 1:
    print("{0} : {1}".format(get_str_number(result[value], 16), outputData[0][value]))
#         countNumbersLessOne += 1
#
# print(f"countNumbersLessOne: {countNumbersLessOne}")
