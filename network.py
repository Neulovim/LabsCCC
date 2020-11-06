# -*- coding: utf-8 -*-
import copy

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
    def __init__(self, input_data: list, output_data: list):
        self._input_data = np.array(input_data)
        self._output_data = np.array(output_data).T
        self.N = 0.1
        self.M = 2
        # сделаем случайные числа более определёнными
        np.random.seed(1)
        # инициализируем веса случайным образом со средним 0
        self._syn0 = 0.2 * np.random.random((3, 12)) - 0.1
        self._syn1 = 0.2 * np.random.random((12, 1)) - 0.1
        # print(self._syn0)
        # print(self._syn1)

    def get_network_results(self):
        l0 = []
        l1 = []
        l2 = []
        for iteration in range(600000):
            # прямое распространение
            # проходим вперёд по слоям 0, 1 и 2
            l0 = self._input_data
            l1 = self._get_sigmoid(np.dot(l0, self._syn0))
            l2 = self._get_sigmoid(np.dot(l1, self._syn1))

            # как сильно мы ошиблись относительно нужной величины?
            l2_error = self._output_data - l2

            if (iteration % 100000) == 0:
                print("Error:")
                print(f"%.{16}f" % np.mean(np.abs(l2_error)))
                # print(str(np.mean(np.abs(l2_error))))

            # в какую сторону нужно двигаться?
            # если мы были уверены в предсказании, то сильно менять его не надо
            l2_delta = self.N * l2_error * self._get_sigmoid_prime(l2)

            # как сильно значения l1 влияют на ошибки в l2?
            l1_error = l2_delta.dot(self._syn1.T)

            # в каком направлении нужно двигаться, чтобы прийти к l1?
            # если мы были уверены в предсказании, то сильно менять его не надо
            # перемножим это с наклоном сигмоиды
            # на основе значений в l1
            l1_delta = self.N * l1_error * self._get_sigmoid_prime(l1)  # !!!

            # обновим веса
            self._syn1 += self.M * l1.T.dot(l2_delta)  # !!!
            self._syn0 += self.M * l0.T.dot(l1_delta)  # !!!

        # print("Выходные данные после тренировки:")
        # print(l2)
        return l2

    @staticmethod
    def _get_sigmoid(x):
        """Сигмоида."""
        return 1.0 / (1.0 + np.exp(-x))

    def _get_sigmoid_prime(self, x):
        """Производная сигмоиды."""
        # return self._get_sigmoid(x) * (1 - self._get_sigmoid(x))
        return x * (1 - x)
