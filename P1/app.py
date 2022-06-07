# "Outputs from previous 3 neuros from previous layer"
inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]  # Every input has an weight
bias = 3  # Every uniuqe nuron has a unique bias


# First step for the output is for the neuron add up all the inputs * weigths + bias
output = inputs[0]*weights[0] + inputs[1] * \
    weights[1] + inputs[2]*weights[2] + bias

print(output)
