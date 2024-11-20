import matplotlib.pyplot as plt
from control import tf, impulse_response, step_response
import numpy as np

numerator = [3, -1, 3]  # 3p^2 - p + 3
denominator = [2, 0, 0, 2]  # 2p^3 + 2
k_u = 0.01

def create_stable_system(num, den, k_u):
    num_stable = [k_u * n for n in num]
    den_stable = [
        den[0],
        den[1] + 0.5 * k_u * num[0],
        den[2] + 0.5 * k_u * num[1],
        den[3] + 0.5 * k_u * num[2]
    ]
    return num_stable, den_stable

num_stable, den_stable = create_stable_system(numerator, denominator, k_u)
system = tf(num_stable, den_stable)

t = np.linspace(0, 50, 1000)

t_impulse, y_impulse = impulse_response(system, T=t)

t_step, y_step = step_response(system, T=t)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(t_impulse, y_impulse, label='Імпульсна характеристика', color='blue')
plt.title('Імпульсна характеристика (k_u = 0.01)')
plt.xlabel('Час')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t_step, y_step, label='Перехідна характеристика', color='green')
plt.title('Перехідна характеристика (k_u = 0.01)')
plt.xlabel('Час')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
