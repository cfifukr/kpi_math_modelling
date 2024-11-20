import numpy as np
import scipy.signal as signal
from control import tf, step_response
import matplotlib.pyplot as plt

numerator = [3, -1, 3]
denominator = [2, 0, 0, 2]
G = tf(numerator, denominator)

A, B, C, D = signal.tf2ss(numerator, denominator)

# Відображення матриць простору станів
print("Матриці простору станів:")
print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)

numerator_ss, denominator_ss = signal.ss2tf(A, B, C, D)

numerator_ss = numerator_ss[0]
denominator_ss = denominator_ss[0]

G_ss = tf(numerator_ss, denominator_ss)

print("\nПередатна функція з простору станів:")
print(G_ss)

print("\nЧи тотожні передатні функції?")
print("Тотожність:", np.allclose(G.num[0][0], G_ss.num[0][0]) and np.allclose(G.den[0][0], G_ss.den[0][0]))

t = np.linspace(0, 50, 1000)

t1, y1 = step_response(G, T=t)

sys_diff_eq = signal.lti(A, B, C, D)
t2, y2, _ = signal.lsim(sys_diff_eq, U=np.ones_like(t), T=t)

plt.figure(figsize=(10, 5))
plt.plot(t1, y1, label='Передаточна функція (КФК)')
plt.plot(t2, y2, '--', label='Простір станів (КФС)')
plt.title('Порівняння ступінчатого відгуку КФК та КФС')
plt.xlabel('Час [с]')
plt.ylabel('Відгук')
plt.grid(True)
plt.legend()
plt.show()
