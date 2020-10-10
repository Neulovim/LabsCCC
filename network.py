# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def lineplot(x_data, y_data, x_label="", y_label="", title=""):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw=2, color='#539caf', alpha=1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


class Network(object):
    def __init__(self, input_data, output_data):
        self._input_data = input_data
        self._output_data = output_data
        # сделаем случайные числа более определёнными
        np.random.seed(1)
        # инициализируем веса случайным образом со средним 0
        self._syn0 = 0

    def get_network_results(self):
        self._syn0 = 2 * np.random.random((3, 1)) - 1
        for iteration in range(10000):
            # прямое распространение
            l0 = self._input_data
            l1 = self._get_sigmoid_prime(np.dot(l0, self._syn0))
            # if iteration == 9999:
            #     print(l1_delta)
            #     print(np.dot(l0, syn0))
            #     lineplot(np.dot(l0, syn0), l1)

            # насколько мы ошиблись?
            l1_error = self._output_data - l1

            # перемножим это с наклоном сигмоиды
            # на основе значений в l1
            l1_delta = l1_error * self._get_sigmoid(l1)  # !!!

            # обновим веса
            self._syn0 += np.dot(l0.T, l1_delta)  # !!!

        print("Выходные данные после тренировки:")
        print(l1)

    @staticmethod
    def _get_sigmoid(x):
        """Сигмоида."""
        return 1.0 / (1.0 + np.exp(-x))

    def _get_sigmoid_prime(self, x):
        """Производная сигмоиды."""
        return self._get_sigmoid(x) * (1 - self._get_sigmoid(x))
        # return x * (1 - x)