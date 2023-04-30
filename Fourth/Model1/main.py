import matplotlib.pyplot as plt
import numpy as np
import math

##########################################
u = [1, 4, 9]
Q_small = 1
Q_big = 4

delta = 10
t = np.linspace(-2 * math.pi, 4 * math.pi, 1000)

fig, ax = plt.subplots(2, 2)

ax[0, 0].set_title(f'Четные состояния, Q = {Q_small}')
ax[0, 0].set_xlim(0, delta)
ax[0, 0].set_ylim(-delta / 2, delta)
ax[0, 0].grid()

ax[1, 0].set_title(f'Нечетные состояния, Q = {Q_small}')
ax[1, 0].set_xlim(0, delta)
ax[1, 0].set_ylim(-delta / 2, delta)
ax[1, 0].grid()

ax[0, 1].set_title(f'Четные состояния, Q = {Q_big}')
ax[0, 1].set_xlim(0, delta)
ax[0, 1].set_ylim(-delta / 2, delta)
ax[0, 1].grid()

ax[1, 1].set_title(f'Нечетные состояния, Q = {Q_big}')
ax[1, 1].set_xlim(0, delta)
ax[1, 1].set_ylim(-delta / 2, delta)
ax[1, 1].grid()

tan_values = np.tan(t)
cot_values = -1 / np.tan(t)

y2_00 = y2_10 = y2_01 = y2_11 = []

for i in u:
    y2_00 = np.sqrt(i * Q_small ** 2 - t ** 2) / t
    ax[0, 0].plot(t, y2_00, 'g')

    y2_10 = np.sqrt(i * Q_small ** 2 - t ** 2) / t
    ax[1, 0].plot(t, y2_10, 'g')

    y2_01 = np.sqrt(i * Q_big ** 2 - t ** 2) / t
    ax[0, 1].plot(t, y2_01, 'g')

    y2_11 = np.sqrt(i * Q_big ** 2 - t ** 2) / t
    ax[1, 1].plot(t, y2_11, 'g')

tan_values[:-1][np.diff(tan_values) < 0] = np.nan
cot_values[:-1][np.diff(cot_values) < 0] = np.nan

ax[0, 0].plot(t, tan_values)
ax[1, 0].plot(t, cot_values)
ax[0, 1].plot(t, tan_values)
ax[1, 1].plot(t, cot_values)
plt.figure(1)
##########################################
delta = 10
plt.figure(2)
Q = 3
u = [1, 2, 9]
odd_values = []
even_values = []

t = np.linspace(-2 * math.pi, 4 * math.pi, 1000)
tan_values = np.tan(t)
tan_values[:-1][np.diff(tan_values) < 0] = np.nan
plt.xlim(-delta / 2, delta / 2)
plt.ylim(-delta, delta)
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')

for i in u:
    odd_values = np.sqrt(i * Q ** 2 - t ** 2) / t
    even_values = - (t / np.sqrt(i * Q ** 2 - t ** 2))

    plt.plot(t, odd_values, 'g')
    plt.plot(t, even_values, 'g')

plt.plot(t, tan_values)
plt.grid()
##########################################
plt.figure(3)

h = 1.0545726
w = 1
n = 10

x = []
y = []

for i in range(-n, n + 1):
    temp = (abs(i) + 0.5) * h * w
    y.append(temp)
    x.append(i / temp)

for i in range(n + 1):
    plt.hlines(y[i], x[i], -x[i], colors='red')

x = []
y = []
step = 0.1

for i in range(-n, n):
    start = i
    end = i + 1
    while start < end:
        temp = (abs(start) + 0.5) * h * w
        y.append(temp)
        x.append(start / temp)
        start += step

plt.plot(x, y)
ax = plt.gca()
ax.set_xlabel('x')
ax.set_ylabel('U(x)')
plt.grid()
##########################################
fig, ax = plt.subplots(2)

x1 = np.linspace(-1, 0, 1000)
x2 = np.linspace(0, 1, 1000)
k_values = [1.8365, 4.8158]
a = 1

for i in range(0, len(k_values)):
    y1 = -np.sqrt(2 * k_values[i] / (2 * k_values[i] * a - np.sin(2 * k_values[i] * a))) * \
         np.sin(k_values[i] * (x1 + a))
    y2 = np.sqrt(2 * k_values[i] / (2 * k_values[i] * a - np.sin(2 * k_values[i] * a))) * np.sin(k_values[i] * (x2 - a))
    ax[i].plot(x1, y1)
    ax[i].plot(x2, y2)
    ax[i].set_title(f'k = {k_values[i]}')
    plt.xlim(-1, 1)
    ax[i].grid()

plt.figure(4)
plt.show()
