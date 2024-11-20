import numpy as np
import matplotlib.pyplot as plt
import control as ctl

import numpy as np
import matplotlib.pyplot as plt
import control as ctl

numerator = [3, -1, 3]  # 3p^2 - p + 3
denominator = [2, 0, 0, 2]  # 2p^3 + 2
system = ctl.TransferFunction(numerator, denominator)

plt.figure(figsize=(8, 8))
ctl.nyquist(system, omega_limits=(1e-2, 1e2))
plt.title('Годограф Найквіста')
plt.xlabel('Дійсна частина')
plt.ylabel('Уявна частина')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
ctl.bode(system, dB=True, Hz=True)
plt.title('Амплітудно-частотна характеристика (АЧХ)')
plt.show()

plt.figure(figsize=(8, 6))
ctl.bode(system, dB=False, Hz=True)
plt.title('Фазово-частотна характеристика (ФЧХ)')
plt.show()
