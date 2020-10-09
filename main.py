from data import TrainingData

inputData = [9, 8, 7]
# inputData = [5, 4, 3]

training = TrainingData(inputData, 4)
training.create_training_list()
training.print_result()