# reference: J. M. Bardeen
#  "Timelike and Null Geodesics in the Kerr Metric"
#   in Les Houches 1972 summer school lectures, fig6

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

a_min,a_max = 0.001, 0.9998 # range of Kerr parameter

def PlotKerrShadow(a, theta=np.pi/2, N=200, fill=True, **kw):
    """
    a = Kerr parameter (0<a<1)
    theta = observer's polar coordinate in Kerr spacetime
    N = number of plotting points
    fill = fill shadow or not
    kw = keyword arguments passed to plot or fill_between
    """
    if a < a_max:
        def lam(r): # Bardden eq(48)
            return (-r**3 + 3*r**2 - a**2*(r+1))/a/(r-1)
        def eta(r): # Bardeen eq(49)
            return r**3*(4*a**2 - r*(r-3)**2)/a**2/(r-1)**2
    else:
        def lam(r): # Bardden eq(51)
            return -r**2 + 2*r + 1
        def eta(r): # Bardeen eq(52)
            return r**3*(4-r)

    def beta2(r): # Bardeen eq(42b)
        return eta(r) + a**2*np.cos(theta)**2\
            - lam(r)**2/np.tan(theta)**2

    if a < a_min: # Schwarzschild case
        r1,r2 = -3*np.sqrt(3), 3*np.sqrt(3)
    else:
        r1 = newton(beta2, 1.05) if a < a_max else 1
        r2 = newton(beta2, 4)

    x = np.tanh(np.linspace(-10, 10, N))
    r = r1 + (r2-r1)*(1+x)/2

    if a < a_min: # Schwarzschild case
        alpha,beta = r, np.sqrt(27-r**2)
    else:
        alpha = -lam(r)/np.sin(theta) # Bardeen eq(42a)
        beta = np.sqrt(beta2(r)) # Bardeen eq(42b)

    if fill:
        plt.fill_between(alpha, beta, -beta, **kw)
    else:
        plt.plot(alpha,beta,**kw)
        plt.plot(alpha,-beta,**kw)
        if a < a_max: return
        plt.plot(alpha[[0,0]],[-beta[0],beta[0]],**kw)
