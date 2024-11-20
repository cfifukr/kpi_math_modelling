import seaborn as sbs
import matplotlib.pyplot as plt
from control import tf, step_response
import numpy as np
from scipy.signal import tf2zpk


numerator = [3, -1, 3]  # 3p^2 - p + 3
denominator = [2, 0, 0, 2]  # 2p^3 + 2


def is_stable(num, den):
    _, poles, _ = tf2zpk(num, den)
    return all(p.real < 0 for p in poles)


def create_stable_system(num, den, k_u):
    num_stable = [k_u * n for n in num]
    den_stable = [
        den[0],
        den[1] + 0.5 * k_u * num[0],
        den[2] + 0.5 * k_u * num[1],
        den[3] + 0.5 * k_u * num[2]
    ]

    stable_result = is_stable(num_stable, den_stable)
    print(
        f"Система : {num_stable}/{den_stable}, k_u = {k_u}, "
        f"Результат: {stable_result}"
    )

    return num_stable, den_stable


k_test = [ 0.01, 0.1, 1, 2, 5,  10, 20, 30, 50, 100]

t = np.linspace(0, 50, 1000)
_, y_unstable = step_response(tf(numerator, denominator), T=t)

plt.figure(figsize=(10, 6))
plt.plot(t, y_unstable, label='Нестабільна система')

for k in k_test:
    num_test, den_test = create_stable_system(numerator, denominator, k)
    _, y_stable = step_response(tf(num_test, den_test), T=t)
    plt.plot(t, y_stable, label=f'k_u = {k}')

plt.title('Порівняння перехідних характеристик')
plt.xlabel('Час')
plt.ylabel('Амплітуда')
plt.legend()
plt.grid(True)
plt.show()

