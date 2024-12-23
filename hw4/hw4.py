import numpy as np
import matplotlib.pyplot as plt


def myfs(Dn, omega0, t):
    fn = np.zeros_like(t, dtype=complex)
    N = len(Dn) // 2  # Assuming Dn has coefficients from -N to N

    # Sum over Fourier series terms
    for k, D in enumerate(Dn):
        n = k - N
        fn += D * np.exp(1j * n * omega0 * t)

    return fn.real  # Return real part for the evaluated Fourier series


# Parameters
N_values = [10, 50]
omega0 = 2 * np.pi
t = np.linspace(0, 1, 1000)

# Create subplots
plt.figure(figsize=(12, 6))

Dn_all = [
    np.where(np.arange(-N, N + 1) == 0, 0.5, 1 / (-1j * 2 * np.pi * np.arange(-N, N + 1)))
    for N in N_values
]

for idx, (N, Dn) in enumerate(zip(N_values, Dn_all), start=1):
    fn = myfs(Dn, omega0, t)

    # Plot the result
    plt.subplot(1, 2, idx)
    plt.plot(t, fn, label=f'N = {N}', color='b')
    plt.plot(t, t % 1, label='Sawtooth Waveform', color='r', linestyle='--')
    plt.title(f'Truncated Fourier Series for Sawtooth')
    plt.xlabel('Time (t)')
    plt.ylabel('Amplitude')

plt.show()
