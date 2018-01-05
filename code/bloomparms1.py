#!/usr/bin/env python3
# -*- encoding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter 

M = 64*1024*1024*8 # Size: 64 MiB

# Scala logaritmica per P da 10% a 0.1%
P = np.logspace(-1, -4, 1000)

# Calcola numero di elementi ottimale
N = np.ceil(M*0.480453014/-np.log(P))

# Calcola numero di funzioni di hash ottimali
K = np.ceil(-np.log2(P))

plt.plot(P, N, "b-")
plt.ylabel("numero di elementi (N)", color="b")
plt.xlabel("probabilità falso positivo (P)")
plt.tick_params("y", colors="b")
plt.xscale("log")
plt.grid(True)

plt2 = plt.twinx()
plt2.plot(P, K, "g-")
plt2.set_ylabel("numero di funzioni di hash (K)", color="g")
plt2.tick_params("y", colors="g")

plt.tight_layout()
plt.savefig("bloom_parms_1.png")
plt.show()
