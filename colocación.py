# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

"""# Método de colocación.
# Problema a, página 372
$$ 9y'' + \pi^2 y = 0$$
con condiciones de frontera $y(0) = -1, y(3/2) = 3$.

Solución exacta, $y(t) = 3\sin(\pi t/3) - \cos(\pi t/3)$.
"""

# Condiciones del problema
a, b = 0, 3/2
ya, yb = -1, 3
N = 8 # Número de nodos

t = np.linspace(a, b, N)

"""Dada la estructura de la ecuación diferencial, suponiendo que
$$ y(t) = \sum_{j=1}^n c_j t^j $$

tenemos que las constantes satisfacen la ecuaciones
$$c_1 = -1$$
$$ \sum_{j=1}^n [j(j-1)t^{j-2} - 3t^j + 2jt^{j-1}]c_j = 0 $$
$$ \sum_{j=1}^n c_j(3/2)^j = 3 $$

Lo cual se puede representar de forma matricial, considerando los tiempos $t_i$, y se implementara de esa manera.
"""

# Matriz de movimiento
A = np.zeros((N,N))

A[0,0] = 1 # Primera ecuación

# Renglones intermedios
for j in range(N):
  A[1:-1, j] = 9*j*(j-1)*t[1:-1]**(j-2) + (np.pi**2)*t[1:-1]**j #Error de los indeces

# Última ecuación
last = np.zeros(N)
for j in range(N):
  last[j] = (3/2)**j

A[-1, :] = last

# Vector
v = np.zeros(N)
v[0], v[-1] = ya, yb

def colocacion(A, b, t):
  coef = np.linalg.solve(A, b)

  # Modelo propuesto (polinominal)
  y = coef[0]*np.ones(N)
  for i in range(1,N):
    y += coef[i]*t**i
  return y

sol = colocacion(A, v, t)

def y(t):
  return 3*np.sin((np.pi/3)*t ) - np.cos((np.pi/3)*t)

plt.plot(t, sol, '-', label = 'Solución del método')
plt.plot(t, y(t), '--r', label = 'Solución exacta')
plt.plot([a,b], [ya, yb], 'ok', label = 'Cond. Frontera')

plt.title('Método de colocación')
plt.legend()
plt.show()

"""## Problema b, página 372.
$$ y'' = 3y - 2y' $$
con condiciones de frontera $ y (0) = e^3$, $y(1) = 1$.

Solución exacta, $y = e^{3-3t}$.
"""

# Condiciones del problema
a, b = 0, 1
ya, yb = np.exp(3), 1
N = 8 # Número de nodos

t = np.linspace(a, b, N)

"""Dada la estructura de la ecuación diferencial, suponiendo que
$$ y(t) = \sum_{j=1}^n c_j t^j $$

tenemos que las constantes satisfacen la ecuaciones
$$c_1 = e^3$$
$$ \sum_{j=1}^n [j(j-1)t^{j-2} - 3t^j + 2jt^{j-1}]c_j = 0 $$
$$ \sum_{j=1}^n c_j = 1 $$

Lo cual se puede representar de forma matricial, considerando los tiempos $t_i$, y se implementara de esa manera.
"""

# Matriz de movimiento
A = np.zeros((N,N))

A[0,0] = 1 # Primera ecuación

# Renglones intermedios
for j in range(N):
  A[1:-1, j] = j*(j-1)*t[1:-1]**(j-2) + 2*j*t[1:-1]**(j-1) - 3*t[1:-1]**j #Error de los indeces

A[-1, :] = np.ones(N) # Última ecuación

# Vector
v = np.zeros(N)
v[0], v[-1] = ya, yb

sol = colocacion(A,v,t)

def y(t):
  return np.exp(3-3*t)

plt.plot(t, sol, '-', label = 'Solución del método')
plt.plot(t, y(t), '--r', label = 'Solución exacta')
plt.plot([a,b], [ya,yb], 'ok', label = 'Cond. Frontera')

plt.title('Método de colocación')
plt.legend()
plt.show()
