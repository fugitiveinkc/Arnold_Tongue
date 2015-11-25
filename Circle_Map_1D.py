'''

Title: Circle Map Graph (n vs. Theta_n)
Objective: Plot a circle map given by the equation
	Theta_n+1 = Theta_n + Omega - K/2pi sin(2pi Theta_n)

'''
import numpy as np
import math as m
import matplotlib.pyplot as plt

#First, plot online one value of Theta_n
#Set Theta_n = a sequence, Omega = 0.7, K = 1, n = 500

results = []
n = 500
T_n = np.arange(0,1.2,0.2)
O = 0.7
K = 1

#Note: Right now, this works for multiple seqeunces of T_n.  We need to plot it on the same graph.

for index, t in list(enumerate(T_n)):
	results.append([])
	for x in range(n):
		results[index].append(t)
		t = (t + O - (1/(2*m.pi))*m.sin(2*m.pi*t)) % 1
	plt.plot(range(n), results[index])
print len(results)
plt.show()



	

