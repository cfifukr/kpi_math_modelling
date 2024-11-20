import matplotlib.pyplot as plt
import numpy as np
from control import tf, step_response
from scipy.signal import lti, lsim

numerator = [3, -1, 3]
denominator = [2, 0, 0, 2]

k_u = 0.01
numerator_feedback = numerator
denominator_feedback = [
    denominator[0],
    denominator[1] + k_u * numerator[0],
    denominator[2] + k_u * numerator[1],
    denominator[3] + k_u * numerator[2],
]

G_feedback = tf(numerator_feedback, denominator_feedback)

A = denominator_feedback  # y(t) коефіцієнти
B = numerator_feedback  # u(t) коефіцієнти

sys_diff_eq = lti(B, A)

t = np.linspace(0, 50, 1000)

t1, y1 = step_response(G_feedback, T=t)

t2, y2, _ = lsim(sys_diff_eq, U=np.ones_like(t), T=t)

plt.figure(figsize=(10, 6))
plt.plot(t1, y1, label="Передатна функція", linestyle='-', color='blue')
plt.plot(t2, y2, label="Диференційне рівняння", linestyle='--', color='orange')
plt.title("Порівняння перехідних характеристик")
plt.xlabel("Час [с]")
plt.ylabel("Амплітуда")
plt.legend()
plt.grid(True)
plt.show()
