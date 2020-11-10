import numpy as np
import math
import random
import matplotlib.pyplot as plt

pi = 3.1415926535
def E(x,y,z = 2,l = 0.000006):
    ''' integrand of fresnel-kirchoff diffraction integral'''
    return complex(z*(x**2 + y**2 + z**2)**(-2)*np.cos(2*pi*(x**2 + y**2 + z**2)**(0.5)/l), z*(x**2 + y**2 + z**2)**(-2)*np.sin(2*pi*(x**2 + y**2 + z**2)**(0.5)/l))

def pattern(xsize = 0.003, ysize = 0.00003, z = 1, l = 0.000006):
    V = xsize*ysize   #area
    n = 30              #number of points to sample at
    k = 30              #O(k^2) is number of points at which field components (and hence intensity) are calculated
    kstep = (xsize + ysize)/2         #Step size for above side lengths

    #Random Sampling
    montepoints = np.random.rand(n, 2)
    for i in range(n):
        montepoints[i][0] = montepoints[i][0]*xsize*0.5*(-1)**(random.randint(1, 4))
        montepoints[i][1] = montepoints[i][1]*ysize*0.5*(-1)**(random.randint(1,4))
    #print(montepoints)

    #Plot the randomly sampled points
##    plt.close()
##    plt.scatter(np.transpose(montepoints)[0], np.transpose(montepoints)[1])
##    plt.show()

    #Integration
    phi_real = np.zeros((k,k))   
    phi_im = np.zeros((k,k))
    phi = np.zeros((k,k))
    for ity in range(k):
        for itx in range(k):
            f_real = 0
            f2_real = 0
            f_im = 0
            f2_im = 0
            r = [-k*kstep/2 + itx*kstep, -k*kstep/2 + ity*kstep]
            for monti in range(n):
                f_real += (E(r[0] - montepoints[monti][0], r[1] - montepoints[monti][1], z, l).real)/n
                f2_real += (E(r[0] - montepoints[monti][0], r[1] - montepoints[monti][1], z, l).real)**2 /n       #Not needed 
                f_im += (E(r[0] - montepoints[monti][0], r[1] - montepoints[monti][1], z, l).imag)/ n   
                f2_im += (E(r[0] - montepoints[monti][0], r[1] - montepoints[monti][1], z, l).imag)**2 /n         #Not needed
            phi_real[ity][itx] = V*f_real 
            phi_im[ity][itx] = V*f_im 
            phi[ity][itx] = (phi_real[ity][itx]**2 + phi_im[ity][itx]**2)/(l**2)
    return phi

##Monte Carlo Party ends here


