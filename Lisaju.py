import numpy as np
import matplotlib.pyplot as plt


A = 1
omega1 = 1
omega2 = 1
phi_values = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]

def plot_lissajous(omega1, omega2, phi, title):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = A * np.sin(omega1 * t)
    y = A * np.sin(omega2 * t + phi)

    plt.plot(x, y, label=f'phi = {phi:.2f} rad')


# 1 ранг

plt.figure(figsize=(10, 8))

for phi in phi_values:
    plot_lissajous(omega1, omega2, phi, 'Lissajous Figure 1st Rank')

plt.title('Фігури Лісажу 1-го рангу (ω1/ω2 = 1)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()

# 2 ранг

omega2 = 2
plt.figure(figsize=(10, 8))
for phi in phi_values:
    plot_lissajous(omega1, omega2, phi, 'Lissajous Figure 2nd Rank')

plt.title('Фігури Лісажу 2-го рангу (ω1/ω2 = 2)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()