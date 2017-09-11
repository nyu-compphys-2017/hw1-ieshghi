import numpy as np
import matplotlib.pyplot as plt

def mandel(N):
	x = np.linspace(-2,2,N)
	y = x.copy()
	grid = np.zeros((N,N))
	for i in range(N): #I am sorry. There should be a smart parallel way to do this, but I'm stupid
		for j in range(N):	
			c = x[i] + 1j*y[j]
			grid[i,j] = checkmand(c)
	plt.imshow(grid,cmap = 'jet')
	
	
def checkmand(c):
	zpr = 0
	z = 0
	n = 0
	while((abs(z)<2)and(n<100)):
		zpr = z**2 + c
		n = n+1
		z = zpr
	if(abs(z)>=2):
		return n
	else:
		return 0
