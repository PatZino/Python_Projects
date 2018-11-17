# Input: space interval [xl,xr], time interval [yb,yt],
#        number of space steps M, number of time steps N
# Output: solution w
# Example usage: w=crank(0,1,0,1,10,10)

from numpy import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt

def crank(xl,xr,yb,yt,M,N,f,l,r):
	D = 1.									# diffusion coefficient
	h = float(xr-xl)/M; k=float(yt-yb)/N; m=M-1; n=N
	sigma = D*k/(h*h)
	a  = diag(2+2*sigma*ones(m)) + diag(-sigma*ones(m-1),1) # define tridiagonal matrices a and b
	b  = diag(2-2*sigma*ones(m)) + diag( sigma*ones(m-1),1) 
	a += diag(-sigma*ones(m-1),-1)
	b += diag( sigma*ones(m-1),-1)
	xvals = linspace(xl,xr,M+1)
	yvals = linspace(yb,yt,N+1)
	w = zeros((N+1,m))   					# 1st index is time index
	w[0,:] = f(xvals[1:-1])					# initial conditions
	lvals = l(yvals); rvals = r(yvals)		# boundary conditions
	for j in range(n):
		sides = hstack((lvals[j]+lvals[j+1],zeros(m-2),rvals[j]+rvals[j+1]))
		w[j+1,:] = linalg.solve( a, dot(b,w[j,:]) + sigma*sides )
	w = vstack((lvals,w.T,rvals)).T
	[x,y] = meshgrid(xvals,yvals)			# 3-D plot of solution w
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_wireframe(x, y, w, rstride=100 )
	ax.set_xlabel('x'); ax.set_ylabel('t'); ax.set_zlabel('w')
	#ax.set_zlim(-1,1)   					# (Doesn't work)
	plt.show()
	return w