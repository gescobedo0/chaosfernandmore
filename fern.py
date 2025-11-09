import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

x_values = []
y_values = []
x = 0
y = 0
# initialize r, a random number between 0 and 1
r = random.random()
print(r)
for values in range(300):
    if r > 0.93:
        x_new = -.15*x + .28*y
        y_new = 0.26*x + 0.24*y + 0.44
        x_values.append(x_new)
        y_values.append(y_new)
        x = x_new
        y = y_new
        r = random.random()
    if 0.86 < r <= 0.93:
        x_new = 0.2*x - 0.26*y
        y_new = 0.23*x + 0.22*y + 1.6
        x_values.append(x_new)
        y_values.append(y_new)
        x = x_new
        y = y_new
        r = random.random()
    if 0.01 < r <= 0.86:
        x_new = -0.85*x + 0.04*y
        y_new = -0.04*x + 0.85*y + 1.6
        x_values.append(x_new)
        y_values.append(y_new)
        x = x_new
        y = y_new
        r = random.random()
    if r <= 0.01:
        x_new = 0
        y_new = 0.16*y
        x_values.append(x_new)
        y_values.append(y_new)
        x = x_new
        y = y_new
        r = random.random()

plt.scatter(x_values, y_values,  s=1, linewidths = 0.5)
plt.show()