# -*- coding: utf-8 -*-
"""Esfera de Bloch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sWp-VlAjZlepbUL1XpKNPHT-f_JHWbED
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, color='cyan', alpha=0.3, rstride=5, cstride=5, edgecolor='k')

ax.quiver(0, 0, 0, 1, 0, 0, color="red", arrow_length_ratio=0.1, linewidth=2)
ax.quiver(0, 0, 0, 0, 1, 0, color="green", arrow_length_ratio=0.1, linewidth=2)
ax.quiver(0, 0, 0, 0, 0, 1, color="blue", arrow_length_ratio=0.1, linewidth=2)

ax.text(1.1, 0, 0, "$|1\\rangle$", color="red", fontsize=16)
ax.text(0, 1.1, 0, "$|+\\rangle$", color="green", fontsize=16)
ax.text(0, 0, 1.1, "$|0\\rangle$", color="blue", fontsize=16)
ax.text(-1.2, 0, 0, "$|-1\\rangle$", color="red", fontsize=16)
ax.text(0, -1.2, 0, "$|-\\rangle$", color="green", fontsize=16)
ax.text(0, 0, -1.2, "$|\\pi\\rangle$", color="blue", fontsize=16)

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

"""Imagine a esfera de Bloch como um globo terrestre para qubits, os "átomos" básicos da computação quântica! Em vez de locais como o Polo Norte ou o Equador, a esfera de Bloch mostra onde o qubit está "apontando", seja para representar um estado de 0, 1, ou algo misteriosamente entre os dois.

No mundo quântico, um qubit não precisa escolher entre 0 ou 1 como os bits clássicos (se é que os bits realmente têm escolha). Em vez disso, ele pode estar em qualquer lugar da superfície da esfera! O topo da esfera representa o estado ∣0⟩ (onde o qubit “se sente” 0), e o fundo representa ∣1⟩(um qubit totalmente “1”).

Agora, imagine girar o qubit! A rotação muda a "orientação" do qubit na esfera. Esses giros são chamados de portas quânticas, e elas são os comandos que ajustam a direção do qubit. Assim, com algumas rotações (ou seja, operações quânticas), podemos fazer o qubit passear pela esfera, combinando probabilidades até chegar no resultado final desejado!

A esfera de Bloch é o mapa para entender esses giros e estados exóticos, ajudando cientistas a visualizar como preparar e manipular qubits para resolver problemas complexos de forma super rápida!
"""