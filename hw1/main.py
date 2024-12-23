import numpy as np
import matplotlib.pyplot as plt

#PART A
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define the time range and step size
# t = np.arange(-10, 10.2, 0.2)
#
# # Define the function e^−t * cos(2πt)
# y = np.exp(-t) * np.cos(2 * np.pi * t)
#
# # Plot the function
# plt.figure(figsize=(8, 6))
# plt.plot(t, y, label=r'$e^{-t} \cdot \cos(2\pi t)$')
# plt.title(r'Plot of $e^{-t} \cdot \cos(2\pi t)$')
# plt.xlabel('t')
# plt.ylabel('y')
# plt.grid()
# plt.show()

#PART B
# #Define the ReLU function as described
# def relu(t):
#      return np.maximum(0, t)
#
# # Define the time range and step size for -5 <= t <= 5 with a step size of 0.1
# t = np.arange(-5, 5.1, 0.1)
#
# # Apply the ReLU function
# y = relu(t)
#
# # Plot the function
# plt.figure(figsize=(8, 6))
# plt.plot(t, y, label=r'ReLU function: $x(t) = \max(0, t)$', color='blue')
# plt.title(r'Plot of ReLU function: $x(t) = \max(0, t)$')
# plt.xlabel('t')
# plt.ylabel('x(t)')
# plt.grid()
# plt.show()

#PART C
# # Define functions to compute the even and odd parts of a function
def relu(t):
    return np.maximum(0, t)
def even(t, f):
    return 0.5 * (f(t) + f(-t))

def odd(t, f):
    return 0.5 * (f(t) - f(-t))

# Define the time range for -5 <= t <= 5 with a step size of 0.1
t = np.arange(-5, 5.1, 0.1)

# Compute the even and odd parts of the ReLU function
even_relu = [even(tt, relu) for tt in t]
odd_relu = [odd(tt, relu) for tt in t]

# Plot the even and odd parts of the ReLU function
plt.figure(figsize=(10, 6))

# Plot even part
plt.plot(t, even_relu, label='Even Part', color='green')

# Plot odd part
plt.plot(t, odd_relu, label='Odd Part', color='red')

# Configure the plot
plt.title('Even and Odd')
plt.xlabel('t')
plt.ylabel('Function Value')
plt.grid()
plt.show()


