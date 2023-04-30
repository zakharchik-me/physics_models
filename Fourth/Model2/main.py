from math import sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np

state_free = 0  # Свободный электрон
state_not_transparent = 10e12  # Случай непрозрачных стенок потенциальной ямы


def solve_equation(alpha_a, p):
    if alpha_a != 0:
        return cos(alpha_a) + p * sin(alpha_a) / alpha_a


class DefaultCase:
    func = []
    up = []
    down = []

    delta = 20
    x_min = -delta
    x_max = delta
    x = np.arange(x_min, x_max, 0.001)

    def __init__(self, p):
        self.p = p

    def show_plot(self):
        for i in self.x:
            self.func.append(solve_equation(i, self.p))
            self.down.append(-1)
            self.up.append(1)

        plt.title(
            "Cлучай свободного электрона" if self.p == state_free else "Случай непрозрачных стенок потенциальной ямы")
        plt.plot(self.x, self.func)
        plt.plot(self.x, self.down)
        plt.plot(self.x, self.up)
        plt.xlabel("alpha * a")
        plt.ylabel("cos(alpha * a) + P * sin(alpha*a)/(alpha*a)")
        plt.grid()
        plt.show()


class SpecialCase:
    m = 9.1093837 * 10e-31
    h = 6.62607015 * 10e-34
    a = 1
    list_k = np.arange(-1 * pi / a, 1 * pi / a, 0.01)
    list_e = []
    n = 2

    def draw_graph(self, n, a):
        list_k = np.arange(-n * pi / a, -(n - 1) * pi / a, 0.01)
        list_e = []
        sign = 1 if n % 2 == 0 else -1
        shift = (n - 1) * 2.5
        for k in list_k:
            list_e.append(shift + k ** 2 * self.h ** 2 / (2 * self.m) + cos(k * a) * sign)
        plt.plot(list_k, list_e, color=(0, 0, 1))

        list_k = np.arange((n - 1) * pi / a, n * pi / a, 0.01)
        list_e = []
        for k in list_k:
            list_e.append(shift + k ** 2 * self.h ** 2 / (2 * self.m) + cos(k * a) * sign)
        plt.plot(list_k, list_e, color=(0, 0, 1))

    def show_plot(self):
        for k in self.list_k:
            self.list_e.append(k ** 2 * self.h ** 2 / (2 * self.m) - cos(k * self.a))

        plt.plot(self.list_k, self.list_e, color=(0, 0, 1))

        for i in range(2, self.n + 1):
            self.draw_graph(i, self.a)

        y_start, y_end = -1, 1 + (2.5 * (self.n - 1))

        for i in range(1, self.n):
            plt.vlines(i * pi / self.a, y_start, y_end, linestyle=':')
            plt.vlines(-i * pi / self.a, y_start, y_end, linestyle=':')

        plt.title('Случай промежуточных значений Р')
        plt.xlabel('k')
        plt.ylabel('E(k)')
        plt.grid()
        plt.show()


freeElectron = DefaultCase(state_free)
freeElectron.show_plot()

# nonTransparentBorder = DefaultCase(state_not_transparent)
# nonTransparentBorder.show_plot()
#
# specialCase = SpecialCase()
# specialCase.show_plot()
