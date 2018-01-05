#!/usr/bin/env python3
# -*- encoding: utf8 -*-
import random
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter 

K = 2
M = 8192

bloom = [0]*M
cards = []
errors = []
densities = []

p = 0
N = 0

while p < 1:
	# Simula l'inserimento di un elemento
	for j in range(K):
		x = random.randrange(M)
		bloom[x] = 1

	# Numero effettivo di elementi inseriti
	N += 1

	# Calcola la densità (numero di bit a 1 diviso numero totale di bit)
	p = bloom.count(1) / M

	# Calcola la stima della cardinalità (infinito se diverge) 
	try:
		card = -M/K * math.log(1-p)
	except ValueError: 
		card = math.inf

	# Calcola l'errore commesso rispetto al numero reale di elementi inseriti
	error = abs(card - N) / N

	densities.append(p)
	cards.append(card)
	errors.append(error)


plt.plot(
	densities, cards, "b-", 
	densities, range(1,N+1), "r--",
)
plt.ylabel("numero di elementi stimato/reale", color="b")
plt.xlabel("densità")
plt.tick_params("y", colors="b")

plt2 = plt.twinx()
plt2.plot(
	densities, errors, "g-"
)
plt2.set_ylabel("errore di stima della cardinalità", color="g")
plt2.yaxis.set_major_formatter(FuncFormatter(lambda x,pos=0: "%1.2f%%" % (100*x)))
plt2.tick_params("y", colors="g")

plt.tight_layout()
plt.savefig("bloom_card_error.png")
plt.show()
