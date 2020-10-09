import copy
import math


class TrainingData:
    def __init__(self, input_data, function):
        self._training_data = []
        self._function_results = []
        self._bool_function_results = []
        self._input_data = input_data

    @staticmethod
    def change_column_number(data_lines, column_number_to_change, number_to_change):
        new_data_lines = copy.deepcopy(data_lines)
        for line in new_data_lines:
            line[column_number_to_change] += number_to_change
        return new_data_lines

    def create_training_list(self):
        first_lines = self._preparing_first_lines(self._input_data, 2)
        self._add_missing_lines(first_lines, self._training_data)

        first_lines = self.change_column_number(first_lines, 0, -1)
        self._add_missing_lines(first_lines, self._training_data)

        first_lines = self.change_column_number(first_lines, 0, -1)
        self._add_missing_lines(first_lines, self._training_data)

        print("_training_data:")
        print(self._training_data)

    def create_bool_function_results(self):
        self._create_function_results()
        self._bool_function_results = [1 if value > 0 else 0 for value in self._function_results]
        print("_bool_function_results:")
        print(self._bool_function_results)

    def print_result(self):
        print("_input_data: ")
        print(self._input_data)
        print("len _training_data: ")
        print(len(self._training_data))
        print("len _function_results: ")
        print(len(self._function_results))
        print("len _bool_function_results: ")
        print(len(self._bool_function_results))

    def _create_function_results(self):
        self._function_results = [math.tan(line[0]) + math.sin(line[1]) - math.sin(line[2])
                                  for line in self._training_data]
        print("_function_results:")
        print(self._function_results)

    def _add_missing_lines(self, first_lines, combo_lines):
        second_lines = self.change_column_number(first_lines, 1, -1)
        third_lines = self.change_column_number(first_lines, 1, 1)
        combo_lines += first_lines + second_lines + third_lines

    @staticmethod
    def _preparing_first_lines(input_data, column_number_to_change):
        first_line = copy.deepcopy(input_data)
        second_line = copy.deepcopy(input_data)
        third_line = copy.deepcopy(input_data)
        second_line[column_number_to_change] -= 1
        third_line[column_number_to_change] += 1
        return [first_line] + [second_line] + [third_line]