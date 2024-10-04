import numpy as np
import matplotlib.pyplot as plt

def T_7(x):
    return np.cos(7 * np.arccos(x))

x = np.linspace(-1, 1, 400)
y = T_7(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='T(x)', color='blue')
plt.title('Поліном Чебишева 7-го порядку')
plt.xlabel('x')
plt.ylabel('T(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.ylim(-1.5, 1.5)
plt.show()
