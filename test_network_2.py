import numpy as np

from network_2 import Network_2

# набор входных данных
X = [[0, 0, 1],
     [0, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]
# выходные данные
y = [[0, 0, 1, 1]]

# X = np.array(X)
# y = np.array(y).T

net = Network_2([3, 3, 2])
nabla_b, nabla_w = net.backprop(X, y)
print("nabla_b:")
print(nabla_b)
print("nabla_w:")
print(nabla_w)
