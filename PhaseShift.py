import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
f = 1
omega = 2 * np.pi * f

input_signal = np.sin(omega * t)
output_signal = 0.5 * np.sin(omega * t - np.pi / 4)

A_in = np.max(input_signal)
A_out = np.max(output_signal)
gain = A_out / A_in

peak_in = t[np.argmax(input_signal)]
peak_out = t[np.argmax(output_signal)]
delta_t = peak_out - peak_in
phase_shift = delta_t * omega

print(f"Коефіцієнт посилення (K): {gain}")
print(f"Фазовий зсув (φ): {np.degrees(phase_shift):.2f}°")

plt.figure(figsize=(10, 6))
plt.plot(t, input_signal, label='Вхідний сигнал')
plt.plot(t, output_signal, label='Вихідний сигнал')
plt.axvline(peak_in, color='blue', linestyle='--', label='Пік вхідного сигналу')
plt.axvline(peak_out, color='orange', linestyle='--', label='Пік вихідного сигналу')
plt.title('Вхідний та вихідний сигнали')
plt.xlabel('Час')
plt.ylabel('Амплітуда')
plt.legend()
plt.grid(True)
plt.show()
