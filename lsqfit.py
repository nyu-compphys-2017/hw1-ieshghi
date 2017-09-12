import numpy as np
import matplotlib.pyplot as plt

def program(): #This is the main program for problem 3.8
	x,y = readfile()
	plt.scatter(x,y,c='red')
	m,c = calce(x,y)
	fity = m*x+c
	plt.plot(x,fity,'k-')

	#Now let's calculate h.
	h = m*1.6*10**(-19)
	scaled = h*10**34 #we don't want to carry this stupid exponent, since we care only about percent error, so the exponents of 10^34 vanish
	error = abs((scaled-6.62607004)/6.6207004)
	print(error)

	#The error we get for this is ~1%

	return 0
	

def readfile(): #reads millikan.txt
	dat = np.loadtxt("millikan.txt")
	x = dat[:,0]*1.0
	y = dat[:,1]*1.0
	return x,y

def calce(x,y): #calculates Ex,Ey,Exx,Exy
	n = len(x)
	ex = sum(x)*1.0/n	
	ey = sum(y)*1.0/n	
	exx = sum(x**2)*1.0/n	
	exy = sum(x*y)*1.0/n

	m = (exy-ex*ey)/(exx-ex**2)
	c = (exx*ey-ex*exy)/(exx-ex**2)

	return m,c
