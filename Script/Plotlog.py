import numpy as np
import matplotlib.pyplot as plt

# Gera valores de n de 1 a 1000
n_values = np.arange(1, 500000)

# Calcula Theta(n*log_2(n)) para cada valor de n
theta_values = n_values * np.log2(n_values)

# Plota o gráfico
plt.plot(n_values, theta_values, label=r"$\Theta(n \log_2 n)$")

# Configurações do gráfico
plt.xlabel("n")
plt.ylabel("Tempo de execução")
plt.title("Complexidade Theta(n*log_2(n))")
plt.legend()

plt.savefig("Complexidadetheta.png")