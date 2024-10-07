import numpy as np
import matplotlib.pyplot as plt

def D(omega):
    return (3*(1j * omega) ** 6) +\
        ((1j * omega) ** 4) +\
        (2 * (1j * omega) ** 3)\
        + 2


def plot_mikhailov():
    omegas = np.linspace(0, 1.05, 200)
    D_values = D(omegas)

    plt.figure(figsize=(8, 8))
    plt.plot(D_values.real, D_values.imag, label="Годограф Михайлова")
    plt.title("Годограф Михайлова")
    plt.xlabel('Re(D(iω))')
    plt.ylabel('Im(D(iω))')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

plot_mikhailov();