# -*- coding: utf-8 -*-
"""
Example of use Hopfield Recurrent network
=========================================

Task: Recognition of letters

"""
# https://code.google.com/archive/p/neurolab/


import numpy as np
import neurolab as nl

A = [-1, -1, -1, 1, 1, -1, -1, -1,
     -1, -1, 1, 1, 1, 1, -1, -1,
     -1, -1, 1, -1, -1, 1, -1, -1,
     -1, -1, 1, 1, 1, 1, -1, -1,
     -1, 1, -1, -1, -1, -1, 1, -1,
     1, -1, -1, -1, -1, -1, -1, 1]

L = [1, 1, -1, -1, -1, -1, -1, -1,
     1, 1, -1, -1, -1, -1, -1, -1,
     1, 1, -1, -1, -1, -1, -1, -1,
     1, 1, -1, -1, -1, -1, -1, -1,
     1, 1, 1, 1, 1, -1, -1, -1,
     1, 1, 1, 1, 1, -1, -1, -1]

N = [1, -1, -1, -1, -1, 1, 1, -1,
     1, 1, -1, -1, -1, 1, 1, -1,
     1, 1, 1, -1, -1, 1, 1, -1,
     1, 1, -1, 1, -1, 1, 1, -1,
     1, 1, -1, -1, 1, 1, 1, -1,
     1, 1, -1, 1, -1, 1, 1, -1]

E = [1, 1, 1, 1, 1, 1, -1, -1,
     1, 1, -1, -1, -1, -1, -1, -1,
     1, 1, 1, 1, 1, -1, -1, -1,
     1, 1, 1, 1, 1, -1, -1, -1,
     1, 1, -1, -1, -1, -1, -1, -1,
     1, 1, 1, 1, 1, 1, -1, -1]

R = [1, 1, 1, 1, 1, 1, -1, -1,
     1, 1, -1, -1, -1, 1, 1, -1,
     1, 1, -1, -1, -1, 1, 1, -1,
     1, 1, 1, 1, 1, 1, -1, -1,
     1, 1, -1, -1, 1, 1, -1, -1,
     1, 1, -1, -1, -1, 1, 1, -1]

N_T = [1, -1, -1, -1, -1, 1, -1, -1,
       1, -1, -1, -1, -1, 1, -1, -1,
       1, 1, 1, -1, -1, 1, -1, -1,
       1, -1, -1, 1, -1, 1, -1, -1,
       1, -1, -1, -1, 1, 1, -1, -1,
       1, -1, -1, 1, -1, 1, -1, -1]

# A, L, N, E, R
target = [A, L, N, E, R]

chars = ['A', 'L', 'N', 'E', 'R']
target = np.asfarray(target)
# target[target == 0] = -1

# Create and train network
net = nl.net.newhop(target)

output = net.sim(target)
print("Test on train samples:")
for i in range(len(target)):
    print(chars[i], (output[i] == target[i]).all())

print("\nTest on defaced N:")
test = np.asfarray(N_T)
# test[test == 0] = -1
out = net.sim([test])
print((out[0] == target[0]).all(), 'Sim. steps', len(net.layers[0].outs))
