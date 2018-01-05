#!/usr/bin/env python3
# -*- encoding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter 

M = 64*1024*1024*8 # Size: 64 MiB

# Valore di N da 100 mila a 10 milioni 
N = np.logspace(7, 11, 1000)

# Calcola probabilità falsi positivi
P = 0.6185**(M/N)

# Calcola numero di funzioni di hash ottimali
K = np.ceil(-np.log2(P))

plt.plot(N, P, "b-")
plt.ylabel("probabilità falso positivo (P)", color="b")
plt.xlabel("numero di elementi (N)")
plt.tick_params("y", colors="b")
plt.xscale("log")
plt.grid(True)

plt2 = plt.twinx()
plt2.plot(N, K, "g-")
plt2.set_ylabel("numero di funzioni di hash (K)", color="g")
plt2.tick_params("y", colors="g")

plt.tight_layout()
plt.savefig("bloom_parms_2.png")
plt.show()
