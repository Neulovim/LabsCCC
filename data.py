import copy


class TrainingData:
    def __init__(self, input_data, function):
        self._training_data = []
        self._input_data = input_data

    def create_training_list(self):
        # self._training_data = [self._input_data] * 3
        first_lines = self._preparing_first_lines(self._input_data, 2)
        second_lines = self._change_column_number(first_lines, 1, -1)

        # self._training_data.append([self._input_data] * 3)
        print ("first_lines:")
        print (first_lines)
        print ("second_lines:")
        print (second_lines)
        print ("_training_data:")
        print (self._training_data)

    def _preparing_first_lines(self, input_data, column_number_to_change):
        first_line = copy.deepcopy(input_data)
        second_line = copy.deepcopy(input_data)
        third_line = copy.deepcopy(input_data)
        second_line[column_number_to_change] -= 1
        third_line[column_number_to_change] += 1
        self._training_data.append(first_line)
        self._training_data.append(second_line)
        self._training_data.append(third_line)
        return [first_line] + [second_line] + [third_line]

    def _change_column_number(self, data_lines, column_number_to_change, number_to_change):
        new_data_lines = copy.deepcopy(data_lines)
        for line in new_data_lines:
            line[column_number_to_change] += number_to_change
        return new_data_lines

    def print_result(self):
        print(self._input_data)