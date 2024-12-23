import numpy as np
import matplotlib.pyplot as plt
#PART A
T = 2  # Period in seconds
omega = 3.14159  # Angular frequency corresponding to a period of 2 seconds
sigma = -0.109861
#set y(10) = 1/3 = e^(sigma*10)*e^(jw(t)
#e^(jw(t) magnitude cos^2(wt) + sin^2(wt) = 1
#solving for sigma = -0.109861...
time = np.linspace(0, 10, 500)
y = np.exp((sigma + 1j * omega) * time)

#PART B
#i
real = np.real(y)
imaginery = np.imag(y)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
ax1.plot(time, real, label="Real", color="red")
ax1.set_title("Real")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")

ax2.plot(time, imaginery, label="Imaginary", color="blue")
ax2.set_title("Imaginary")
ax2.set_xlabel("Time")
ax2.set_ylabel("Amplitude")

#ii
plt.figure(figsize=(12, 5))
plt.plot(real, imaginery, label="imagiery as a function of real", color="yellow")
plt.title("imaginery as a function of real")
plt.xlabel("Real")
plt.ylabel("Imaginery")
#After plotting it seems to be in a spiral shape, which means that the signal will trace a
#in a spiral manner in the complex plane aka a phasor. if it didn't decay i think it would be
#a perfect circle, however since it is exponential decay it is instead skrinking from the outside in

#PART C
m = np.abs(y)
p = np.angle(y) / (2 * 3.14159)  # Convert phase angle to cycles
plt.figure(figsize=(12, 6))
plt.plot(time, m, label="magnitude", color="blue")
plt.plot(time, p, label="phase", color="red")
plt.title("Magnitude and Phase")
plt.xlabel("Time")
plt.ylabel("Amplitude")

#only do plt show once per code
plt.show()
print(y)