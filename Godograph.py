import numpy as np
import matplotlib.pyplot as plt

coefficients = [3, 0, 1, 2, 0, 0, 2] #3p^6 + +p^4 + +2p^3 +2

roots = np.roots(coefficients)

print("Корні :")
print(roots)

p = np.linspace(-3, 3, 400)
D_values = np.polyval(coefficients, p)

plt.figure(figsize=(10, 6))
plt.plot(p, D_values, label='D(p)', color='red')
plt.axhline(0, color='black', linestyle='-', lw=1)
plt.axvline(0, color='black', linestyle='-', lw=1)
plt.title('Графік полінома D(p)')
plt.xlabel('p')
plt.ylabel('D(p)')
plt.ylim(-10, 10)
plt.grid()
plt.legend()
plt.show()
