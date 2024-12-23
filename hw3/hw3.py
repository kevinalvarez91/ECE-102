import numpy as np
import matplotlib.pyplot as plt

#PARTA
# Define the rectangular function
def rect(t):
    return np.where((t >= -0.5) & (t <= 0.5), 1.0, 0.0)
# Define the ramp function
def ramp(t):
    return np.where(t >= 0, t, 0.0)

# Define the functions f(t) and g(t)
def f(t):
    return 2 * rect(t - 3/2)

def g(t):
    return 2 * ramp(t - 1) * rect(t - 3/2)

# Modified nconv function to handle non-integer step counts in ty
def nconv(x, tx, h, th):
    y = np.convolve(x, h) * (th[1] - th[0])
    ty = np.linspace(tx[0] + th[0], tx[-1] + th[-1], len(y))
    return y, ty
t = np.arange(0, 5, 0.01)
f = f(t)
g = g(t)
y, ty = nconv(f, t, g, t)
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)#f(t)
plt.plot(t, f, label="f(t) = 2rect(t - 3/2)")
plt.xlabel("t")
plt.title("y(t)")
plt.ylabel("f(t)")#g(t)
plt.subplot(3, 1, 2)
plt.plot(t, g, label="g(t) = 2r(t - 1)rect(t - 3/2)")
plt.xlabel("t")
plt.title("g(t)")
plt.ylabel("g(t)")#convulition
plt.subplot(3, 1, 3)
plt.plot(ty, y, label="y(t) = f(t) * g(t)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Convolution")

#PART B
t_l = np.arange(-1, 2, 0.01)
h = rect(t_l)
j = rect(t_l)
i, iy = nconv(h, t_l, j, t_l)
plt.figure(figsize=(10, 5))
plt.plot(iy, i, label="rect(t) * rect(t)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Convolution of rect(t) & rect(t)")


plt.show()
