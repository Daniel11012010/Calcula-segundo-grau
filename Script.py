import math
import numpy as np
import matplotlib.pyplot as plt


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


delta = (b**2) - (4*a*c)


if delta < 0:
    print("Não existem raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"x1 é: {x1} e x2 é: {x2}")


x_vals = np.linspace(min(x1, x2) - 2, max(x1, x2) + 2, 400)
y_vals = a * x_vals**2 + b * x_vals + c


plt.plot(x_vals, y_vals, label="y = ax² + bx + c")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Gráfico da equação {a}x² + {b}x + {c}")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.scatter([x1, x2], [0, 0], color='red', label=f"Raízes: x1={x1}, x2={x2}")
plt.scatter(0, c, color='blue', label=f"Ponto C no eixo y (0, {c})")
plt.grid(True)
plt.legend()
plt.show()
